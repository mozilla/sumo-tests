import sumo_test_data
import sumo_functions

# Recurring breadcrumb links
FirefoxSupport1 = "li[1]/a"
KnowledgeBase2 = "li[3]/span/a"
Forums2 = "li[3]/a"
ForumsFirefox3 = "li[5]/a"
HowToContribute2 = "li[3]/span/a"
accounts = sumo_test_data.SUMOtestData()
functions = sumo_functions.SUMOfunctions()
user = accounts.getUserInfo(0)


# *** Adding breadcrumbs ***
#		the script references the breadcrumbs array by index, not the individual s stored in it
#		the  name for a breadcrumb object is not important but must be unique.
# *** Editting this file ***
#		Remember that selenium IDE must be closed and restarted to see changes in this or any user extension
 

# ious breadcrumbs that don't belong to a list 


# Object defintion 
class breadcrumbObject():
        description=""	    # description of the breadcrumbs.  used in error message.
        user=""		        # user name and password for log in.  script tests breadcrumbs on the landing page
        passw=""
        parentUrl=""		# relative URL of page with the link to article.  page open uses this value unmodified.
        linkLocator=""	    # link locator to page with the breadcrumbs. clickAndWait uses this value unmodified.
                                    # if empty the script skips opening the page using a link
        directUrl=""		# relative URL of page with breadcrumbs.  page open uses this value unmodified.
                                    # 	if empty the script skips opening the page directly by URL.
                                    # generally, linkLocator and directUrl reference to the same page, but there could be exceptions.
                                    # crumbXLocator is locator for crumbX.  values are appended to div/ul specifiers common to all breadcrumbs.
                                    # crumbXName is a friendly name for crumbX.  used in error message.
                                    # crumbs that aren't used are set to "".  crumb1Locator = "" indicates no breadcrumbs expected.
        crumb1Locator=""	
        crumb1Name=""	
        crumb2Locator=""
        crumb2Name=""
        crumb3Locator=""
        crumb3Name=""
        crumb4Locator=""
        crumb4Name=""


breadcrumbs = []

# Log In link
login0 = breadcrumbObject()
login0.description="Log In page from side menu (WITHOUT logon)"
login0.parentUrl = "/en-US/kb/Contributor+Home+Page"
login0.linkLocator = "link=Log In"
login0.directUrl = "/tiki-login.php?locale=en-US"
login0.crumb1Locator = FirefoxSupport1
login0.crumb1Name = "Firefox Support"
breadcrumbs.append(login0)

		
# Contributer Home Page and user login lands at the page
login1 = breadcrumbObject()
login1.description="Login landing page & Contribute Home Page"
login1.user = user['username']
login1.passw = user['password']
login1.parentUrl = "/en-US/kb/Contributor+Home+Page"
#login1.linkLocator = "//div[@id='contrib_tools2']/div/a[ contains(@href,'/kb/Contributor+Home+Page') ]"
login1.directUrl = "/en-US/kb/Contributor+Home+Page"
login1.crumb1Locator = FirefoxSupport1
login1.crumb1Name = "Firefox Support"
login1.crumb2Locator = KnowledgeBase2
login1.crumb2Name = "Knowledge Base"
login1.crumb3Locator = "li[5]"
login1.crumb3Name = "Contributor Home Page"
breadcrumbs.append(login1)

# Log In page when logged in
login2 = breadcrumbObject()
login2.description="Log In page from side menu (WITH logon)"
login2.parentUrl = ""
login2.linkLocator = ""  # no available link
login2.directUrl = "/tiki-login.php?locale=en-US"
login2.crumb1Locator = FirefoxSupport1
login2.crumb1Name = "Firefox Support"
breadcrumbs.append(login2)
		
# Links in the upper right side bar menu 
# Firefox Support header 
sb1 = breadcrumbObject()
sb1.description="Firefox Support home page from side menu (header link)"
sb1.parentUrl = "/en-US/search"
sb1.linkLocator = "//ul[@id='side-menu']/li/h3/a[ contains(@href,'/kb/') ][ contains(text(),'Firefox Support') ]"
sb1.directUrl = ""
sb1.crumb1Locator = "" 	# no breadcrumbs
breadcrumbs.append(sb1)

