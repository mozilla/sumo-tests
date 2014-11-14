Selenium Tests for support.mozilla.org - the Mozilla Support Site (SUMO)
===================

Thank you for checking out Mozilla's SUMO test suite. Mozilla and the Mozwebqa team are grateful for the help and hard work of many contributors like yourself.
The following contributors have submitted pull requests to sumo-tests:

https://github.com/mozilla/sumo-tests/contributors

Getting involved as a contributor
------------------------------------------

We love working with contributors to fill out the Selenium test coverage for sumo-tests, but it does require a few skills.   You will need to know some Python, some Selenium and you will need some basic familiarity with GitHub.

If you know some Python, it's worth having a look at the Selenium framework to understand the basic concepts of browser-based testing and especially page objects.

If you need to brush up on programming but are eager to start contributing immediately, please consider helping us find bugs in Mozilla [Firefox][firefox] or find bugs in the Mozilla web-sites tested by the [WebQA][webqa] team.

To brush up on Python skills before engaging with us, [Dive Into Python][dive] is an excellent resource.  MIT also has [lecture notes on Python][mit] available through their open courseware.The programming concepts you will need to know include functions, working with classes, and some object-oriented programming basics.

[mit]: http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-189-a-gentle-introduction-to-programming-using-python-january-iap-2011/
[dive]: http://www.diveintopython.net/toc/
[webqa]: https://quality.mozilla.org/teams/web-qa/
[firefox]: https://quality.mozilla.org/teams/firefoxqe//
[webdriver]: http://seleniumhq.org/docs/03_webdriver.html

Questions are always welcome
----------------------------
While we take pains to keep our documentation updated, the best source of information is those of us who work on the project.  Don't be afraid to join us in irc.mozilla.org #mozwebqa to ask questions about our Selenium tests.  Mozilla also hosts the  [#mozillians][mozillians] chat room to answer your general questions about contributing to Mozilla.

[mozwebqa]:http://chat.mibbit.com/?server=irc.mozilla.org&channel=#mozwebqa
[mozillians]:http://chat.mibbit.com/?server=irc.mozilla.org&channel=#mozillians




How to Set up and Build SUMO Tests Locally
------------------------------------------
This repository contains Selenium tests used to test the website support.mozilla.org on
development: http://support-dev.allizom.org or
staging: http://support.allizom.org

For information specific to Firefox Support see the [GitHub repository][GitHub Support].

[GitHub Support]: https://github.com/mozilla/kitsune

Mozilla maintains a guide to running Automated tests on our QMO website:

https://developer.mozilla.org/docs/Mozilla/QA/Running_Web_QA_automated_tests
This wiki page has some advanced instructions specific to Windows:

https://wiki.mozilla.org/QA_SoftVision_Team/WebQA_Automation


###You will need to install the following:

#### Git
If you have cloned this project already then you can skip this!
GitHub has excellent guides for [Windows][GitWin], [MacOSX][GitMacOSX] and [Linux][GitLinux].
[GitWin]: http://help.github.com/win-set-up-git/
[GitMacOSX]: http://help.github.com/mac-set-up-git/
[GitLinux]: http://help.github.com/linux-set-up-git/

#### Python
Before you will be able to run these tests you will need to have [Python 2.6][Python] installed.
[Python]: http://www.python.org/download/releases/2.6.6/

Run

    easy_install pip

followed by

    sudo pip install -r requirements.txt

__note__

If you are running on Ubuntu/Debian you will need to do following first

    sudo apt-get install python-setuptools

to install the required Python libraries.

####Virtualenv and Virtualenvwrapper (Optional/Intermediate level)
While most of us have had some experience using virtual machines, [virtualenv][venv] is something else entirely.  It's used to keep libraries that you install from clashing and messing up your local environment.  After installing virtualenv, installing [virtualenvwrapper][wrapper] will give you some nice commands to use with virtualenvwrapper.

[venv]: http://pypi.python.org/pypi/virtualenv
[wrapper]: http://www.doughellmann.com/projects/virtualenvwrapper/

#### Credentials

Some of the tests in sumo-tests require logging in to https://support.allizom.org with credentials of varying privilege levels.

1. Create two username and password combinations on https://support.allizom.org
2. Join [#sumo][sumo] and ask for one of these users to be upgraded to admin (or ask someone on [#mozwebqa][mozwebqa] to do this for you)
3. Copy sumo-tests/credentials.yaml to a location outside of sumo-tests. update the 'default' and 'admin' users in credentials.yaml with those credentials

[mozwebqa]:http://chat.mibbit.com/?server=irc.mozilla.org&channel=#mozwebqa
[sumo]:http://chat.mibbit.com/?server=irc.mozilla.org&channel=#sumo


#### Running tests locally


Before each test run, clean up the repo:
    find . \( -name 'results*' -or -name '*.pyc' \) -print0 | xargs -0 rm -Rf

To run tests locally its a simple case of calling the command below from this directory

    py.test --driver=firefox --destructive --credentials=/full/path/to/credentials.yaml .

__Output__
Output of a test run should look like this:

	============================= test session starts ==============================
	platform darwin -- Python 2.6.1 -- pytest-2.2.3
	collected 35 items 
	
	tests/desktop/test_kb_article.py .X....
	tests/desktop/test_new_user_registration.py .
	tests/desktop/test_questions.py ....
	tests/desktop/test_rewrites.py .....................
	tests/desktop/test_search.py ..X
	
	==================== 33 passed, 2 xpassed in 172.03 seconds ====================

__Note__
"~" will not resolve to the home directory when used in the py.test command line.

Some options for py.test are pre-specified by the file sumo_tests/mozwebqa.cfg

The mozwebqa plugin has advanced command line options for reporting and using browsers. See the documentation on [davehunt's pytest mozwebqa github][pymozwebqa]:
[pymozwebqa]: https://github.com/davehunt/pytest-mozwebqa

__Troubleshooting__

If the test run hangs with Firefox open but no URL gets entered in the address box, some combination of the Firefox version, the Selenium RC version, and the python Selenium bindings version may not be compatible. Upgrading each of them to latest should fix it.

Writing Tests
-------------

If you want to get involved and add more tests, then there's just a few things
we'd like to ask you to do:

1. Use the [template files][GitHub Templates] for all new tests and page objects
2. Follow our simple [style guide][Style Guide]
3. Fork this project with your own GitHub account
4. Make sure all tests are passing, and submit a pull request with your changes

[GitHub Templates]: https://github.com/mozilla/mozwebqa-test-templates
[Style Guide]: https://wiki.mozilla.org/QA/Execution/Web_Testing/Docs/Automation/StyleGuide


License
-------
This software is licensed under the [MPL] 2.0:

    This Source Code Form is subject to the terms of the Mozilla Public
    License, v. 2.0. If a copy of the MPL was not distributed with this
    file, You can obtain one at http://mozilla.org/MPL/2.0/.

[MPL]: http://www.mozilla.org/MPL/2.0/
