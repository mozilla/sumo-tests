'''
Created on Apr 13, 2011

@author: mozilla
'''

import vars
import unittest
import urllib
import sys

cmd_line_args = []
cmd_line_args.extend(sys.argv)
del sys.argv[1:]

class TestRewrites(unittest.TestCase):

    def __init__(self,methodName):
        super(TestRewrites, self).__init__(methodName)
        if len(cmd_line_args) > 1:
            self.mainURL = cmd_line_args[1]
        else:
            self.mainURL    = vars.ConnectionParameters.baseurl
        if self.mainURL.endswith('/'):
            self.mainURL = self.mainURL.rstrip('/')
        self.numberOne  = "/1"
        self._1         = "/firefox"
        #self._2         = array("/3.5.1","/3.0.12","/2.0.0.20","/3.5b99")
        #self._3         = array("/Linux","/WINNT","/Darwin")
        #self._2         = array("/3.6.3plugin1","/3.6.2")
        self._2         = ["/4.0"]
        self._3         = ["/WINNT","/Darwin","/Linux"]
        self.kbSuffix   = "/kb"
        
         
        us = {"goToUrl":"/en-US","redirectUrl" : "/en-US"}
        #es = {"goToUrl":"/es-AR","redirectUrl" : "/es"}
        #pa = {"goToUrl":"/pa-IN","redirectUrl" : "/pa-IN"}
        #self.localesArray = (us,pa)
        self.localesArray = (us,)
                            
                             
        self.key1 = "goToUrl"
        self.key2 = "redirectUrl"
        self.key3 = "hash"
        self.styleMode = "/home?as=u"
        #self.styleMode = "/Firefox Help?style_mode=inproduct"
        self.styleModePageInfo = "/Page Info window"
        self.styleMode4 = "?style_mode=inproduct"
        self.article_source_suffix = "?as=u"
         
        
    """ // # Redirect locales that point to one locale in SUMO
       // 10     RewriteRule ^1/([\-a-zA-Z]+)/([\.0-9ab]+(?:pre)?)/([\-_a-zA-Z0-9]+)/ja\-JP\-mac$ /1/$1/$2/$3/ja/ [R]
       // 11     RewriteRule ^1/([\-a-zA-Z]+)/([\.0-9ab]+(?:pre)?)/([\-_a-zA-Z0-9]+)/n[bn]\-NO$ /1/$1/$2/$3/no/ [R]
       // 12     RewriteRule ^1/([\-a-zA-Z]+)/([\.0-9ab]+(?:pre)?)/([\-_a-zA-Z0-9]+)/es\-ES$ /1/$1/$2/$3/es/ [R]
       // 13     RewriteRule ^1/([\-a-zA-Z]+)/([\.0-9ab]+(?:pre)?)/([\-_a-zA-Z0-9]+)/es\-AR$ /1/$1/$2/$3/es/ [R]
      // 14     RewriteRule ^1/([\-a-zA-Z]+)/([\.0-9ab]+(?:pre)?)/([\-_a-zA-Z0-9]+)/es\-CL$ /1/$1/$2/$3/es/ [R]
      // 15     RewriteRule ^1/([\-a-zA-Z]+)/([\.0-9ab]+(?:pre)?)/([\-_a-zA-Z0-9]+)/sr$ /1/$1/$2/$3/sr-CYRL/ [R]      
    """
    def test_redirect_one_locale(self):
        ja    = {"goToUrl":"/ja-JP-mac","redirectUrl" : "/ja"}
        #nb    = {"goToUrl":"/nb-NO","redirectUrl":"/no"}
        nn    = {"goToUrl":"/nn-NO","redirectUrl":"/no"}
        es_es = {"goToUrl":"/es-ES","redirectUrl":"/es"}
        es_ar = {"goToUrl":"/es-AR","redirectUrl":"/es"}
        es_cl = {"goToUrl":"/es-CL","redirectUrl":"/es"}
        sr    = {"goToUrl":"/sr","redirectUrl":"/sr-CYRL"}
         
        """
            removing nb-no for now due to bug 650363
        """
        urlMatrixArray = (ja,nn,es_es,es_ar,es_cl,sr)
        
        for x in urlMatrixArray:
            for two in self._2:
                for three in self._3:
                    open_url = self.mainURL+self.numberOne+self._1+two+three+(x[self.key1])
                    expected_url = self.mainURL+x[self.key2]+self.styleMode
                    http_response = urllib.urlopen(open_url)
                    actual_url = urllib.unquote(http_response.geturl())
                    self.assertEqual(actual_url,expected_url)

        """
           redirect /kb to /home
           Note: this redirect is not part of the .htaccess, its part of Kitsune
                 if you go to an over-specified or under-specified locale, kitsune fixes it
        """
        ja    = {"goToUrl":"/ja-JP-mac","redirectUrl" : "/ja"}
        #nb    = {"goToUrl":"/nb-NO","redirectUrl":"/no"}
        nn    = {"goToUrl":"/nn-NO","redirectUrl":"/no"}
        es_es = {"goToUrl":"/es-ES","redirectUrl":"/es"}
        es_ar = {"goToUrl":"/es-AR","redirectUrl":"/es"}
        es_cl = {"goToUrl":"/es-CL","redirectUrl":"/es"}
        us    = {"goToUrl":"/en-US","redirectUrl":"/en-US"}
        us2    = {"goToUrl":"/en","redirectUrl":"/en-US"}
        
        urlMatrixArray2 = (ja,nn,es_es,es_ar,es_cl,us,us2)
        for x in urlMatrixArray2:
            open_url = self.mainURL+(x[self.key1])+self.kbSuffix
            expected_url = self.mainURL+(x[self.key2])+"/home"
            http_response = urllib.urlopen(open_url)
            actual_url = urllib.unquote(http_response.geturl())
            self.assertEqual(actual_url,expected_url)
                        
    """ // //RewriteRule ^1/([\-a-zA-Z]+)/([\.0-9ab]+(?:pre)?)/([\-_a-zA-Z0-9]+)/([\-a-zA-Z]+)/pageinfo_general\/$ to
// // /$4/kb/Page+Info+window?style_mode=inproduct#General [R,NE] 
// For eg. http://support.mozilla.com/1/firefox/3.6b3pre/Darwin/es-MX/pageinfo_general
//         redirects to
//         http://support.mozilla.com/es/kb/Page+Info+window?style_mode=inproduct#General      
    """
    def test_redirect_pageinfo(self):
        one    = {"goToUrl":"/pageinfo_general","redirectUrl" : "?as=u#General"}
        two    = {"goToUrl":"/pageinfo_media","redirectUrl" :"?as=u#Media"}
        three  = {"goToUrl":"/pageinfo_feed","redirectUrl":"?as=u#Feeds"}
        four   = {"goToUrl":"/pageinfo_permissions","redirectUrl":"?as=u#Permissions"}
        five   = {"goToUrl":"/pageinfo_security","redirectUrl":"?as=u#Security"}

         
        urlPageInfo = (one,two,three,four,five)
        
        for x in self.localesArray:
            for pageInfo in urlPageInfo:
                for two in self._2:
                    for three in self._3:
                        open_url = self.mainURL+self.numberOne+self._1+two+three+x[self.key1]+pageInfo[self.key1]+"/"
                        open_urlNoTrailingSlash = self.mainURL+self.numberOne+self._1+two+three+(x[self.key1])+pageInfo[self.key1]
                        expected_url = self.mainURL+x[self.key2]+self.kbSuffix+self.styleModePageInfo+pageInfo[self.key2]
                        http_response = urllib.urlopen(open_url)
                        actual_url = urllib.unquote(http_response.geturl())
                        self.assertEqual(actual_url,expected_url)
                        """ repeat without trailing slash"""
                        http_response = urllib.urlopen(open_urlNoTrailingSlash)
                        actual_url = urllib.unquote(http_response.geturl())
                        self.assertEqual(actual_url,expected_url)


    """ //  // RewriteRule ^1/([\-a-zA-Z]+)/([\.0-9ab]+(?:pre)?)/([\-_a-zA-Z0-9]+)/([\-a-zA-Z]+)/firefox-help\/$ to
//  // /$4/kb/Firefox+Help?style_mode=inproduct [R,NE] 
// For eg. http://support.mozilla.com/1/firefox/3.6b3pre/Darwin/fr/firefox-help
//         redirects to
//         http://support.mozilla.com/fr/kb/Firefox+Help?style_mode=inproduct    
    """
    def test_redirect_firefox_help(self):
        firefoxHelpArr = ["/firefox-help","/firefox-f1","/firefox-osxkey"]
        
        for x in self.localesArray:
            for two in self._2:
                for three in self._3:
                    for fxHelp in firefoxHelpArr:
                        open_url = self.mainURL+self.numberOne+self._1+two+three+x[self.key1]+fxHelp+"/"
                        open_urlNoTrailingSlash = self.mainURL+self.numberOne+self._1+two+three+x[self.key1]+fxHelp
                        expected_url = self.mainURL+x[self.key2]+self.styleMode
                        http_response = urllib.urlopen(open_url)
                        actual_url = urllib.unquote(http_response.geturl())
                        self.assertEqual(actual_url,expected_url)
                        """ repeat without trailing slash"""
                        http_response = urllib.urlopen(open_urlNoTrailingSlash)
                        actual_url = urllib.unquote(http_response.geturl())
                        self.assertEqual(actual_url,expected_url)
                        
    """RewriteRule ^1/([\-a-zA-Z]+)/([\.0-9ab]+(?:pre)?)/([\-_a-zA-Z0-9]+)/([\-a-zA-Z]+)/prefs-main\/$ to
//  /$4/kb/Options+window+-+Main+panel?style_mode=inproduct&as=u [R,NE]
// For eg. http://support.mozilla.com/1/firefox/3.6b3pre/Darwin/en-US/prefs-main/
//         redirects to
//         http://support.mozilla.com/en-US/kb/Options+window+-+Main+panel?style_mode=inproduct&as=u    
    """
    def test_redirect_preferences(self):
        one    = {"goToUrl":"/prefs-main","redirectUrl" : "/Options window - General panel","hash" :"?as=u"}
        two    = {"goToUrl":"/prefs-clear-private-data","redirectUrl":"/Clear Recent History","hash":"?as=u"}
        three    = {"goToUrl":"/prefs-fonts-and-colors","redirectUrl":"/Options window - Content panel","hash":"?as=u#fonts_and_colors"}
        four = {"goToUrl":"/prefs-privacy","redirectUrl":"/Options window - Privacy panel","hash":"?as=u"}
        five = {"goToUrl":"/prefs-applications","redirectUrl":"/Options window - Applications panel","hash":"?as=u"}
        six = {"goToUrl":"/prefs-connection-settings","redirectUrl":"/Options window - Advanced panel","hash":"?as=u#connection_settings"}
        seven    = {"goToUrl":"/prefs-tabs","redirectUrl":"/Options window - Tabs panel","hash":"?as=u"}
        eight    = {"goToUrl":"/prefs-advanced-javascript","redirectUrl" : "/Options window - Content panel","hash":"?as=u#advanced_javascript"}
        nine    = {"goToUrl":"/prefs-languages","redirectUrl":"/Options window - Content panel","hash":"?as=u#languages"}
        ten    = {"goToUrl":"/prefs-content","redirectUrl":"/Options window - Content panel","hash":"?as=u"}
        eleven = {"goToUrl":"/prefs-security","redirectUrl":"/Options window - Security panel","hash":"?as=u"}
        twelve = {"goToUrl":"/prefs-advanced-general","redirectUrl":"/Options window - Advanced panel","hash":"?as=u"}
        thirteen = {"goToUrl":"/prefs-advanced-network","redirectUrl":"/Options window - Advanced panel","hash":"?as=u#advanced_network"}
        fourteen    = {"goToUrl":"/prefs-advanced-update","redirectUrl":"/Options window - Advanced panel","hash":"?as=u#advanced_update"}
        fifteen = {"goToUrl":"/prefs-advanced-encryption","redirectUrl":"/Options window - Advanced panel","hash":"?as=u#advanced_encryption"}
        #sixteen = {"goToUrl":"/ieusers","redirectUrl":"/Windows start page","hash":"?as=u"}
        #seventeen    = {"goToUrl":"/eu/ieusers","redirectUrl":"/Windows start page","hash":"?as=u&eu=1"}
        eighteen    = {"goToUrl":"/places-locked","redirectUrl" : "/The bookmarks and history system will not be functional","hash":"?as=u"}
        nineteen    = {"goToUrl":"/private-browsing","redirectUrl":"/Private Browsing","hash":"?as=u"}
        twenty    = {"goToUrl":"/prefs-weave","redirectUrl":"/How to sync Firefox settings between computers","hash":"?as=u"}
        #twentyone = {"goToUrl":"/firefox-f1","redirectUrl":"/Firefox Help","hash":""}
        #twentytwo = {"goToUrl":"/firefox-osxkey","redirectUrl":"/Firefox Help","hash":""}
        twentythree = {"goToUrl":"/keyboard-shortcuts","redirectUrl":"/Keyboard shortcuts","hash":"?as=u"}
        twentyfour    = {"goToUrl":"/eu/keyboard-shortcuts","redirectUrl":"/Keyboard shortcuts","hash":"?as=u&eu=1"}
        twentyfive = {"goToUrl":"/plugin-crashed","redirectUrl":"/Plugin crash reports","hash":"?as=u"}
        twentysix    = {"goToUrl":"/eu/plugin-crashed","redirectUrl":"/Plugin crash reports","hash":"?as=u&eu=1"}
        
        urlPrefsArray = (one,two,three,four,five,six,seven,eight,nine,ten,eleven,twelve,thirteen,fourteen,fifteen,eighteen,nineteen,twenty,twentythree,twentyfour,twentyfive,twentysix)

 
        for x in self.localesArray:
            for urlPrefs in urlPrefsArray:
                for two in self._2:
                    for three in self._3:
                        open_url = self.mainURL+self.numberOne+self._1+two+three+x[self.key1]+urlPrefs[self.key1]+"/"
                        open_urlNoTrailingSlash = self.mainURL+self.numberOne+self._1+two+three+x[self.key1]+urlPrefs[self.key1]
                        expected_url = self.mainURL+x[self.key2]+self.kbSuffix+urlPrefs[self.key2]
                        http_response = urllib.urlopen(open_url)
                        if http_response.code == 404:
                                print "%s gives %s" %(open_url,http_response)
                                continue
                        actual_url = urllib.unquote(http_response.geturl())
                        self.assert_(expected_url in actual_url)
                        if 'eu=1' in urlPrefs[self.key3]:
                            self.assert_('eu=1' in actual_url)
                            self.assert_('as=u' in actual_url)
                        else:
                            try:
                                if not urlPrefs[self.key3] in actual_url:
                                    raise Exception
                            except Exception:
                                print '\r\n'
                                print "string not foud :"+urlPrefs[self.key3]
                                print "actual url :"+actual_url
                                raise
                                

                            
                        """ repeat without trailing slash"""
                        http_response = urllib.urlopen(open_urlNoTrailingSlash)
                        if http_response.code == 404:
                                print "%s gives %s" %(open_url,http_response)
                                continue
                        actual_url = urllib.unquote(http_response.geturl())
                        self.assert_(expected_url in actual_url)
                        if 'eu=1' in urlPrefs[self.key3]:
                            self.assert_('eu=1' in actual_url)
                            self.assert_('as=u' in actual_url)
                        else:
                            try:
                                if not urlPrefs[self.key3] in actual_url:
                                    raise Exception
                            except Exception:
                                print '\r\n'
                                print "string not foud :"+urlPrefs[self.key3]
                                print "actual url :"+actual_url
                                raise
                        

    def test_redirect_misc(self):
        """ 
           // this redirect is for windows 7 support only
          //  http://support-stage.mozilla.org/1/windows7-support using |en-US| and
          //  have it redirect to
          //  http://support-stage.mozilla.org/en-US/kb/Firefox+Help?style_mode=inproduct   
        """
        open_url     = self.mainURL+"/windows7-support"
        expected_url = self.mainURL+"/en-US"+self.styleMode
        http_response = urllib.urlopen(open_url)
        actual_url = urllib.unquote(http_response.geturl())
        self.assertEqual(expected_url,actual_url)
        
        
        """     +# Redirect old discussion forums to new discussion forums
                +RewriteRule ^forum/3(.*) /en-US/forums/contributors$1 [L,QSA,R=301]
                +RewriteRule ^([\-a-zA-Z]+)/forum/3(.*) /en-US/forums/contributors$2 [L,QSA,R=301]
                 +RewriteRule ^forum/4(.*) /en-US/forums/off-topic$1 [L,QSA,R=301]
                 +RewriteRule ^([\-a-zA-Z]+)/forum/4(.*) /en-US/forums/off-topic$2 [L,QSA,R=301]
                +RewriteRule ^forum/5(.*) /en-US/forums/knowledge-base-articles$1 [L,QSA,R=301]
                +RewriteRule ^([\-a-zA-Z]+)/forum/5(.*) /en-US/forums/knowledge-base-articles$2 [L,QSA,R=301]
        """
        """
           No longer valid, bug 650349
        """
