from selenium import selenium
import vars
import unittest
import sumo_functions


class locale_redirect(unittest.TestCase):

    def setUp(self):
        self.selenium = selenium(
        vars.ConnectionParameters.server,
        vars.ConnectionParameters.port,
        vars.ConnectionParameters.browser,
        vars.ConnectionParameters.baseurl)
        self.selenium.start()
        self.selenium.set_timeout(vars.ConnectionParameters.page_load_timeout)

    def test_locale_redirect(self):
        sel = self.selenium
        sumo_func = sumo_functions.SUMOfunctions()
        locales = ["sq", "ar", "as", "ast", "eu", "bn-BD", "bn-IN", "bs",
            "pt-BR", "bg", "ca", "hr", "da", "eo", "et", "fi", "fr", "fy-NL",
            "fur", "gl", "el", "gu-IN", "he", "hi-IN", "hu", "is", "ilo",
            "id", "ga-IE", "kn", "kk", "rw", "lt", "mk", "ms", "mr", "mn",
            "no", "oc", "pa-IN", "pl", "pt-PT", "ro", "rm", "gd",
            "sr-CYRL", "zh-CN", "si", "sk", "sv-SE", "ta-LK", "te", "th",
            "zh-TW", "vi"]
        for locale in locales:
            #print locale
            if "-" in locale:
                #check existing locales don't redirect
                sumo_func.open(sel, "/" + locale)
                self.failUnless("/" + locale in sel.get_location(),
                    "%s not in %s" % (locale, sel.get_location()))
            else:
                #check redirect for existing xy when xy-ZW does not exist
                sumo_func.open(sel, "/" + locale + "-AA")
                self.failUnless("/" + locale + "/" in sel.get_location(),
                    "%s not in %s" % (locale, sel.get_location()))
        #check if nonexistant locales redirect to en-US

    def tearDown(self):
        self.selenium.stop()

if __name__ == "__main__":
    unittest.main()
