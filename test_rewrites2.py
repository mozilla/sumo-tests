'''
Created on Dec 13, 2010

@author: mozilla
'''
'''
Created on Sep 22, 2010

@author: mozilla
'''
from selenium import selenium
import vars
import unittest
import urllib
import re
import time

class TestRewrites(unittest.TestCase):

    def __init__(self,methodName):
        super(TestRewrites, self).__init__(methodName)
        self.mainURL    = vars.ConnectionParameters.baseurl
        self.numberOne  = "/1"
        self._1         = "/firefox"
        #self._2         = array("/3.5.1","/3.0.12","/2.0.0.20","/3.5b99")
        #self._3         = array("/Linux","/WINNT","/Darwin")
        #self._2         = array("/3.6.3plugin1","/3.6.2")
        self._2         = ["/3.6.4"]
        self._3         = ["/WINNT"]
        self.kbSuffix   = "/kb"
        
         
        us = {"goToUrl":"/en-US","redirectUrl" : "/en-US"}
        pa = {"goToUrl":"/pa-IN","redirectUrl" : "/pa-IN"}
        #self.localesArray = (us,pa)
        self.localesArray = (us,)
                            
                             
        self.key1 = "goToUrl"
        self.key2 = "redirectUrl"
        self.key3 = "hash"
        self.styleMode = "/home/?as=u"
        #self.styleMode = "/Firefox Help?style_mode=inproduct"
        self.styleModePageInfo = "/Page Info window"
        self.styleMode4 = "?style_mode=inproduct"
        self.article_source_suffix = "?as=u"
        #self.selenium
        
        self.echoOnlyFailStm = True
         
        
    def setUp(self):
        self.selenium = selenium(vars.ConnectionParameters.server, vars.ConnectionParameters.port, vars.ConnectionParameters.browser, vars.ConnectionParameters.baseurl)
        self.selenium.start()
        self.selenium.set_timeout(vars.ConnectionParameters.page_load_timeout)
        #self.selenium.open(vars.ConnectionParameters.authurl)
        #self.selenium.open(vars.ConnectionParameters.authurlssl)


    def tearDown(self):
        self.selenium.stop()


    """ // //RewriteRule ^1/([\-a-zA-Z]+)/([\.0-9ab]+(?:pre)?)/([\-_a-zA-Z0-9]+)/([\-a-zA-Z]+)/pageinfo_general\/$ to
// // /$4/kb/Page+Info+window?style_mode=inproduct#General [R,NE] 
// For eg. http://support.mozilla.com/1/firefox/3.6b3pre/Darwin/es-MX/pageinfo_general
//         redirects to
//         http://support.mozilla.com/es/kb/Page+Info+window?style_mode=inproduct#General      
    """
