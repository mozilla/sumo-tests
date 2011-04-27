'''
Created on May 25, 2010

@author: mozilla
'''
import unittest
import sumo_functions
import vars
import tests
import sys

args = sys.argv

if len(args) < 2:
    type = "smoke"
else:
    type = args[1]
    
if type == "smoke":
    for test in tests.testlist.smoke_list:
        module_name = "import " + test[0]
        exec module_name
elif type == "bft":
    for test in tests.testlist.bft_list:
        module_name = "import " + test[0]
        exec module_name
elif type == "fft":
    for test in tests.testlist.fft_list:
        module_name = "import " + test[0]
        exec module_name
   
class SUMOtestSuite(unittest.TestCase):
    
    def testSUMOtestSuite(self):
       
        test_result_array = []
        counter = 0

        smoke_browser_array = []
        bft_browser_array = []
        fft_browser_array = []
        
        browser_array = []
        
        #smoketest
        smoke_browser_array.append(["192.168.165.128",5571,"Firefox-default;en-us;Vista"])
        
        #bft
        bft_browser_array.append(["10.250.5.250",5568,"IE-8;en-us;Vista"])
        
        #fft
        fft_browser_array.append(["qa-selenium.mv.mozilla.com",5554,"Firefox-3.5;en-us;MacOSX6"])
        fft_browser_array.append(["qa-selenium.mv.mozilla.com",5557,"Safari;en-us;MacOSX6"])
        fft_browser_array.append(["192.168.165.128",5555,"Firefox-3.5;en-us;WinXP"])
        fft_browser_array.append(["qa-selenium.mv.mozilla.com",5556,"Firefox-default-b;en-us;MacOSX6"])
        
        #fft_browser_array.append(["192.168.165.128",5566,"IE-7;en-us;WinXP"])
        
        #cannot authenticate via url
        #browser_array.append(["192.168.165.128",5563,"Chrome;en-us;WinXP"])
        #browser_array.append(["qa-selenium.mv.mozilla.com",5563,"Chrome;en-us;MacOSX6"])
        #browser_array.append(["192.168.165.130",5573,"Firefox-default;en-us;Linux"])
        
       
                        
        if type == "smoke":
            browser_array.extend(smoke_browser_array)
        elif type == "bft":
            browser_array.extend(smoke_browser_array)
            browser_array.extend(bft_browser_array)
        elif type == "fft":
            browser_array.extend(smoke_browser_array)
            browser_array.extend(bft_browser_array)
            browser_array.extend(fft_browser_array)
        
   

        #localhost
        #browser_array = [["localhost", 5652, "*firefox"]]

        
        # loop thru browsers
        for curr_browser in browser_array:
            
            # initialize for new test.
            suite = unittest.TestSuite()
            runner = unittest.TextTestRunner()

            # AMO Search API 1.2 tests
            if type == "smoke":
                for test in tests.testlist.smoke_list:
                    constr = str(test[0]) + "." + str(test[1]) + "('" + str(test[2]) + "')"
                    addtest = "suite.addTest(" + constr + ")"
                    exec addtest
            elif type == "bft":
                for test in tests.testlist.bft_list:
                    if test in tests.testlist.smoke_list and curr_browser in smoke_browser_array:
                        continue
                    constr = str(test[0]) + "." + str(test[1]) + "('" + str(test[2]) + "')"
                    addtest = "suite.addTest(" + constr + ")"
                    exec addtest 
            elif type == "fft":
                for test in tests.testlist.fft_list:
                    if test in tests.testlist.bft_list and (curr_browser in bft_browser_array or curr_browser in smoke_browser_array):
                        continue
                    constr = str(test[0]) + "." + str(test[1]) + "('" + str(test[2]) + "')"
                    addtest = "suite.addTest(" + constr + ")"
                    exec addtest                    

            vars.ConnectionParameters.browser = curr_browser[2]
   
   
            # run the suite
            print '\r\n------------------------------------------------------\r\n'
            print 'Running tests in Browser = %s\r\n' %(curr_browser[2])
            test_result_array.append(runner.run(suite))
            print 'test result instance %s \r\n' %(test_result_array[counter])
            counter = counter+1
 
        
        for x in test_result_array:
            #print x.testsRun
            #errs = x.errors[0][1]
            if x.wasSuccessful():
                    pass
            else:
                    raise AssertionError(str(x.failures))
            
        

if __name__ == "__main__":
    unittest.main(argv=["type"])
