from selenium import selenium
import vars
import unittest
import sumo_functions
from SUMO_breadcrumbs import *

class breadcrumbs_misc(unittest.TestCase):
    def setUp(self):
        self.selenium = selenium(
        vars.ConnectionParameters.server,
        vars.ConnectionParameters.port,
        vars.ConnectionParameters.browser,
        vars.ConnectionParameters.baseurl)
        self.selenium.start()
        self.selenium.set_timeout(vars.ConnectionParameters.page_load_timeout)
    
    def test_breadcrumbs_misc(self):
        sel = self.selenium
        sumo_func = sumo_functions.SUMOfunctions()

        # Objective: check the "breadcrumb" list at the top of pages.
        # verifies each breadcrumb's text and link href
        # page can be launched by link from login landing page, link from another page, directly by URLare defined by a URL, a link from a parent page, or user login.

        # Notes:
        # Script will log out any current login
        # Script requires user extension SUMO-breadcrumbs.js

        # Logout and Login links on side menu
        logoutLink = "link=Log Out"
        loginText1 = "log in"
        loginText2 = "Log In"
        loginLink = "link=" + loginText2
        # Prefix for all breadcrumb elements containing div/ul 
        bcPrefix = "//div[@id='breadcrumbs']/ul/"
        # Locators for dividers between breadcrumbs
        divider1 = "li[2]"
        divider2 = "li[4]"
        divider3 = "li[6]"
        sumo_func.open(sel, "en-US/search")
        # log out if the is a current login
        logoutLinkPresent = sel.is_element_present(logoutLink)
        # sel.goto_if("( ${logoutLinkPresent} == false )", "loggedOut")
        if logoutLinkPresent == 1:
            sel.click(logoutLink)
            sel.wait_for_page_to_load(vars.ConnectionParameters.page_load_timeout)
        # sel.label("loggedOut")

        idx1 = 0
        count = len(breadcrumbs)
        print("breadcrumb array length is " + str(count))
        
        # While #1 indexes into next breadcrumb in array
        # breadcrumb array is defined in in SUMO-breadcrumbs.py module
        # sel.while("( ${idx1} < breadcrumbs.length )")
        while int(idx1) < int(len(breadcrumbs)):
            # Set the breadcrumb locators
            crumb1_locator = breadcrumbs[idx1].crumb1Locator
            crumb1_name = breadcrumbs[idx1].crumb1Name
            crumb2_locator = breadcrumbs[idx1].crumb2Locator
            crumb2_name = breadcrumbs[idx1].crumb2Name
            crumb3_locator = breadcrumbs[idx1].crumb3Locator
            crumb3_name = breadcrumbs[idx1].crumb3Name
            crumb4_locator = breadcrumbs[idx1].crumb4Locator
            crumb4_name = breadcrumbs[idx1].crumb4Name

            pageDescription = breadcrumbs[idx1].description
            #print("page is " + pageDescription)

            idx2 = 1
            # While #2 loops thru methods of launching a page: login landing page, link from a parent page, direct URL.
            # after launching a page the breadcrumbs are verified.
            # sel.while("( ${idx2} <= 3 )")
            while idx2 <= 3:
                # access page as per loop index
                # sel.goto_if("( ${idx2} == 1 )", "loginLanding")
                # sel.goto_if("( ${idx2} == 2 )", "clickLink")
                # sel.goto_if("( ${idx2} == 3 )", "openPage")

                # Login Landing Page - breadcrumbs that appear after login
                # sel.label("loginLanding")
                if idx2 == 1:
                    user = breadcrumbs[idx1].user
                    passw = breadcrumbs[idx1].passw
                    # if no user name then skip iteration
                    # sel.goto_if("(${user} == )", "exitIteration")
                    if user == "":
                        idx2 = idx2+1
                        continue;
                    print("log in to user " + user)
                    launchDescription = "launched by login"
                    if sel.is_element_present(loginLink) != 1:
                        loginLink == "link=" + loginText1

                    sel.click(loginLink)
                    sel.wait_for_page_to_load(vars.ConnectionParameters.page_load_timeout)
                    sel.type("login-user", user)
                    sel.type("login-pass", passw)
                    sel.click("login-button")
                    sel.wait_for_page_to_load(vars.ConnectionParameters.page_load_timeout)
                    # sel.goto("verifyBreadCrumbs")

                # Click on link on the parent page
                # sel.label("clickLink")
                if idx2 == 2:
                    parent_url = breadcrumbs[idx1].parentUrl
                    link_locator = breadcrumbs[idx1].linkLocator
                    # if no link locator then skip iteration
                    # sel.goto_if("(${link_locator} == )", "exitIteration")
                    if link_locator == "":
                        idx2 = idx2+1
                        continue;
                    launchDescription = "launched by link"
                    sumo_func.open(sel, parent_url)
                    # check that the link is present on page.  exit iteration if not.
                    linkPresent = sel.is_element_present(link_locator)
                    # sel.goto_if("( ${linkPresent} == true )", "linkIsPresent")
                    if linkPresent != 1:
                        print("***** link for " + pageDescription + " not found on parent page.")
                        idx2 = idx2 + 1
                        continue;
                    # sel.goto("exitIteration")

                    # sel.label("linkIsPresent")
                    sel.click(link_locator)
                    sel.wait_for_page_to_load(vars.ConnectionParameters.page_load_timeout)
                    # sel.goto("verifyBreadCrumbs")

                # Open the page
                # sel.label("openPage")
                if idx2 == 3:
                    direct_url = breadcrumbs[idx1].directUrl
                    # if no URL then skip iteration
                    # sel.goto_if("(${direct_url} == )", "exitIteration")
                    if direct_url == "":
                        idx2 = idx2+1
                        continue;
                    launchDescription = "launched by URL"
                    
                    sumo_func.open(sel, direct_url)
                    # sel.goto("verifyBreadCrumbs")

                # Verify the breadcrumbs specified, including dividers between crumbs
                # sel.label("verifyBreadCrumbs")
                errorMsg = ""
                # li_count is the number of <li> elements verified
                li_count = 0
                # sel.goto_if("(${crumb1_locator} == )", "endVerifies")
                if crumb1_locator != "":
                    elementPresent = sel.is_element_present(bcPrefix + crumb1_locator)
                    if elementPresent != 1:
                        errorMsg += "  Crumb 1 is not " + crumb1_name
                    li_count += 1
                # sel.goto_if("(${crumb2_locator} == )", "endVerifies")
                if crumb2_locator != "":
                    elementPresent = sel.is_element_present(bcPrefix + divider1)
                    if elementPresent != 1:
                        errorMsg += "  Divider 1 is not present"
                    elementPresent = sel.is_element_present(bcPrefix + crumb2_locator)
                    if elementPresent != 1:
                        errorMsg += "  Crumb 2 is not " + crumb2_name
                    li_count += 2
                # sel.goto_if("(${crumb3_locator} == )", "endVerifies")
                if crumb3_locator != "":
                    elementPresent = sel.is_element_present(bcPrefix + divider2)
                    if elementPresent != 1:
                        errorMsg += "  Divider 2 is not present"
                    elementPresent = sel.is_element_present(bcPrefix + crumb3_locator)
                    if elementPresent != 1:
                        errorMsg += "  Crumb 3 is not " + crumb3_name
                    li_count += 2
                # sel.goto_if("(${crumb4_locator} == )", "endVerifies")
                if crumb4_locator != "":
                    elementPresent = sel.is_element_present(bcPrefix + divider3)
                    if elementPresent != 1:
                        errorMsg += "  Divider 3 is not present."
                    elementPresent = sel.is_element_present(bcPrefix + crumb4_locator)
                    if elementPresent != 1:
                        errorMsg + "  Crumb 4 is not " + crumb4_name
                    li_count += 2
                # sel.label("endVerifies")
                # check there are no additional item in the list beyond the specified breadcrumbs
                elementPresent = sel.is_element_present(bcPrefix + "li[" + str(int(li_count)+1) + "]")
                
                # error message includes dividers in expected item count
                if elementPresent == 1:
                    errorMsg += "  Expected only " + str(li_count) + " items in breadcrumb list."

                # display error message, if anything
                # sel.goto_if("( ${errorMsg} ==  )", "msgDone")
                if errorMsg != "":
                    print("***** " + pageDescription + " has errors when " + launchDescription + ": " + errorMsg)
                # sel.label("msgDone")

                # sel.label("exitIteration")
                idx2 = idx2 + 1
            # sel.end_while()

            idx1 = idx1 + 1
        # sel.end_while()

        # Logout
        sel.click(logoutLink)
        sel.wait_for_page_to_load(vars.ConnectionParameters.page_load_timeout)

        print("DONE")
    
    def tearDown(self):
        self.selenium.stop()

if __name__ == "__main__":
    unittest.main()
