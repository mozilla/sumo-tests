import unittest
import sys
import tests2 as tests
import multiprocessing
import StringIO
import os
import vars
from selenium import selenium
import sumo_test_data
import sumo_functions

# Wrapper output stream class
# Separates thread output to dict for stderr and stdout as buffer
# Uses os.getpid() as unique identifier
class streamCapture():

    def __init__(self):
        self.io = {}

    # pushes write to corresponding StringIO, instantiating if it doesn't exist
    def write(self, s):
        if os.getpid() not in self.io.keys():
            self.io[os.getpid()] = StringIO.StringIO()
        self.io[os.getpid()].write(s)

    # returns keys for ease of iteration
    def keys(self):
        return self.io.keys()

    # returns all text from StringIO buffer, or blank if none
    def getText(self, key):
        out = self.io.get(key, "")
        if isinstance(out, basestring):
            return out
        else:
            return out.getvalue()

    # unittest.testTextRunner calls flush, but we don't need it
    def flush(self):
        pass

suite_opts = []
test_list = []
counter = 0

# grab command line
suite_opts.extend(sys.argv)
# clear name of file
del suite_opts[0]
# empty sys.argv so unittest doesn't freak
del sys.argv[1:]

# set test_type to type from cmd line params, default FFT
test_type = next((arg for arg in suite_opts if (arg == 'smoketests' or arg == 'bft' or arg == 'fft')), "fft")

# remove arg with test type, pass if defaulted
try:
    del suite_opts[suite_opts.index(test_type)]
except:
    pass

# format test type to that of TCParams
if len(test_type) == 3:
    test_type = test_type.upper()
else:
    test_type = test_type.title()

# gets additional non-tag parameters
cmd_params = [x for x in suite_opts if x[0:1] == '-']

for param in cmd_params:
    if param[1:2] == 'U':
        if not 'http://' in str(param[2:]):
            url_with_protocol = "http://"+str(param[2:])
            vars.ConnectionParameters.baseurl = url_with_protocol
            vars.ConnectionParameters.authurl = url_with_protocol
            print "This suite runs on %s" %(vars.ConnectionParameters.baseurl)
        vars.ConnectionParameters.authurlssl = url_with_protocol.replace("http", "https")
        vars.ConnectionParameters.baseurl_ssl = url_with_protocol.replace("http", "https")
        
for opt in suite_opts:
    if opt[0:1] == "-":
        del suite_opts[suite_opts.index(opt)]

test_info_list = []

# adds test if a tag matches a cmd line param, otherwise adds all tests in test type
if len(suite_opts) > 0:
    for test in tests.testlist.FFT:
        for tag_inner in suite_opts:
            if (tag_inner in test["tags"]):
                test_info_list.append(test)
                break
else:
    test_info_list.extend(getattr(tests.testlist, test_type))

# imports all necessary TC modules and initializes copies of TCparams
for test in test_info_list:
    # import module
    test_list.append(__import__(test["testcase"]["module"]))
    # construct class in temp var to avoid self referencing
    temp_class = getattr(test_list[counter], test["testcase"]["class"])
    if temp_class == None:
        print "Unknown test class: %s.%s" % (test["testcase"]["module"], test["testcase"]["class"])
        sys.exit(1)
    if not hasattr(temp_class, test["testcase"]["method"]):
        print "Unknown test method: %s.%s.%s" % (test["testcase"]["module"], test["testcase"]["class"], test["testcase"]["method"])
        sys.exit(1)
    # copy class to list
    test_list[counter] = temp_class
    counter += 1

# holds TC results
suiteFinalResult = []

# initialize wrapper stream class
outstream = streamCapture()
errstream = streamCapture()

class MasterSuite(unittest.TestCase):

    def runTest(self):
        global suiteFinalResult

        # holds list of all processes since there's no analogous version of threading.enumerate()
        processList = []

        # thread/process-safe queue for transferring results between processes
        q = multiprocessing.Queue()

        for browser in getattr(vars.ConfigOptions, test_type):
            # start process to run target, passing args since processes are sandboxed
            tempProc = multiprocessing.Process(target=ThreadTestRunner, args=(q,browser,test_list,test_info_list))
            tempProc.start()
            processList.append(tempProc)

        # join() the processes to the spawning process so that it doesn't continue until all the processes finish
        outputs = []
        for process in processList:
            if process is not multiprocessing.current_process():
                outputs.append(q.get())
                process.join()

        # remap stdout and stderr to regular console output
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__

        # iterate over result queue
        while not q.empty():
            outputs.append(q.get())
        for streams in outputs:
            # save stream list temporarily
            #streams = q.get()
            # get pid set for unique printouts
            pidSet = set(streams[0].keys()) | set(streams[1].keys())
            for key in pidSet:
                print "===========stderr=========================="
                print unicode(streams[1].getText(key))
                print "===========stdout=========================="
                print unicode(streams[0].getText(key))
                print "==========================================="
                print "==========================================="
                print "===========================================\n\n"
            suiteFinalResult.extend(streams[2])

        # iterate through results and pass/fail accordingly
        for x in suiteFinalResult:
            if x:
                pass
            else:
                raise AssertionError()

# multiprocessing function 
def ThreadTestRunner(q, browser, test_list, test_info_list):
    sys.stdout = outstr = streamCapture()
    sys.stderr = errstr = streamCapture()

    print >> sys.stdout, "Output for browser: %s" % browser
    print >> sys.stderr, "Output for browser: %s" % browser
    
    # recreate for new process, to be returned
    suiteFinalResult = []
    
    suite = unittest.TestSuite()
    runner = unittest.TextTestRunner(stream=sys.stderr)
    
    counter = 0
    for test in test_list:
        # decorator to modify setUp of all functions to open the appropriate browser
        # replaces original setUp
        def setUpDecorator(fn, test, env):
            def setUp(*args, **kwargs):
                setattr(test, 'browser', env)
                vars.ConnectionParameters.browser = test.browser
                #fn(*args, **kwargs)
                setattr(test, 'selenium', selenium(vars.ConnectionParameters.server,vars.ConnectionParameters.port,env,vars.ConnectionParameters.baseurl))
                test.selenium.start()
                test.selenium.set_timeout(vars.ConnectionParameters.page_load_timeout)
                setattr(test, 'accounts', sumo_test_data.SUMOtestData())
                setattr(test, 'functions', sumo_functions.SUMOfunctions())
            return setUp
        setattr(test, 'setUp', setUpDecorator(getattr(test, 'setUp'), test, browser))
        suite.addTest(test(test_info_list[counter]["testcase"]["method"]))
        counter += 1

    # run the suite
    result = runner.run(suite)
    # evaluate the results
    suiteFinalResult.append(result.wasSuccessful())
    
    # place results in queue for later retrieval
    q.put([outstr, errstr, suiteFinalResult])
    #q.cancel_join_thread()
    return
    
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(MasterSuite)
    runner = unittest.TextTestRunner().run(suite)
    if not runner.wasSuccessful():
        sys.exit(-1)
    #unittest.main()
