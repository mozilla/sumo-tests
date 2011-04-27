class ConnectionParameters:
    server = "localhost"
    #server = "qa-selenium.mv.mozilla.com"
    port = 4444
    #browser = "IE-8;en-us;Win7-second"
    #browser = "IE-8;en-us;Win7"
    browser = "*chrome"
    #browser = "Firefox-default;en-us;MacOSX6"
    baseurl = "http://support.allizom.org"
    #baseurl = "http://support-release.allizom.org"
    #baseurl = "http://support.mozilla.com"
    baseurl_ssl = "https://support.allizom.org"
    #baseurl_ssl = "https://support-release.allizom.org"
    authurl = "http://support-release.allizom.org"
    authurlssl = "https://support-release.allizom.org"
    page_load_timeout = 120000

class ConfigOptions:
    #Environment list
    Smoketests = ["IE-8;en-us;Win7-second"]
    
#    BFT = [
#    "Firefox-default;en-us;Win7-second"
#    ]
    BFT = [
    "*chrome"
    ]
    FFT = [
    "Firefox-default;en-us;MacOSX6",
    "Firefox-default;en-us;Win7-second"
    ]