# Knowledge Base 
sb2 = breadcrumbObject()
sb2.description="Firefox Support home page from side menu (KB link)"
sb2.parentUrl = "/en-US/search"
sb2.linkLocator = "//ul[@id='side-menu']/li/a[ contains(@href,'/kb/') ][ contains(text(),'Knowledge Base') ]"
sb2.directUrl = ""		# same as previous object
sb2.crumb1Locator = "" 	# no breadcrumbs
breadcrumbs.append(sb2)

# Support Forum
sb3 = breadcrumbObject()
sb3.description="Support Forum home page from side menu"
sb3.parentUrl = "/en-US/search"
sb3.linkLocator = "//ul[@id='side-menu']/li/a[ contains(@href,'/forum') ][ contains(text(),'Support Forum') ]"
sb3.directUrl = "/forum"
sb3.crumb1Locator = "" 	# no breadcrumbs
breadcrumbs.append(sb3)

# Ask A Question
sb4 = breadcrumbObject()
sb4.description="Ask A Question page from side menu"
sb4.parentUrl = "/en-US/search"
sb4.linkLocator = "//ul[@id='side-menu']/li/a[ contains(@href,'/kb/Ask+a+question') ]"
sb4.directUrl = "/en-US/kb/Ask+a+question"
sb4.crumb1Locator = FirefoxSupport1
sb4.crumb1Name = "FirefoxSupport"
sb4.crumb2Locator = "li[3][contains(text(),'Ask a question')]"
sb4.crumb2Name = "Ask a question"
breadcrumbs.append(sb4)

# Other Firefox Support
sb5 = breadcrumbObject()
sb5.description="Other Firefox Support page from side menu"
sb5.parentUrl = "/en-US/search"
sb5.linkLocator = "//ul[@id='side-menu']/li/a[ contains(@href,'/kb/Other+Firefox+support') ]"
sb5.directUrl = "/en-US/kb/Other+Firefox+support"
sb5.crumb1Locator = FirefoxSupport1
sb5.crumb1Name = "Firefox Support"
sb5.crumb2Locator = "li[3][contains(text(),'Other Firefox support')]"
sb5.crumb2Name = "Other Firefox support"
breadcrumbs.append(sb5)

# How to Contribute 
sb6 = breadcrumbObject()
sb6.description="How To Contribute page from side menu"
sb6.parentUrl = "/en-US/search"
sb6.linkLocator = "//ul[@id='side-menu']/li/a[contains(@href,'/kb/How+to+contribute') ]"
sb6.directUrl = "/en-US/kb/How+to+contribute"
sb6.crumb1Locator = FirefoxSupport1
sb6.crumb1Name = "Firefox Support"
sb6.crumb2Locator = "li[3][contains(text(),'How')][contains(text(),'contribute')]"
sb6.crumb2Name = "How to contribute"
breadcrumbs.append(sb6)

# My Account / User Preferences 
sb7 = breadcrumbObject()
sb7.description="My Account / User Preferences page from side menu"
sb7.parentUrl = "/en-US/kb/How+to+contribute"	# a bug has caused the link to sometimes not display from the KB home
sb7.linkLocator = "//ul[@id='side-menu']/li/a[ contains(@href,'/tiki-user_preferences.php?locale=en-US') ]"
sb7.directUrl = "/tiki-user_preferences.php?locale=en-US"
sb7.crumb1Locator = FirefoxSupport1
sb7.crumb1Name = "Firefox Support"
breadcrumbs.append(sb7)

# Browse all Knowledge Base topics home page 
misc1 = breadcrumbObject()
misc1.description="Browse All KB Topics home page"
misc1.parentUrl = ""
misc1.linkLocator = "//a[contains(@href,'/kb/Article+list') ]"
misc1.directUrl = "/en-US/kb/Article+list"
misc1.crumb1Locator = FirefoxSupport1
misc1.crumb1Name = "Firefox Support"
misc1.crumb2Locator = "li[3][contains(text(),'Article list')]"
misc1.crumb2Name = "Article list"
breadcrumbs.append(misc1)

