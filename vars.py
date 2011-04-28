class ConnectionParameters:
    #server = "localhost"
    server = "qa-selenium.mv.mozilla.com"
    port = 4444
    browser = "*firefox"
    baseurl = "http://support.allizom.org"
    baseurl_ssl = "https://support.allizom.org"
    authurl = "http://support-release.allizom.org"
    authurlssl = "https://support-release.allizom.org"
    page_load_timeout = 120000

class ConfigOptions:
    #Environment list
    Smoketests = [
    #"Firefox-default;en-us;MacOSX6"
    "Firefox-default;en-us;Win7-second"
    ]
    
    BFT = [
    "Firefox-default;en-us;Win7-second"
    ]
    
    FFT = [
    "Firefox-default;en-us;MacOSX6",
    "Firefox-default;en-us;Win7-second"
    ]