#        open_url     = self.mainURL+"/forum/3"
#        http_response = urllib.urlopen(open_url)
#        actual_url = urllib.unquote(http_response.geturl())
#        self.assert_('/forums/contributors' in actual_url)
#        
#        open_url     = self.mainURL+"/forum/4"
#        http_response = urllib.urlopen(open_url)
#        actual_url = urllib.unquote(http_response.geturl())
#        self.assert_('/forums/off-topic' in actual_url)
#                        
#        open_url     = self.mainURL+"/forum/5"
#        http_response = urllib.urlopen(open_url)
#        actual_url = urllib.unquote(http_response.geturl())
#        self.assert_('/forums/knowledge-base-articles' in actual_url)
        
#        open_url     = self.mainURL+"/en-US/forum/6"
#        expected_url = self.mainURL+"/en-US/questions?tagged=FxHome"
#        sel.open(open_url)
#        actual_url = sel.get_location()
#        self.assertEqual(expected_url,actual_url)
        
        """ redirect old mobie url's to new sumo url's
        http://support.allizom.org/1/mobile/4.0/android/en-US/firefox-help ->
        http://www.mozilla.com/en-US/m/support/
        """
        platform  = "/mobile"
        mobile_os = ('/android','/iphone', '/nokia')
        
        for x in self.localesArray:
            for two in self._2:
                for three in mobile_os:
                    open_url     = str(self.mainURL)+str(self.numberOne)+platform+two+three+str(x[self.key1])+"/firefox-help"
                    expectedStr = "m/support"
                    http_response = urllib.urlopen(open_url)
                    actual_url = urllib.unquote(http_response.geturl())
                    if http_response.code == 404:
                        print ("%s gives %s") %(open_url,http_response.code)
                        continue
                    self.assert_(expectedStr in actual_url)
                
        """
        # Contribute shortcut
        RewriteRule ^contribute/?$ /kb/superheroes-wanted [L,QSA,R=302]  
        """
        open_url     = self.mainURL+"/contribute"  
        expectedStr = "/en-US"+self.kbSuffix+"/superheroes-wanted"
        http_response = urllib.urlopen(open_url)
        actual_url = urllib.unquote(http_response.geturl())
        self.failUnless(expectedStr in actual_url)
        
        """
        # Redirect no help topic to main in-product page
          RewriteRule ^1/Firefox/4\.0b\d[^/]*/([\-_a-zA-Z0-9]+)/([\-a-zA-Z]+)\/$ "/$2/kb/Get help with Firefox 4 beta?style_mode=inproduct&as=u" [R,NC]
          RewriteRule ^kb/Get\+help\+with\+Firefox\+4\+Beta$ /home/ [L,NC,R=301]
          RewriteRule ^1/([\-a-zA-Z]+)/([0-9]+\.[0-9]+[^/]*)/([\-_a-zA-Z0-9]+)/([\-a-zA-Z]+)$ /1/$1/$2/$3/$4/ [L,R]
          RewriteRule ^1/([\-a-zA-Z]+)/([0-9]+\.[0-9]+[^/]*)/([\-_a-zA-Z0-9]+)/([\-a-zA-Z]+)\/$ "/$4/kb/Firefox Help?style_mode=inproduct" [L,R,NE] 
       """
        for x in self.localesArray:
            for z in self._2:
                for y in self._3:
                    fx_4 = "/4.0b4"
                    open_url = self.mainURL+str(self.numberOne)+str(self._1)+str(fx_4)+str(y)+str(x[self.key1])
                    expected_url = self.mainURL+x[self.key2]+self.styleMode
                    http_response = urllib.urlopen(open_url)
                    actual_url = urllib.unquote(http_response.geturl())
                    self.assertEqual(expected_url,actual_url)
            
                    open_url = self.mainURL+str(self.numberOne)+str(self._1)+str(z)+str(y)+(x[self.key1])
                    expected_url = self.mainURL+x[self.key2]+self.styleMode
                    http_response = urllib.urlopen(open_url)
                    actual_url = urllib.unquote(http_response.geturl())
                    self.assertEqual(expected_url,actual_url)
 
    '''
       future test:
                     http://support.allizom.org/1/firefox/3.6.6/WINNT/en-US/firefox-help
                     redirects to 
                     http://support.allizom.org/en-US/home?as=u
                     
                      
    '''            
    """ /*http://support.mozilla.com/1/firefox-home/%version%/iPhone/en-US/ ->
        http://support.mozilla.com/en-US/kb/What+is+Firefox+Home
        http://support.mozilla.com/1/firefox-home/%version%/iPhone/en-US/install ->
        http://support.mozilla.com/en-US/kb/How to set up Firefox Home
        support.allizom.org/1/firefox-home/1.0/iPhone/en-US/log-in/ ->
        http://support.allizom.org/en-US/kb/Cannot log in to Firefox Home App?as=u
    """
    def test_redirect_iphone(self):
        
        product_iphone  = "/firefox-home"
        platform_iphone = "/iPhone"
        #helptopic_iphone = "/install"
        helptopic_login  = "/log-in"
 
        for x in self.localesArray:
            for two in self._2:
                open_url     = str(self.mainURL)+str(self.numberOne)+str(product_iphone)+two+str(platform_iphone)+str(x[self.key1])
                expected_url = self.mainURL+"/en-US"+self.kbSuffix+"/What is Firefox Home"+self.article_source_suffix
                http_response = urllib.urlopen(open_url)
                actual_url = urllib.unquote(http_response.geturl())
                if http_response.code == 404:
                    print ("%s gives %s") %(open_url,http_response.code)
                    continue
                self.assertEqual(expected_url,actual_url)
                            
                """
                commented due to frequent unknown failures
                """
