class ConnectionParameters:
    server = "localhost"
    port = 4444
    browser = "Firefox-default;en-us;MacOSX6"
    baseurl = "http://support.allizom.org"
    baseurl_ssl = "https://support.allizom.org"
    authurl = "http://support-release.allizom.org"
    authurlssl = "https://support-release.allizom.org"
    page_load_timeout = 120000

class ConfigOptions:
    #Environment list
    Smoketests = [
    "Firefox-default;en-us;MacOSX6"
    ]
    
    BFT = [
    "Firefox-default;en-us;Win7-second"
    ]
    
    FFT = [
    "Firefox-default;en-us;MacOSX6",
    "Firefox-default;en-us;Win7-second"
    ]
