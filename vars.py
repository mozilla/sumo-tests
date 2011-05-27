class ConnectionParameters:
    server = "localhost"
    port = 4444
    browser = "*chrome"
    baseurl = "http://support.allizom.org"
    baseurl_ssl = "https://support.allizom.org"
    authurl = "http://support-release.allizom.org"
    authurlssl = "https://support-release.allizom.org"
    page_load_timeout = 120000

class ConfigOptions:
    #Environment list
    Smoketests = [
    "Firefox 4 on Mac OS X"
    ]
    
    BFT = [
    "Firefox 4.0 on Windows 7"
    ]
    
    FFT = [
    "Firefox 4 on Mac OS X",
    "Firefox 4.0 on Windows 7"
    "Internet Explorer 8 on Windows 7"
    ]