# Knowledge Base Policies KB article 
misc2 = breadcrumbObject()
misc2.description="Knowledge Base Policies article"
misc2.parentUrl = "/en-US/kb/Contributor+Home+Page"
misc2.linkLocator = "//a[contains(@href,'/kb/Knowledge+Base+Policies') ]"
misc2.directUrl = "/en-US/kb/Knowledge+Base+Policies"
misc2.crumb1Locator = FirefoxSupport1
misc2.crumb1Name = "Firefox Support"
misc2.crumb2Locator = "li[3][contains(text(),'Knowledge Base Policies')]"
misc2.crumb2Name = "Knowledge Base Policies"
breadcrumbs.append(misc2)

# User Permission Levels / Group Permissions KB article 
misc3 = breadcrumbObject()
misc3.description="Group Permissions article"
misc3.parentUrl = "/en-US/kb/Contributor+Home+Page"
misc3.linkLocator = "//a[contains(@href,'/kb/Group+permissions') ]"
misc3.directUrl = "/en-US/kb/Group+permissions"
misc3.crumb1Locator = FirefoxSupport1
misc3.crumb1Name = "Firefox Support"
misc3.crumb2Locator = "li[3][contains(text(),'Group permissions')]"
misc3.crumb2Name = "Group permissions"
breadcrumbs.append(misc3)

# Introduction to Live Chat KB article 
misc4 = breadcrumbObject()
misc4.description="Introduction to Live Chat article"
misc4.parentUrl = "/en-US/kb/Helping+with+Live+Chat"
misc4.linkLocator = "//a[contains(@href,'/kb/Introduction+to+Live+Chat') ]"
misc4.directUrl = "/en-US/kb/Introduction+to+Live+Chat"
misc4.crumb1Locator = FirefoxSupport1
misc4.crumb1Name = "Firefox Support"
misc4.crumb2Locator = "li[3][contains(text(),'Introduction to Live Chat')]"
misc4.crumb2Name = "Introduction to Live Chat"
breadcrumbs.append(misc4)

'''
# Weekly Common Issues page 
# No longer used, so not testing
misc5 = breadcrumbObject()
misc5.description="Weekly Common Issues page"
misc5.parentUrl = "/en-US/kb/Contributing+to+the+Knowledge+Base"
misc5.linkLocator = "//a[contains(@href,'/kb/Weekly+common+issues') ]"
misc5.directUrl = "/en-US/kb/Weekly+common+issues"
misc5.crumb1Locator = FirefoxSupport1
misc5.crumb1Name = "Firefox Support"
misc5.crumb2Locator = "li[3][contains(text(),'Weekly common issues')]"
misc5.crumb2Name = "Weekly common issues"
breadcrumbs.append(misc5)
'''


# breadcrumbs in How-to-Contribute series 


class HTC_BreadcrumbObject():
    parentUrlEnding=""		# end of URL of page with the link to article.  page open appends value to "/en-US/kb/"
    articleUrlEnding=""	# end of URL of article with breadcrumbs.  value will be embedded into the locator #a[contains(@href,'???')]


HTC_breadcrumbs = []

HTC1 = HTC_BreadcrumbObject()
HTC1.parentUrlEnding="How+to+contribute"
HTC1.articleUrlEnding="Contributing+to+the+Knowledge+Base"
HTC_breadcrumbs.append(HTC1)

HTC2 = HTC_BreadcrumbObject()
HTC2.parentUrlEnding="Contributing+to+the+Knowledge+Base"
HTC2.articleUrlEnding="How+we+are+different"
HTC_breadcrumbs.append(HTC2)

HTC3 = HTC_BreadcrumbObject()
HTC3.parentUrlEnding="Contributing+to+the+Knowledge+Base"
HTC3.articleUrlEnding="Improving+articles"
HTC_breadcrumbs.append(HTC3)

HTC4 = HTC_BreadcrumbObject()
HTC4.parentUrlEnding="Contributor+Home+Page"
HTC4.articleUrlEnding="Updating+articles+for+Firefox+35"
HTC_breadcrumbs.append(HTC4)

