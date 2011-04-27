from selenium import selenium
import vars
import unittest
import sumo_functions
from SUMO_breadcrumbs import *

class breadcrumbs_htc(unittest.TestCase):
    def setUp(self):
        self.selenium = selenium(
        vars.ConnectionParameters.server,
        vars.ConnectionParameters.port,
        vars.ConnectionParameters.browser,
        vars.ConnectionParameters.baseurl)
        self.selenium.start()
        self.selenium.set_timeout(vars.ConnectionParameters.page_load_timeout)
    
    def test_breadcrumbs_htc(self):
        sel = self.selenium
        sumo_func = sumo_functions.SUMOfunctions()

        # Objective: verify breadcrumbs at the top of 'How to Contribute' knowledge base articles.
        # Verifies breadcrumbs' text and URL
        # Verifies after opening on article by links from article list, or directly by URL
        # article link locators found in the array HTC_breadcrumbs.
        # Error messages for breadcrumbs are prefixed with *****
        # Does not check breadcrumbs on How To Contribute home page

        sumo_func.open(sel, "/en-US/kb/How+to+contribute")
        # Prefix for all breadcrumb elements
        bcPrefix = "//div[@id='breadcrumbs']/ul/"
        # Locators for dividers between breadcrumbs
        divider1 = "li[2][contains(@class,'divider')][contains(text(),'/')]"
        divider2 = "li[4][contains(@class,'divider')][contains(text(),'/')]"

        # Locators for recurring breadcrumbs.  Appear before the article title crumb.
        FirefoxSupport1 = "li[1]/a[contains(@href,'/kb/')][contains(text(),'Firefox Support')]"
        HowToContribute2 = "li[3]/span/a[contains(@href,'/kb/How+to+contribute')][starts-with(text(),'How')][contains(text(),'Contribute')]"

        # get the article count from HTC breadcrumb array
        articleCount = len(HTC_breadcrumbs)
        print("Count for HTC articles is " + str(articleCount) + ".")

        idx2 = 0
        # While #2 indexes into the next article
        # sel.while("${idx2} < ${articleCount}")
        while idx2 < articleCount:
            parent_URL_Ending = HTC_breadcrumbs[idx2].parentUrlEnding
            article_URL_Ending = HTC_breadcrumbs[idx2].articleUrlEnding

            idx3 = 1
            # While #3 launches a page in different ways  (clicking on link or loading page by URL) and verifies breadcrumbs
            # sel.while("${idx3} <= 2")
            while idx3 <= 2:

                # sel.goto_if("( ${idx3} == 1 )", "pageByLink")
                # sel.goto_if("( ${idx3} == 2 )", "pageByUrl")

                if idx3 == 1:
                    # Launch by link
                    # sel.label("pageByLink")
                    # launch the parent page containing the article link
                    pageURL = "en-US/kb/" + parent_URL_Ending
                    sumo_func.open(sel, pageURL)
                    # click on the article 
                    articleLocator = sel.get_eval("//a[contains(@href,'" + article_URL_Ending + "')]")
                    # check that the link is present on page.  exit iteration if not.
                    linkPresent = sel.is_element_present(articleLocator)
                    # sel.goto_if("( ${linkPresent} == true )", "linkIsPresent")
                    if linkPresent != 1:
                        errorMsg = "Link not found: " + articleLocator
                        break;
                    # sel.goto("echoErrorMsg")

                    # sel.label("linkIsPresent")
                    sel.click(articleLocator)
                    sel.wait_for_page_to_load(vars.ConnectionParameters.page_load_timeout)
                    # save the article URL for launching in the next iteration
                    articleUrl = sel.get_location()
                    # save the article title for the last breadcrumb
                    articleTitle = sel.get_text("//div[@class='titleetc']/h1")
                    #print("Article header from page: " + articleTitle)
                    # sel.goto("verifyBreadcrumbs")

                if idx3 == 2:
                    # Launch page by URL
                    # sel.label("pageByUrl")
                    sumo_func.open(sel, articleUrl)

                # Verify the breadcrumbs.
                # errors are gathered and reported in one statement at the  bottom of the loop
                # sel.label("verifyBreadcrumbs")

                errorMsg = ""
                elementPresent = sel.is_element_present(bcPrefix + FirefoxSupport1)
                if elementPresent != 1:
                    errorMsg = errorMsg + "  Crumb 1 is not Firefox Support."

                #errorMsg = sel.get_eval("if ( " + str(elementPresent) + " != true ) {  " + errorMsg + "  Crumb 1 is not Firefox Support. } else { " + errorMsg + " }")

                elementPresent = sel.is_element_present(bcPrefix + divider1)
                if elementPresent != 1:
                    errorMsg = errorMsg + "  Divider 1 is not present."
                #errorMsg = sel.get_eval("if ( " + str(elementPresent) + " != true ) {  " + errorMsg + "  Divider 1 is not present. } else { " + errorMsg + " }")

                elementPresent = sel.is_element_present(bcPrefix + KnowledgeBase2)
                if elementPresent != 1:
                    errorMsg = errorMsg + "  Crumb 2 is not Knowledge Base."
                #errorMsg = sel.get_eval("if ( " + str(elementPresent) + " != true ) {  " + errorMsg + " Crumb 2 is not How to Contribute. } else { " + errorMsg + " }")

                elementPresent = sel.is_element_present(bcPrefix + divider2)
                if elementPresent != 1: 
                    errorMsg = errorMsg + "  Divider 2 is not present."
                #errorMsg = sel.get_eval("if ( " + str(elementPresent) + " != true ) {  " + errorMsg + "  Divider 2 is not present. } else { " + errorMsg + " }")

                # Crumb 3 - the article title
                elementPresent = sel.is_element_present(bcPrefix + "li[5]")
                # this breadcrumb text can be long since it's a user created title
                # compare the link and breadcrumb text as additional check.  using long strings with the starts-with( ) and contains( ) functions return True when they should return False.
                elementText = sel.get_text(bcPrefix + "li[5]")
                #pos = elementText'].indexOf(storedVars['articleTitle'])")
                #errorMsg = sel.get_eval("if ( " + elementPresent + " != true || (" + pos + "<0)  ) {  " + errorMsg + " Crumb 4 is not article title. } else { " + errorMsg + " }")
                if elementPresent != 1 or elementText != articleTitle:
                    errorMsg = errorMsg + "  Crumb 4 is not article title."
                
                # Test there is NOT an 6th item in the breadcrumb list
                elementPresent = sel.is_element_present(bcPrefix + "li[6]")
                if elementPresent == 1:
                            errorMsg = errorMsg + "  Unexpected item after crumb 4."
                #errorMsg = sel.get_eval("if ( " + elementPresent + " == true ) {  " + errorMsg + " Unexpected item after crumb 4. } else { " + errorMsg + " }")

                # Display a messagge if there were errors
                # ( to temporarily force an error msg: a) append non-existent attribute to item locator(s), such as [contains(text(),"zzz")]  , b) for non-existent 8th item change locator to an existing item )
                # sel.label("echoErrorMsg")
                # sel.goto_if("( ${errorMsg} ==  )", "goBackPage")
                # sel.goto_if("( ${idx3} == 1 )", "errorForLink")
                # sel.goto_if("( ${idx3} == 2 )", "errorForUrl")

                # sel.label("errorForLink")
                if idx3 == 1 and errorMsg != "":
                    print("***** link with URL containing " + article_URL_Ending + " launched from page with URL ending " + parent_URL_Ending + " has errors: " + errorMsg)
                # sel.goto("goBackPage")

                if idx3 == 2 and errorMsg != "":
                # sel.label("errorForUrl")
                    print("***** article with URL " + articleUrl + " launched directly by URL has errors: " + errorMsg)

                # sel.label("goBackPage")
                # return to the forum home page
                sel.go_back()
                sel.wait_for_page_to_load(vars.ConnectionParameters.page_load_timeout)

                # While #3 launches a page in different ways (clicking on link or loading page by URL)
                idx3 = idx3 + 1
            # sel.end_while()

            # While #2 indexes into the next article in the list
            idx2 = idx2 + 1
        # sel.end_while()

        print("DONE")
    
    def tearDown(self):
        self.selenium.stop()

if __name__ == "__main__":
    unittest.main()