#    def test_redirect_pageinfo(self):
#        one    = {"goToUrl":"/pageinfo_general","redirectUrl" : "\?as=u#General"}
#        two    = {"goToUrl":"/pageinfo_media","redirectUrl" :"\?as=u#Media"}
#        three  = {"goToUrl":"/pageinfo_feed","redirectUrl":"\?as=u#Feeds"}
#        four   = {"goToUrl":"/pageinfo_permissions","redirectUrl":"\?as=u#Permissions"}
#        five   = {"goToUrl":"/pageinfo_security","redirectUrl":"\?as=u#Security"}
#
#         
#        urlPageInfo = (one,two,three,four,five)
#        
#        sel  = self.selenium 
#        for x in self.localesArray:
#            for pageInfo in urlPageInfo:
#                for two in self._2:
#                    for three in self._3:
#                        openUrl = self.numberOne+self._1+two+three+x[self.key1]+pageInfo[self.key1]+"/"
#                        openUrlNoTrailingSlash = self.numberOne+self._1+two+three+(x[self.key1])+pageInfo[self.key1]
#                        expectedUrl = self.mainURL+x[self.key2]+self.kbSuffix+self.styleModePageInfo+pageInfo[self.key2]
#                        sel.open(openUrl)
#                        actualUrl = urllib.unquote(sel.get_location())
#                        if re.search(expectedUrl,actualUrl,re.I) is not None :
#                            self.echoPass("Redirect "+x[self.key1]+pageInfo[self.key1]+" => "+self.styleModePageInfo+pageInfo[self.key2]+" PASS\n")
#                        else:
#                            print "Redirect "+x[self.key1]+pageInfo[self.key1]+" => "+self.styleModePageInfo+pageInfo[self.key2]+" FAIL\n"
#                            print "Expected Redirect: "+expectedUrl+"\n"
#                            print "Actual Redirect: "+actualUrl+"\n"
#                        """ repeat without trailing slash"""
#                        sel.open(openUrlNoTrailingSlash)
#                        actualUrl = urllib.unquote(sel.get_location())
#                        if re.search(expectedUrl,actualUrl,re.I) is not None :
#                            self.echoPass("Redirect "+x[self.key1]+pageInfo[self.key1]+" => "+self.styleModePageInfo+pageInfo[self.key2]+" PASS\n")
#                        else:
#                            print "Redirect "+x[self.key1]+pageInfo[self.key1]+" => "+self.styleModePageInfo+pageInfo[self.key2]+" FAIL\n"
#                            print "Expected Redirect: "+expectedUrl+"\n"
#                            print "Actual Redirect: "+actualUrl+"\n"
#
#    """ //  // RewriteRule ^1/([\-a-zA-Z]+)/([\.0-9ab]+(?:pre)?)/([\-_a-zA-Z0-9]+)/([\-a-zA-Z]+)/firefox-help\/$ to
#//  // /$4/kb/Firefox+Help?style_mode=inproduct [R,NE] 
#// For eg. http://support.mozilla.com/1/firefox/3.6b3pre/Darwin/fr/firefox-help
#//         redirects to
#//         http://support.mozilla.com/fr/kb/Firefox+Help?style_mode=inproduct    
#    """
#    def test_redirect_firefox_help(self):
#        firefoxHelpArr = ["/firefox-help","/firefox-f1","/firefox-osxkey"]
#        
#        sel  = self.selenium 
#        for x in self.localesArray:
#            for two in self._2:
#                for three in self._3:
#                    for fxHelp in firefoxHelpArr:
#                        openUrl                = self.numberOne+self._1+two+three+x[self.key1]+fxHelp+"/"
#                        openUrlNoTrailingSlash = self.numberOne+self._1+two+three+x[self.key1]+fxHelp
#                        expectedUrl = self.mainURL+x[self.key2]+self.styleMode
#                        sel.open(openUrl)
#                        actualUrl = urllib.unquote(sel.get_location())
#                        self.assertEqual(expectedUrl,actualUrl )
#                        """ repeat without trailing slash"""
#                        sel.open(openUrlNoTrailingSlash)
#                        actualUrl = urllib.unquote(sel.get_location())
#                        self.assertEqual(expectedUrl,actualUrl)
                        
