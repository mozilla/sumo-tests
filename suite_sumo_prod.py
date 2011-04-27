'''
Created on May 25, 2010

@author: mozilla
'''
import unittest
import vars
import tests_prod

for test in tests_prod.testlist.list:
    module_name = "import " + test[0]
    exec module_name

class SUMOtestSuite(unittest.TestCase):

    def testSUMOtestSuite(self):
        
        test_result_array = []
        counter = 0
        
        browser_array = [
                        #["10.250.5.250",5568,"IE-8;en-us;Vista"],
                        #["qa-selenium.mv.mozilla.com",5554,"Firefox-3.5;en-us;MacOSX6"],
                        #["192.168.165.128",5566,"IE-7;en-us;WinXP"],
                        ["192.168.165.128",5571,"Firefox-default;en-us;WinXP"],
                        #["qa-selenium.mv.mozilla.com",5557,"Safari;en-us;MacOSX6"],
                        #["192.168.165.128",5555,"Firefox-3.5;en-us;WinXP"],
                        #["qa-selenium.mv.mozilla.com",5556,"Firefox-default;en-us;MacOSX6"]
                        ]
                        
                        #["192.168.165.128",5563,"Chrome;en-us;WinXP"],
                        #["qa-selenium.mv.mozilla.com",5563,"Chrome;en-us;MacOSX6"],
                        #["192.168.165.130",5573,"Firefox-default;en-us;Linux"],
        
        
        #browser_array = [["localhost", 5652, "*firefox"]]
        
        # loop thru browsers
        for curr_browser in browser_array:
            
            # initialize for new test.
            suite = unittest.TestSuite()
            runner = unittest.TextTestRunner()

            # AMO Search API 1.2 tests
            for test in tests_prod.testlist.list:
                constr = str(test[0]) + "." + str(test[1]) + "('" + str(test[2]) + "')"
                addtest = "suite.addTest(" + constr + ")"
                exec addtest
                        
            #vars.ConnectionParameters.server = curr_browser[0]
            #vars.ConnectionParameters.port = curr_browser[1]
            vars.ConnectionParameters.browser = curr_browser[2]
            vars.ConnectionParameters.baseurl = "http://support.mozilla.com"
            vars.ConnectionParameters.authurl = "http://support.mozilla.com"
            vars.ConnectionParameters.authurlssl = "https://support.mozilla.com"
   
   
            # run the suite
            print '\r\n------------------------------------------------------\r\n'
            print 'Running tests in Browser = %s\r\n' %(curr_browser[2])
            test_result_array.append(runner.run(suite))
            print 'test result instance %s \r\n' %(test_result_array[counter])
            counter = counter+1
 
        
        for x in test_result_array:
            if x.wasSuccessful():
                pass
            else:
                raise AssertionError(str(x.failures))
        
        

if __name__ == "__main__":
    unittest.main()
