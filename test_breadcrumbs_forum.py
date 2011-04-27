from selenium import selenium
import vars
import unittest
import sumo_functions

class breadcrumbs_forum(unittest.TestCase):
    def setUp(self):
        self.selenium = selenium(
        vars.ConnectionParameters.server,
        vars.ConnectionParameters.port,
        vars.ConnectionParameters.browser,
        vars.ConnectionParameters.baseurl)
        self.selenium.start()
        self.selenium.set_timeout(vars.ConnectionParameters.page_load_timeout)
    
    def test_breadcrumbs_forum(self):
        sel = self.selenium
        sumo_func = sumo_functions.SUMOfunctions()
        sumo_func.open(sel, vars.ConnectionParameters.authurl)

        sumo_func.open(sel, vars.ConnectionParameters.authurlssl)
        # Objective: verify breadcrumbs at the top of forum articles.
        # Verifies breadcrumbs' text and URL
        # Verifies after opening on article by links from article list, or directly by URL
        # Checks 5 lists of articles:
        # -- the Forum home page Most Popular Topics and Most Recently Answered, 
        # -- first page of All Forum Topics, Contributors Forum, Off Topic 
        # Logs out an existing login.  Article list format changes with login
        # Error messages for breadcrumbs are prefixed with *****
        # Does not check breadcrumbs on forum home pages

        logoutLink = "link=Log Out"
        
        # Logout if there is a log in
        logoutLinkPresent = sel.is_element_present(logoutLink)
        # sel.goto_if("${logoutLinkPresent} != true", "LoggedOut")
        if logoutLinkPresent == 1:
            sel.click(logoutLink)
            sel.wait_for_page_to_load(vars.ConnectionParameters.page_load_timeout)
        
        # Prefix for all breadcrumb elements
        bcPrefix = "//div[@id='breadcrumbs']/ul/"
        # Locators for dividers between breadcrumbs
        divider1 = "li[2][contains(@class,'divider')][contains(text(),'/')]"
        divider2 = "li[4][contains(@class,'divider')][contains(text(),'/')]"
        divider3 = "li[6][contains(@class,'divider')][contains(text(),'/')]"
        
        # Locators for recurring breadcrumbs.  Appear before the article title crumb.
        FirefoxSupport1 = "li[1]/a[contains(@href,'/kb/')][contains(text(),'Firefox Support')]"
        Forums2 = "li[3]/a[contains(@href,'/tiki-forums.php?locale=en-US')][contains(text(),'Forums')]"
        ForumsFirefox3 = "li[5]/a[contains(@href,'/en-US/forum/1')][contains(text(),'Firefox')]"
        Contributors3 = "li[5]/a[contains(@href,'/en-US/forum/3')][contains(text(),'Contributors')]"
        OffTopic3 = "li[5]/a[contains(@href,'/en-US/forum/4')][contains(text(),'Off Topic')]"
        
        idx1 = 3
        # While #1 sets selectors & variables for the next forum article list.
        # sel.while("( ${idx1} <= 5 )")
        while idx1 <= 5:
            
            # sel.goto_if("( ${idx1} == 1 )", "MostReadTopics")
            # sel.goto_if("( ${idx1} == 2 )", "LatestTopics")
            # sel.goto_if("( ${idx1} == 3 )", "AllArticles")
            # sel.goto_if("( ${idx1} == 4 )", "ContributorsForum")
            # sel.goto_if("( ${idx1} == 5 )", "OffTopic")
            
            # Variables set:
            # listLocator - front part of locator for the list/table of articles.  Everything before the article# index
            # itemSuffix - end of locator that follows the article# index
            # articleIndexOffset - offset in a list/table to the first article.  0 for lists, 1 for tables with a header row.
            # titleTruncate - trailer that needs to be truncated from titles in the article list.  for example: long titles are shortened in the article list and end with "..."
            # crumb3Locator - the locator of the third crumb, which is differs by forum.
            # crumb3Name - a friendly name for the third crumb.  used in the error message.
            # listDescription - Friendly name of the forum and list.  used in error message.
            
            '''if idx1 == 1:
                # sel.label("MostReadTopics")
                sumo_func.open(sel, "/en-US/kb/Support+Website+Forums")
                listLocator = "//div[@id='mod-forums_most_read_topics']/ul/li"
                articleLocatorSuffix = "/a"
                articleIndexOffset = 0
                titleTruncate = "..."
                crumb3Locator = str(ForumsFirefox3)
                crumb3Name = "Firefox (forums)"
                listDescription = "Forum home page, Most Popular Topics"
                # sel.goto("processList")
            
            if idx1 == 2:
                # sel.label("LatestTopics")
                sumo_func.open(sel, "/en-US/kb/Support+Website+Forums")
                listLocator = "//div[@id='mod-forums_last_topics']/ul/li"
                articleLocatorSuffix = "/a"
                articleIndexOffset = 0
                titleTruncate = "..."
                crumb3Locator = ForumsFirefox3
                crumb3Name = "Firefox (forums)"
                listDescription = "Forum home page, Most Recent Topics"
                # sel.goto("processList")
                '''
            
            if idx1 == 3:
                # sel.label("AllArticles")
                sumo_func.open(sel, "/en-US/forum/1")
                listLocator = "//table[@class='normal']/tbody/tr"
                articleLocatorSuffix = "/td[2]/table/tbody/tr/td/a"
                articleIndexOffset = 1
                titleTruncate = ""
                crumb3Locator = ForumsFirefox3
                crumb3Name = "Firefox (forums)"
                listDescription = "All Forum Articles"
                # sel.goto("processList")
            
            if idx1 == 4:
                # sel.label("ContributorsForum")
                sumo_func.open(sel, "/en-US/forum/3")
                listLocator = "//table[@class='normal']/tbody/tr"
                articleLocatorSuffix = "/td[2]/table/tbody/tr/td/a"
                articleIndexOffset = 1
                titleTruncate = ""
                crumb3Locator = Contributors3
                crumb3Name = "Contributors"
                listDescription = "Contributors Forum"
                # sel.goto("processList")
            
            if idx1 == 5:
                # sel.label("OffTopic")
                sumo_func.open(sel, "/en-US/forum/4")
                listLocator = "//table[@class='normal']/tbody/tr"
                articleLocatorSuffix = "/td[2]/table/tbody/tr/td/a"
                articleIndexOffset = 1
                titleTruncate = ""
                crumb3Locator = OffTopic3
                crumb3Name = "Off Topic"
                listDescription = "Off Topic board"
                # sel.goto("processList")
            
            # sel.label("processList")
            # get the item count from the list or table that contains the articles
            linkCount = sel.get_xpath_count(listLocator)
            print("Item count for " + str(listDescription) + " is " + str(linkCount) + ".  Index offset to articles is " + str(articleIndexOffset) + ".")
            
            idx2 = articleIndexOffset+1
            # While #2 indexes into the next article
            # sel.while("${idx2} <= ${linkCount}")

            
            while int(idx2) < int(linkCount):
                idx3 = 1
                # While #3 launches a page in different ways  (clicking on link or loading page by URL) and verifies breadcrumbs
                # sel.while("${idx3} <= 2")
                while idx3 <= 2:
                    # sel.goto_if("( ${idx3} == 1 )", "pageByLink")
                    # sel.goto_if("( ${idx3} == 2 )", "pageByUrl")
                    
                    if idx3 == 1:
                        # Launch page by clicking on links.
                        # sel.label("pageByLink")
                        launchDescription = "launched by link"
                        # save the article's title
                        articleTitle = sel.get_text(listLocator + "[" + str(idx2) + "]" + articleLocatorSuffix)
                        # remove text that's appended to the title for article list
                        # sel.goto_if("( ${titleTruncate} ==  )", "titleIsSet")
                        truncIdx = articleTitle.find(titleTruncate)
                        # sel.goto_if("( ${truncIdx} < 0 )", "titleIsSet")
                        # remove the 'titleTruncate' string from the end of the article title
                        #if truncIdx >= 0:
                            #articleTitle = articleTitle[0:truncIdx]
                        # sel.label("titleIsSet")
                        print("Article title from link: " + articleTitle)
                        # launch the article's page
                        sel.click(listLocator + "[" + str(idx2) + "]" + articleLocatorSuffix)
                        sel.wait_for_page_to_load(vars.ConnectionParameters.page_load_timeout)
                        # save the article URL for launching in the next iteration
                        articleUrl = sel.get_location()
                        # sel.goto("verifyBreadcrumbs")
                    
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
                        errorMsg += "  Crumb 1 is not Firefox Support."
                    
                    elementPresent = sel.is_element_present(bcPrefix + divider1)
                    if elementPresent != 1:
                        errorMsg += "  Divider 1 is not present."
                    
                    elementPresent = sel.is_element_present(bcPrefix + Forums2)
                    if elementPresent != 1:
                        errorMsg += "  Crumb 2 is not Forums."
                    
                    elementPresent = sel.is_element_present(bcPrefix + divider2)
                    if elementPresent != 1:
                        errorMsg += "  Divider 2 is not present."
                        
                    elementPresent = sel.is_element_present(bcPrefix + crumb3Locator)
                    if elementPresent != 1:
                        errorMsg += "  Crumb 3 is not " + crumb3Name
                        
                    elementPresent = sel.is_element_present(bcPrefix + divider3)
                    if elementPresent != 1:
                        errorMsg += "  Divider 3 is not present"
                    
                    # Crumb 4 - the article title
                    elementPresent = sel.is_element_present(bcPrefix + "li[7]")
                    # this breadcrumb text can be long since it's a user created title
                    # compare the link and breadcrumb text as additional check.  using long strings with the starts-with( ) and contains( ) functions return True when they should return False.
                    elementText = sel.get_text(bcPrefix + "li[7]")
                    #pos = sel.get_eval("storedVars['elementText'].indexOf(storedVars['articleTitle'])")
                    if elementPresent != 1 or elementText != articleTitle:
                            print(elementText + " ::: " + articleTitle)
                            errorMsg = errorMsg + "  Crumb 4 is not article title."
                    
                    # Test there is NOT an 8th item in the breadcrumb list
                    elementPresent = sel.is_element_present(bcPrefix + "li[8]")
                    if elementPresent == 1:
                        errorMsg += "  Unexpected item after crumb 4."
                    
                    # Display a messagge if there were errors
                    # ( to temporarily force an error msg: a) append non-existent attribute to item locator(s), such as [contains(text(),"zzz")]  , b) for non-existent 8th item change locator to an existing item )
                    # sel.goto_if("( ${errorMsg} ==  )", "goBackPage")
                    if errorMsg != "":
                        articleNumber = idx2 - articleIndexOffset
                        print("***** " + listDescription + " has errors at article #" + str(articleNumber) + " when " + launchDescription + ": " + errorMsg)
                    
                    # sel.label("goBackPage")
                    # return to the forum home page
                    sel.go_back()
                    sel.wait_for_page_to_load(vars.ConnectionParameters.page_load_timeout)
                    
                    # While #3 launches a page in different ways (clicking on link or loading page by URL)
                    idx3 += 1
                # sel.end_while()
                
                # While #2 indexes into the next article in the list
                idx2 += 1
            # sel.end_while()
            
            # While #1 sets selectors & variables to process next forum article list.
            idx1 += 1
        # sel.end_while()
        
        print("DONE")
            
    def tearDown(self):
        self.selenium.stop()

if __name__ == "__main__":
    unittest.main()