HTC5 = HTC_BreadcrumbObject()
HTC5.parentUrlEnding="Contributor+Home+Page"
HTC5.articleUrlEnding="Localization+Dashboard"
HTC_breadcrumbs.append(HTC5)

HTC6 = HTC_BreadcrumbObject()
HTC6.parentUrlEnding="Contributor+Home+Page"
HTC6.articleUrlEnding="Translating+articles"
HTC_breadcrumbs.append(HTC6)

HTC7 = HTC_BreadcrumbObject()
HTC7.parentUrlEnding="Contributor+Home+Page"
HTC7.articleUrlEnding="Translating+the+interface"
HTC_breadcrumbs.append(HTC7)


#HTC8 = HTC_BreadcrumbObject()
#HTC8.parentUrlEnding="Contributor+Home+Page"
#HTC8.articleUrlEnding="Localizing+Firefox+Support"
#HTC_breadcrumbs.append(HTC8)

HTC9 = HTC_BreadcrumbObject()
HTC9.parentUrlEnding="Contributor+Home+Page"
HTC9.articleUrlEnding="Approving+articles+and+edits"
HTC_breadcrumbs.append(HTC9)

HTC10 = HTC_BreadcrumbObject()
HTC10.parentUrlEnding="Contributor+Home+Page"
HTC10.articleUrlEnding="Editing+articles"
HTC_breadcrumbs.append(HTC10)

HTC11 = HTC_BreadcrumbObject()
HTC11.parentUrlEnding="Contributor+Home+Page"
HTC11.articleUrlEnding="Creating+articles"
HTC_breadcrumbs.append(HTC11)

HTC12 = HTC_BreadcrumbObject()
HTC12.parentUrlEnding="Contributor+Home+Page"
HTC12.articleUrlEnding="Adding+screenshots"
HTC_breadcrumbs.append(HTC12)

HTC13 = HTC_BreadcrumbObject()
HTC13.parentUrlEnding="Contributor+Home+Page"
HTC13.articleUrlEnding="Requesting+an+article"
HTC_breadcrumbs.append(HTC13)

HTC14 = HTC_BreadcrumbObject()
HTC14.parentUrlEnding="Contributor+Home+Page"
HTC14.articleUrlEnding="Creating+content+blocks"
HTC_breadcrumbs.append(HTC14)

HTC15 = HTC_BreadcrumbObject()
HTC15.parentUrlEnding="Contributor+Home+Page"
HTC15.articleUrlEnding="Best+Practices+for+Support+Documents"
HTC_breadcrumbs.append(HTC15)

HTC16 = HTC_BreadcrumbObject()
HTC16.parentUrlEnding="Contributor+Home+Page"
HTC16.articleUrlEnding="Style+Guide"
HTC_breadcrumbs.append(HTC16)

HTC17 = HTC_BreadcrumbObject()
HTC17.parentUrlEnding="Contributor+Home+Page"
HTC17.articleUrlEnding="Using+SHOWFOR"
HTC_breadcrumbs.append(HTC17)

HTC18 = HTC_BreadcrumbObject()
HTC18.parentUrlEnding="Contributor+Home+Page"
HTC18.articleUrlEnding="Dynamic+Content"
HTC_breadcrumbs.append(HTC18)

HTC19 = HTC_BreadcrumbObject()
HTC19.parentUrlEnding="Contributor+Home+Page"
HTC19.articleUrlEnding="Providing+forum+support"
HTC_breadcrumbs.append(HTC19)

HTC20 = HTC_BreadcrumbObject()
HTC20.parentUrlEnding="Contributor+Home+Page"
HTC20.articleUrlEnding="Forum+and+chat+rules+and+guidelines"
HTC_breadcrumbs.append(HTC20)

HTC21 = HTC_BreadcrumbObject()
HTC21.parentUrlEnding="Contributor+Home+Page"
HTC21.articleUrlEnding="Installing+and+Configuring+Spark"
HTC_breadcrumbs.append(HTC21)

HTC22 = HTC_BreadcrumbObject()
HTC22.parentUrlEnding="Contributor+Home+Page"
HTC22.articleUrlEnding="Helping+with+Live+Chat"
HTC_breadcrumbs.append(HTC22)