#    def test_redirect_preferences(self):
#        one    = {"goToUrl":"/prefs-main","redirectUrl" : "/Options window - General panel","hash" :"\?as=u"}
#        two    = {"goToUrl":"/prefs-clear-private-data","redirectUrl":"/Clear Recent History","hash":"\?as=u"}
#        three    = {"goToUrl":"/prefs-fonts-and-colors","redirectUrl":"/Options window - Content panel","hash":"\?as=u#fonts_and_colors"}
#        four = {"goToUrl":"/prefs-privacy","redirectUrl":"/Options window - Privacy panel","hash":"\?as=u"}
#        five = {"goToUrl":"/prefs-applications","redirectUrl":"/Options window - Applications panel","hash":"\?as=u"}
#        six = {"goToUrl":"/prefs-connection-settings","redirectUrl":"/Options window - Advanced panel","hash":"\?as=u#connection_settings"}
#        seven    = {"goToUrl":"/prefs-tabs","redirectUrl":"/Options window - Tabs panel","hash":"\?as=u"}
#        eight    = {"goToUrl":"/prefs-advanced-javascript","redirectUrl" : "/Options window - Content panel","hash":"\?as=u#advanced_javascript"}
#        nine    = {"goToUrl":"/prefs-languages","redirectUrl":"/Options window - Content panel","hash":"\?as=u#languages"}
#        ten    = {"goToUrl":"/prefs-content","redirectUrl":"/Options window - Content panel","hash":"\?as=u"}
#        eleven = {"goToUrl":"/prefs-security","redirectUrl":"/Options window - Security panel","hash":"\?as=u"}
#        twelve = {"goToUrl":"/prefs-advanced-general","redirectUrl":"/Options window - Advanced panel","hash":"\?as=u"}
#        thirteen = {"goToUrl":"/prefs-advanced-network","redirectUrl":"/Options window - Advanced panel","hash":"\?as=u#advanced_network"}
#        fourteen    = {"goToUrl":"/prefs-advanced-update","redirectUrl":"/Options window - Advanced panel","hash":"\?as=u#advanced_update"}
#        fifteen = {"goToUrl":"/prefs-advanced-encryption","redirectUrl":"/Options window - Advanced panel","hash":"\?as=u#advanced_encryption"}
#        sixteen = {"goToUrl":"/ieusers","redirectUrl":"/Windows start page","hash":"\?as=u"}
#        seventeen    = {"goToUrl":"/eu/ieusers","redirectUrl":"/Windows start page","hash":"\?as=u&eu=1"}
#        eighteen    = {"goToUrl":"/places-locked","redirectUrl" : "/The bookmarks and history system will not be functional","hash":"\?as=u"}
#        nineteen    = {"goToUrl":"/private-browsing","redirectUrl":"/Private Browsing","hash":"\?as=u"}
#        twenty    = {"goToUrl":"/prefs-weave","redirectUrl":"/How to sync Firefox settings between computers","hash":"\?as=u"}
#        #twentyone = {"goToUrl":"/firefox-f1","redirectUrl":"/Firefox Help","hash":""}
#        #twentytwo = {"goToUrl":"/firefox-osxkey","redirectUrl":"/Firefox Help","hash":""}
#        twentythree = {"goToUrl":"/keyboard-shortcuts","redirectUrl":"/Keyboard shortcuts","hash":"\?as=u"}
#        twentyfour    = {"goToUrl":"/eu/keyboard-shortcuts","redirectUrl":"/Keyboard shortcuts","hash":"\?as=u&eu=1"}
#        twentyfive = {"goToUrl":"/plugin-crashed","redirectUrl":"/Plugin crash reports","hash":"\?as=u"}
#        twentysix    = {"goToUrl":"/eu/plugin-crashed","redirectUrl":"/Plugin crash reports","hash":"\?as=u&eu=1"}
#        
#        urlPrefsArray = (one,two,three,four,five,six,seven,eight,nine,ten,eleven,twelve,thirteen,fourteen,fifteen,sixteen,seventeen,eighteen,nineteen,twenty,twentythree,twentyfour,twentyfive,twentysix)
#
#
#        
#        sel  = self.selenium 
#        for x in self.localesArray:
#            for urlPrefs in urlPrefsArray:
#                for two in self._2:
#                    for three in self._3:
#                        openUrl                = self.numberOne+self._1+two+three+x[self.key1]+urlPrefs[self.key1]+"/"
#                        openUrlNoTrailingSlash = self.numberOne+self._1+two+three+x[self.key1]+urlPrefs[self.key1]
#                        expectedUrl = self.mainURL+x[self.key2]+self.kbSuffix+urlPrefs[self.key2]+urlPrefs[self.key3]
#                        sel.open(openUrl)
#                        actualUrl = urllib.unquote(sel.get_location())
#                        self.assertTrue( re.search(expectedUrl,actualUrl,re.I) is not None)
#                        """ repeat without trailing slash"""
#                        sel.open(openUrlNoTrailingSlash)
#                        time.sleep(2)
#                        actualUrl = urllib.unquote(sel.get_location())
#                        self.assertTrue( re.search(expectedUrl,actualUrl,re.I) is not None)
                        