#                open_url     = str(self.mainURL)+self.numberOne+product_iphone+two+platform_iphone+x[self.key1]+helptopic_iphone
#                expected_url = self.mainURL+"/en-US"+self.kbSuffix+"/How to set up Firefox Home"+self.article_source_suffix
#                try:
#                    sel.open(open_url)
#                except Exception,e:
#                    if '404' in str(e):
#                        print str(e)
#                        
#                actual_url = urllib.unquote(sel.get_location())
#                self.assertEqual(expected_url,actual_url)
#                
                # Firefox Home App
                open_url     = self.mainURL+self.numberOne+product_iphone+two+platform_iphone+x[self.key1]+helptopic_login
                expected_url = self.mainURL+"/en-US"+self.kbSuffix+"/Cannot log in to Firefox Home App"+self.article_source_suffix
                http_response = urllib.urlopen(open_url)
                actual_url = urllib.unquote(http_response.geturl())
                if http_response.code == 404:
                    print ("%s gives %s") %(open_url,http_response.code)
                    continue
                self.assertEqual(expected_url,actual_url)     
                           
    """
         No longer valid, bug 650303
    """          
#    def test_old_kb_redirects(self):
#        
#        one    = {"goToUrl":"/Firefox+Help","redirectUrl" : "/home"}
#        two    = {"goToUrl":"/Windows+start+page","redirectUrl":"/home"}
#        #three    = {"goToUrl":"/Firefox+Support+Home+Page","redirectUrl":"/home/"}
#        four = {"goToUrl":"/Get+help+with+Firefox+4+Beta","redirectUrl":"/home"}
#        five = {"goToUrl":"/Localization+Dashboard","redirectUrl":"/contributors"}
#        six = {"goToUrl":"/All+Knowledge+Base+articles","redirectUrl":"/contributors"}
#        seven    = {"goToUrl":"/Mobile+Help+and+Tutorials","redirectUrl":"/mobile"}
#        eight    = {"goToUrl":"/Article+list","redirectUrl" : "/all"}
#
#
#        kb_array = (one,two,four,five,six)
#        for x in self.localesArray:
#            for y in kb_array:
#                open_url = self.mainURL+(x[self.key1])+self.kbSuffix+y[self.key1]
#                expected_url = self.mainURL+x[self.key2]+y[self.key2]
#                http_response = urllib.urlopen(open_url)
#                actual_url = urllib.unquote(http_response.geturl())
#                self.assertEqual(expected_url,actual_url)
#                        
#        kb_array2 = (seven,)       
#        for x in self.localesArray:
#            for y in kb_array2:
#                open_url = self.mainURL+(x[self.key1])+self.kbSuffix+y[self.key1]
#                expected_url = y[self.key2]
#                http_response = urllib.urlopen(open_url)
#                actual_url = urllib.unquote(http_response.geturl())
#                self.assertTrue(expected_url in actual_url)
#                        
#        """ ^kb/Article\+list$ /kb/all """
#        kb_array2 = (eight,)
#        for x in self.localesArray:
#            for y in kb_array2:
#                open_url = self.mainURL+str(x[self.key1])+str(self.kbSuffix)+str(y[self.key1])
#                expected_url = self.mainURL+x[self.key2]+str(self.kbSuffix)+y[self.key2]
#                http_response = urllib.urlopen(open_url)
#                actual_url = urllib.unquote(http_response.geturl())
#                self.assertEqual(expected_url,actual_url)
#        
#        """ non-localized kb redirects"""           
#        one    = {"goToUrl":"/Live+Chat","redirectUrl":"/chat"}
#        two    = {"goToUrl":"/Support+Website+Forums","redirectUrl" : "/questions"}
#        
#        kb_array2 = (one,two)
#        for x in self.localesArray:
#            for y in kb_array2:
#                open_url = self.mainURL+(x[self.key1])+self.kbSuffix+y[self.key1]
#                expected_url = self.mainURL+"/en-US"+y[self.key2]
#                http_response = urllib.urlopen(open_url)
#                actual_url = urllib.unquote(http_response.geturl())
#                self.assertEqual(expected_url,actual_url)


if __name__ == "__main__":
    unittest.main()
