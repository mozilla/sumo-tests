from selenium import selenium
import vars
import unittest
import sumo_functions, sys
from SUMO_breadcrumbs import *
#import operator

class breadcrumbs_KB(unittest.TestCase):
    def setUp(self):
        self.selenium = selenium(
        vars.ConnectionParameters.server,
        vars.ConnectionParameters.port,
        vars.ConnectionParameters.browser,
        vars.ConnectionParameters.baseurl)
        self.selenium.start()
        self.selenium.set_timeout(vars.ConnectionParameters.page_load_timeout)
        
   
        
    def test_breadcrumbs_kb(self):
        sel = self.selenium
        sumo_func = sumo_functions.SUMOfunctions()

        # Objective: verify breadcrumbs at the top of knowledge base articles.
        # Verifies breadcrumbs' text and URL
        # Verifies after opening on article by links from article list, or directly by URL
        # Checks 3 lists of articles:
        # -- the Forum home page New to Firefox , and Popular Support Articles, 
        # -- All Knowledge Base Forum Topics page
        # Error messages for breadcrumbs are prefixed with *****
        # Does not check breadcrumbs on forum home pages

        # Prefix for all breadcrumb elements
        bcPrefix = "//div[@id='breadcrumbs']/ul/"

        # Locators for dividers between breadcrumbs
        divider1 = "li[2][contains(@class,'divider')][contains(text(),'/')]"
        divider2 = "li[4][contains(@class,'divider')][contains(text(),'/')]"

        # Locators for recurring breadcrumbs.  Appear before the article title crumb.
        FirefoxSupport1 = "li[1]/a[contains(@href,'/kb/')][contains(text(),'Firefox Support')]"
        KnowledgeBase2 = "li[3]/span/a[contains(@href,'/kb/Article+list')][starts-with(text(),'Knowledge')][contains(text(),'Base')]"

        idx1 = 1
       
        # While #1 sets selectors & variables for the next forum article list.
        # sel.while("( ${idx1} <= 3 )")
        while idx1 <= 3:
            # sel.goto_if("( ${idx1} == 1 )", "NewToFirefox")
            # sel.goto_if("( ${idx1} == 2 )", "PopularArticles")
            # sel.goto_if("( ${idx1} == 3 )", "AllArticles")

            # Variables set:
            # listLocator - front part of locator for the list of articles.  Everything before the article# index
            # itemSuffix - end of locator that follows the article# index
            # articleIndexOffset - offset in a list/table to the first article.  0 for lists, 1 for tables with a header row.
            # titleTruncate - trailer that needs to be truncated from titles in the article list.  for example: long titles are shortened in the article list and end with "..."
            # listDescription - Friendly name of the forum and list.  used in error message.

            # sel.label("NewToFirefox")
            if idx1 == 1:
                sumo_func.open(sel, "/en-US/kb")
                listLocator = "//div[@id='promotebox-list']/ul/li"
                articleLocatorSuffix = "/a"
                articleIndexOffset = 0
                titleTruncate = ""
                listDescription = "Knowledge Base home page, New to Firefox"
                # sel.goto("processList")

            # sel.label("PopularArticles")
            if idx1 == 2:
                sumo_func.open(sel, "/en-US/kb")
                listLocator = "//div[@id='mostpopular-new']/ul/li"
                articleLocatorSuffix = "/a"
                articleIndexOffset = 0
                titleTruncate = ""
                listDescription = "Knowledge Base home page, Most Popular"
                # sel.goto("processList")

            # sel.label("AllArticles")
            if idx1 == 3:
                sumo_func.open(sel, "/en-US/kb/Article+list")
                listLocator = "//div[@class='pagelist-wrapper']/ol/li"
                articleLocatorSuffix = "/a"
                articleIndexOffset = 0
                titleTruncate = ""
                listDescription ="All KB Articles"
                # sel.goto("processList")

            # sel.label("processList")
            # get the item count from the list or table that contains the articles
            linkCount = sel.get_xpath_count(listLocator)
            print "Item count for " + listDescription + " is " + str(linkCount) + ".  Index offset to articles is " + str(articleIndexOffset) + "."

            idx2 = articleIndexOffset+1
            # While #2 indexes into the next article
            # sel.while("${idx2} <= ${linkCount}")
            while idx2 <= int(linkCount):
                idx3 = 1
                # While #3 launches a page in different ways  (clicking on link or loading page by URL) and verifies breadcrumbs
                # sel.while("${idx3} <= 2")
                while idx3 <= 2: 
                    # sel.goto_if("( ${idx3} == 1 )", "pageByLink")
                    # sel.goto_if("( ${idx3} == 2 )", "pageByUrl")

                    # Launch page by clicking on links.
                    # sel.label("pageByLink")
                    if idx3 == 1:
                        launchDescription = "launched by link"
                        # save the article's title
                        #print listLocator + "[" + str(idx2) + "]" + articleLocatorSuffix
                        articleTitle = sel.get_text(listLocator + "[" + str(idx2) + "]" + articleLocatorSuffix)
                        # remove text that's appended to the title for article list
                        # sel.goto_if("( ${titleTruncate} ==  )", "titleIsSet")
                        if titleTruncate != "":
                            truncIdx = sel.get_eval("articleTitle.lastIndexOf('" + titleTruncate + "')")
                            # sel.goto_if("( ${truncIdx} < 0 )", "titleIsSet")
                            if truncIdx >= 0:
                                # remove the 'titleTruncate' string from the end of the article title
                                articleTitle = sel.get_eval("articleTitle.substr(0," + truncIdx + ")")
                        # sel.label("titleIsSet")
                        #print("Article title from link: " + articleTitle)
                        # launch the article's page
                        sel.click(listLocator + "[" + str(idx2) + "]" + articleLocatorSuffix)
                        sel.wait_for_page_to_load(vars.ConnectionParameters.page_load_timeout)
                        # save the article URL for launching in the next iteration
                        articleUrl = sel.get_location()
                        # sel.goto("verifyBreadcrumbs")
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
                        #errorMsg = sel.get_eval("if ( " + str(elementPresent) + " != true ) {  " + errorMsg + " Crumb 2 is not Knowledge Base. } else { " + errorMsg + " }")

                        elementPresent = sel.is_element_present(bcPrefix + divider2)
                        if elementPresent != 1: 
                            errorMsg = errorMsg + "  Divider 2 is not present."
                        #errorMsg = sel.get_eval("if ( " + str(elementPresent) + " != true ) {  " + errorMsg + "  Divider 2 is not present. } else { " + errorMsg + " }")

                        # Crumb 3 - the article title
                        elementPresent = sel.is_element_present(bcPrefix + "li[5]")
                        # this breadcrumb text can be long since it's a user created title
                        # compare the link and breadcrumb text as additional check.  using long strings with the starts-with( ) and contains( ) functions return True when they should return False.
                        elementText = sel.get_text(bcPrefix + "li[5]")
                        #pos = operator.indexOf(elementText, articleTitle)
                        if elementPresent != 1 or elementText != articleTitle:
                            errorMsg = errorMsg + "  Crumb 4 is not article title."
                        #errorMsg = sel.get_eval("if ( " + elementPresent + " != true || (" + pos + "<0)  ) {  " + errorMsg + " Crumb 4 is not article title. } else { " + errorMsg + " }")

                        # Test there is NOT an 6th item in the breadcrumb list
                        elementPresent = sel.is_element_present(bcPrefix + "li[6]")
                        if elementPresent == 1:
                            errorMsg = errorMsg + "  Unexpected item after crumb 4."
                        #errorMsg = sel.get_eval("if ( " + elementPresent + " == true ) {  " + errorMsg + " Unexpected item after crumb 4. } else { " + errorMsg + " }")

                        # Display a messagge if there were errors
                        # ( to temporarily force an error msg: a) append non-existent attribute to item locator(s), such as [contains(text(),"zzz")]  , b) for non-existent 8th item change locator to an existing item )
                        # sel.goto_if("( ${errorMsg} ==  )", "goBackPage")
                        if errorMsg != "":
                            articleNumber = int(idx2) - int(articleIndexOffset)
                            print("***** " + listDescription + " has errors at article #" + articleNumber + " when " + launchDescription + ": " + errorMsg)

                        # sel.label("goBackPage")
                        # return to the forum home page
                        sel.go_back()
                        sel.wait_for_page_to_load(vars.ConnectionParameters.page_load_timeout)
                    if idx3 == 2:
                        # Launch page by URL
                        # sel.label("pageByUrl")
                        launchDescription = "launched by URL"
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
                        #errorMsg = sel.get_eval("if ( " + str(elementPresent) + " != true ) {  " + errorMsg + " Crumb 2 is not Knowledge Base. } else { " + errorMsg + " }")

                        elementPresent = sel.is_element_present(bcPrefix + divider2)
                        if elementPresent != 1: 
                            errorMsg = errorMsg + "  Divider 2 is not present."
                        #errorMsg = sel.get_eval("if ( " + str(elementPresent) + " != true ) {  " + errorMsg + "  Divider 2 is not present. } else { " + errorMsg + " }")

                        # Crumb 3 - the article title
                        elementPresent = sel.is_element_present(bcPrefix + "li[5]")
                        # this breadcrumb text can be long since it's a user created title
                        # compare the link and breadcrumb text as additional check.  using long strings with the starts-with( ) and contains( ) functions return True when they should return False.
                        elementText = sel.get_text(bcPrefix + "li[5]")
                        #pos = operator.indexOf(elementText, articleTitle)
                        if elementPresent != 1 or elementText != articleTitle:
                            errorMsg = errorMsg + "  Crumb 4 is not article title."
                        #errorMsg = sel.get_eval("if ( " + elementPresent + " != true || (" + pos + "<0)  ) {  " + errorMsg + " Crumb 4 is not article title. } else { " + errorMsg + " }")

                        # Test there is NOT an 6th item in the breadcrumb list
                        elementPresent = sel.is_element_present(bcPrefix + "li[6]")
                        if elementPresent == 1:
                            errorMsg = errorMsg + "  Unexpected item after crumb 4."
                        #errorMsg = sel.get_eval("if ( " + elementPresent + " == true ) {  " + errorMsg + " Unexpected item after crumb 4. } else { " + errorMsg + " }")

                        # Display a messagge if there were errors
                        # ( to temporarily force an error msg: a) append non-existent attribute to item locator(s), such as [contains(text(),"zzz")]  , b) for non-existent 8th item change locator to an existing item )
                        # sel.goto_if("( ${errorMsg} ==  )", "goBackPage")
                        if errorMsg != "":
                            articleNumber = sel.get_eval(idx2 + " - " + articleIndexOffset)
                            print("***** " + listDescription + " has errors at article #" + articleNumber + " when " + launchDescription + ": " + errorMsg)

                        # sel.label("goBackPage")
                        # return to the forum home page
                        sel.go_back()
                        sel.wait_for_page_to_load(vars.ConnectionParameters.page_load_timeout)

                    # While #3 launches a page in different ways (clicking on link or loading page by URL)
                    idx3 = idx3+1
                    # sel.end_while()

                # While #2 indexes into the next article in the list
                idx2 = idx2+1
                # sel.end_while()

            # While #1 sets selectors & variables to process next forum article list.
            idx1 = idx1+1
            # sel.end_while()

        print("DONE")
    
    
    
    def tearDown(self):
        self.selenium.stop()

if __name__ == "__main__":
    unittest.main()
