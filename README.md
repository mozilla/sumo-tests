
Firefox Support Site (SUMO) Tests
===================

Automated tests for the Firefox Support (SUMO) web application.

Tests Support site for Firefox, support.mozilla.com on
staging: http://support.allizom.org
certification-branch: http://support-release.allizom.org

For information specific to Firefox Support see the [GitHub repository][GitHub Support].

[GitHub Support]: https://github.com/jsocol/kitsune

Running Tests
-------------

### Java
You will need a version of the [Java Runtime Environment][JRE] installed

[JRE]: http://www.oracle.com/technetwork/java/javase/downloads/index.html

### Python
Before you will be able to run these tests you will need to have Python 2.6 installed.

Run

    easy_install pip

followed by

    sudo pip install -r requirements/mozwebqa.txt

__note__

If you are running on Ubuntu/Debian you will need to do following first

    sudo apt-get install python-setuptools
    
to install the required Python libraries.

### Selenium
Once this is all set up you will need to download and start a Selenium server. You can download the latest Selenium server from [here][Selenium Downloads]. The filename will be something like 'selenium-server-standalone-2.0b2.jar'

To start the Selenium server run the following command:

    java -jar ~/Downloads/selenium-server-standalone-2.0b3.jar

Change the path/name to the downloaded Selenium server file.

[Selenium Downloads]: http://code.google.com/p/selenium/downloads/list

### Running tests locally

To run tests locally its a simple case of calling the command below from this directory

    py.test . 


Writing Tests
-------------

If you want to get involved and add more tests then there's just a few things
we'd like to ask you to do:

1. Use the [template files][GitHub Templates] for all new tests and page objects
2. Follow our simple [style guide][Style Guide]
3. Fork this project with your own GitHub account
4. Make sure all tests are passing, and submit a pull request with your changes

Note: You will need a file called sumo_test_data.py which is not on GitHub.
      Scroll down for more information

[GitHub Templates]: https://github.com/AutomatedTester/mozwebqa-test-templates
[Style Guide]: https://wiki.mozilla.org/QA/Execution/Web_Testing/Docs/Automation/StyleGuide

License
-------
This software is licensed under the [Mozilla Tri-License][MPL]:

    ***** BEGIN LICENSE BLOCK *****
    Version: MPL 1.1/GPL 2.0/LGPL 2.1

    The contents of this file are subject to the Mozilla Public License Version
    1.1 (the "License"); you may not use this file except in compliance with
    the License. You may obtain a copy of the License at
    http://www.mozilla.org/MPL/

    Software distributed under the License is distributed on an "AS IS" basis,
    WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License
    for the specific language governing rights and limitations under the
    License.

    The Original Code is Mozilla WebQA Selenium Tests.

    The Initial Developer of the Original Code is Mozilla.
    Portions created by the Initial Developer are Copyright (C) 2011
    the Initial Developer. All Rights Reserved.

    Contributor(s):
      Your Name

    Alternatively, the contents of this file may be used under the terms of
    either the GNU General Public License Version 2 or later (the "GPL"), or
    the GNU Lesser General Public License Version 2.1 or later (the "LGPL"),
    in which case the provisions of the GPL or the LGPL are applicable instead
    of those above. If you wish to allow use of your version of this file only
    under the terms of either the GPL or the LGPL, and not to allow others to
    use your version of this file under the terms of the MPL, indicate your
    decision by deleting the provisions above and replace them with the notice
    and other provisions required by the GPL or the LGPL. If you do not delete
    the provisions above, a recipient may use your version of this file under
    the terms of any one of the MPL, the GPL or the LGPL.

    ***** END LICENSE BLOCK *****

[MPL]: http://www.mozilla.org/MPL/

Sumo User Account file
___________________________

In order to run the SUMO tests on your local machine you will need to have in your 
repository a file called  sumo_test_data.py which is purposely not put on Github 
since it has user account information.
Here's a sample file. Create your own user accounts on [SUMO staging site] and 
replace the 'xxxx' in the file with your user-name and password and keep the file
in your local repository. Do Not check-in this file on Github.
[SUMO staging site]: https://support.allizom.org/en-US/users/register

sample sumo_test_data.py :

#!/usr/bin/env python

class SUMOtestData(object):
    """
    User accounts etc. 
    Keep this file in your local repository
    Do Not check-in this file on Github
    """


    def __init__(self):
        '''
        Constructor
        '''
        self.userNonAdm = {'username':'xxx','password':'xxx','email':'xxx@gmail.com'}
        self.userAdm = {'username':'xxx','password':'xxxxxx','email':'xxx@gmail.com'}
        self.userTuple = (self.userNonAdm,self.userAdm)
        
    def getUserInfo(self, key):
          
        return (self.userTuple[key])
    
    