#    def test_redirect_misc(self):
#        """ 
#           // this redirect is for windows 7 support only
#          //  http://support-stage.mozilla.org/1/windows7-support using |en-US| and
#          //  have it redirect to
#          //  http://support-stage.mozilla.org/en-US/kb/Firefox+Help?style_mode=inproduct   
#        """
#        sel = self.selenium
#        openUrl     = self.mainURL+"/1/windows7-support"
#        expectedUrl = self.mainURL+"/en-US"+self.styleMode
#        sel.open(openUrl)
#        actualUrl = urllib.unquote(sel.get_location())
#        self.assertEqual(expectedUrl,actualUrl)
#        
#        
#        """     +# Redirect old discussion forums to new discussion forums
#                +RewriteRule ^forum/3(.*) /en-US/forums/contributors$1 [L,QSA,R=301]
#                +RewriteRule ^([\-a-zA-Z]+)/forum/3(.*) /en-US/forums/contributors$2 [L,QSA,R=301]
#                 +RewriteRule ^forum/4(.*) /en-US/forums/off-topic$1 [L,QSA,R=301]
#                 +RewriteRule ^([\-a-zA-Z]+)/forum/4(.*) /en-US/forums/off-topic$2 [L,QSA,R=301]
#                +RewriteRule ^forum/5(.*) /en-US/forums/knowledge-base-articles$1 [L,QSA,R=301]
#                +RewriteRule ^([\-a-zA-Z]+)/forum/5(.*) /en-US/forums/knowledge-base-articles$2 [L,QSA,R=301]
#        """
#        openUrl     = self.mainURL+"/forum/3"
#        sel.open(openUrl)
#        actualUrl = urllib.unquote(sel.get_location())
#        self.assert_('/forums/contributors' in actualUrl)
#        
#        openUrl     = self.mainURL+"/forum/4"
#        sel.open(openUrl)
#        actualUrl = urllib.unquote(sel.get_location())
#        self.assert_('/forums/off-topic' in actualUrl)
#                        
#        openUrl     = self.mainURL+"/forum/5"
#        sel.open(openUrl)
#        actualUrl = urllib.unquote(sel.get_location())
#        self.assert_('/forums/knowledge-base-articles' in actualUrl)
#        
##        openUrl     = self.mainURL+"/en-US/forum/6"
##        expectedUrl = self.mainURL+"/en-US/questions?tagged=FxHome"
##        sel.open(openUrl)
##        actualUrl = sel.get_location()
##        self.assertEqual(expectedUrl,actualUrl)
#        
#        """ redirect old mobie url's to new sumo url's
#        """
##        sel.open("http://support:stage@mobile-support-stage.mozilla.com")
##        openUrl = "http://mobile-support-stage.mozilla.com/kb/Ask+a+question"
##        expectedUrl = "http://support.mozilla.com/en-US/kb/Ask+a+question"
##        sel.open(openUrl)
##        self.assertEqual(expectedUrl,urllib.unquote(sel.get_location()))
##        openUrl_hhtp_auth = "http://support:stage@mobile-support-stage.mozilla.com"
##        openUrl = "http://mobile-support-stage.mozilla.com/forum/5"
##        expectedStr = "/en-US/questions/new?product=mobile"
##        sel.open(openUrl_hhtp_auth)
##        sel.open(openUrl)
##        self.failUnless(expectedStr in (sel.get_location()))
##        
##        openUrl = "http://mobile-support-stage.mozilla.com/"
##        expectedStr = "/en-US/mobile/"
##        sel.open(openUrl)
##        self.failUnless(expectedStr in (sel.get_location()))
#                
#        """
#        # Contribute shortcut
#        RewriteRule ^contribute/?$ /kb/How+to+contribute [L,QSA,R=302]  
#        """
#        openUrl     = "/contribute"  
#        expectedStr = "/en-US"+self.kbSuffix+"/How to contribute"
#        sel.open(openUrl)
#        self.failUnless(expectedStr in (urllib.unquote(sel.get_location())))
        
    def test_redirect_iphone(self):
        
        product_iphone  = "/firefox-home"
        platform_iphone = "/iPhone"
        helptopic_iphone = "/install"
        sel  = self.selenium 
        for x in self.localesArray:
            for two in self._2:
                openUrl     = str(self.mainURL)+str(self.numberOne)+str(product_iphone)+two+str(platform_iphone)+str(x[self.key1])
                expectedUrl = self.mainURL+"/en-US"+self.kbSuffix+"/What is Firefox Home"+self.article_source_suffix
                sel.open(openUrl)
                actualUrl = urllib.unquote(sel.get_location())
                self.assertEqual(expectedUrl,actualUrl)
            
                openUrl     = str(self.mainURL)+self.numberOne+product_iphone+two+platform_iphone+x[self.key1]+helptopic_iphone
                expectedUrl = self.mainURL+"/en-US"+self.kbSuffix+"/How to set up Firefox Home on your iPhone"+self.article_source_suffix
                sel.open(openUrl)
                actualUrl = urllib.unquote(sel.get_location())
                self.assertEqual(expectedUrl,actualUrl)
                
    def test_old_kb_redirects(self):
        
        one    = {"goToUrl":"/Firefox+Help","redirectUrl" : "/home/"}
        two    = {"goToUrl":"/Windows+start+page","redirectUrl":"/home/"}
        three    = {"goToUrl":"/Firefox+Support+Home+Page","redirectUrl":"/home/"}
        four = {"goToUrl":"/Get+help+with+Firefox+4+Beta","redirectUrl":"/home/"}
        five = {"goToUrl":"/Localization+Dashboard","redirectUrl":"/contributors"}
        six = {"goToUrl":"/All+Knowledge+Base+articles","redirectUrl":"/contributors"}
        seven    = {"goToUrl":"/Mobile+Help+and+Tutorials","redirectUrl":"/mobile/#os=android&browser=m4"}
        eight    = {"goToUrl":"/Article+list","redirectUrl" : "/all"}


        kb_array = (one,two,three,four,five,six,seven)
        sel = self.selenium
        for x in self.localesArray:
            for y in kb_array:
                openUrl = str(self.mainURL)+(x[self.key1])+self.kbSuffix+y[self.key1]
                expectedUrl = self.mainURL+x[self.key2]+y[self.key2]
                sel.open(openUrl)
                actualUrl = urllib.unquote(sel.get_location())
                self.assertEqual(expectedUrl,actualUrl )
        
        """ ^kb/Article\+list$ /kb/all """
        kb_array2 = (eight,)
        sel = self.selenium
        for x in self.localesArray:
            for y in kb_array2:
                openUrl = str(self.mainURL)+str(x[self.key1])+str(self.kbSuffix)+str(y[self.key1])
                expectedUrl = self.mainURL+x[self.key2]+str(self.kbSuffix)+y[self.key2]
                sel.open(openUrl)
                actualUrl = urllib.unquote(sel.get_location())
                self.assertEqual(expectedUrl,actualUrl )
        
        """ non-localized kb redirects"""           
        one    = {"goToUrl":"/Live+Chat","redirectUrl":"/chat/"}
        two    = {"goToUrl":"/Support+Website+Forums","redirectUrl" : "/questions"}
        
        kb_array2 = (one,two)
        for x in self.localesArray:
            for y in kb_array2:
                openUrl = str(self.mainURL)+(x[self.key1])+self.kbSuffix+y[self.key1]
                expectedUrl = self.mainURL+"/en-US"+y[self.key2]
                sel.open(openUrl)
                actualUrl = urllib.unquote(sel.get_location())
                self.assertEqual(expectedUrl,actualUrl)
                                
    def echoPass(self,string):
        if(not self.echoOnlyFailStm):
            print(string)     


if __name__ == "__main__":
    unittest.main()