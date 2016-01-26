# Tests for Mozilla's support website
This repository contains tests for [Mozilla's support website](https://support.mozilla.org/).

[![license](https://img.shields.io/badge/license-MPL%202.0-blue.svg)](https://github.com/mozilla/sumo-tests/blob/master/LICENSE)
[![travis](https://img.shields.io/travis/mozilla/sumo-tests.svg?label=travis)](http://travis-ci.org/mozilla/sumo-tests/)
[![stage](https://img.shields.io/jenkins/s/https/webqa-ci.mozilla.com/sumo.stage.svg?label=stage)](https://webqa-ci.mozilla.com/job/sumo.stage/)
[![prod](https://img.shields.io/jenkins/s/https/webqa-ci.mozilla.com/sumo.prod.svg?label=prod)](https://webqa-ci.mozilla.com/job/sumo.prod/)
[![requirements](https://img.shields.io/requires/github/mozilla/sumo-tests.svg)](https://requires.io/github/mozilla/sumo-tests/requirements/?branch=master)

## Getting involved
We love working with contributors to fill out the test coverage for Mozilla's
support website, but it does require a few skills. By contributing to our test
suite you will have an opportunity to learn and/or improve your skills with
Python, Selenium WebDriver, GitHub, virtual environments, the Page Object
Model, and more.

For some resources for learning about these technologies, take a look at our
documentation on [running Web QA automated tests][running-tests].

All of [these awesome contributors][contributors] have opened pull requests
against this repository.

## Questions are always welcome
While we take pains to keep our documentation updated, the best source of
information is those of us who work on the project. Don't be afraid to join us
in irc.mozilla.org [#mozwebqa][irc] to ask questions about our tests. We also
have a [mailing list][list] available that you are welcome to join and post to.

## How to run the tests locally
We maintain a [detailed guide][running-tests] to running our automated tests.
However, if you want to get started quickly, you can try following the steps
below:

### Clone the repository
If you have cloned this project already then you can skip this, otherwise you'll
need to clone this repo using Git. If you do not know how to clone a GitHub
repository, check out this [help page][git-clone] from GitHub.

If you think you would like to contribute to the tests by writing or maintaining
them in the future, it would be a good idea to create a fork of this repository
first, and then clone that. GitHub also has great documentation for
[forking a repository][git-fork].

### Create or activate a Python virtual environment
You should install this project's dependencies (which is described in the next
step) into a virtual environment in order to avoid impacting the rest of your
system, and to make problem solving easier. If you already have a virtual
environment for these tests, then you should activate it, otherwise you should
create a new one. For more information on working with virtual environments see
our [summary][virtualenv].

### Install dependencies
Install the Python packages that are needed to run our tests using pip. In a
terminal, from the the project root, issue the following command:

```bash
$ pip install -Ur requirements.txt
```

### Create test users

Some of the tests require logging in as a administrator, and others require
logging in as a user. To run these tests you will need to create accounts on
https://support.allizom.org/. If you want to run the tests that require
administrator access, then you will need to ask someone on [irc][irc] to
upgrade one of your test accounts.

### Create a variables file
The credentials associated with the test users are stored in a JSON file, which
we then pass to the tests via the command line. If you want to be able to run
any of those tests, you will need to create a variables file containing your
own credentials (see above). The following is an example JSON file with the
values missing. You can use this as a template.

```json
{
  "users": {
    "default": {
      "username": "",
      "password": "",
      "email": ""},
    "admin": {
      "username": "",
      "password": "",
      "email": ""}
  }
}
```



You will then pass the name of that your variables file on the command line.
For the purposes of the examples below, assume you named your copy of the file
`my_variables.json`.

### Run the tests
Tests are run using the command line. Below are a couple of examples of running
the tests:

To run all of the desktop tests against the default environment:

```bash
$ py.test --driver Firefox --variables my_variables.json tests/desktop
```

To run against a different environment, pass in a value for `--base-url`, like so:

```bash
$ py.test --base-url https://support.allizom.org --driver Firefox --variables my_variables.json tests/desktop
```

To run the mobile tests you will need to target a mobile device or emulator
using a tool like [Appium][appium]:

```bash
$ py.test --driver Remote --port 4723 \
--capability platformName iOS \
--capability platformVersion 9.2 \
--capability deviceName "iPhone 6" \
--capability browserName Safari \
--variables my_variables.json \
tests/mobile
```

Alternatively you can change the default user agent in Firefox to masquerade
as a mobile browser:

```bash
$ py.test --driver Firefox \
--firefox-preference general.useragent.override "Mozilla/5.0 (iPhone; CPU iPhone OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) GSA/8.0.57838 Mobile/12H321 Safari/600.1.4" \
--variables .variables.json \
tests/mobile
```

The pytest plugin that we use for running tests has a number of advanced
command line options available. To see the options available, run
`py.test --help`. The full documentation for the plugin can be found
[here][pytest-selenium].

[contributors]: https://github.com/mozilla/sumo-tests/contributors
[git-clone]: https://help.github.com/articles/cloning-a-repository/
[git-fork]: https://help.github.com/articles/fork-a-repo/
[irc]: http://widget01.mibbit.com/?settings=1b10107157e79b08f2bf99a11f521973&server=irc.mozilla.org&channel=%23mozwebqa
[list]: https://mail.mozilla.org/listinfo/mozwebqa
[appium]: http://appium.io/
[pytest-selenium]: https://github.com/mozilla/pytest-selenium
[running-tests]: https://developer.mozilla.org/en-US/docs/Mozilla/QA/Running_Web_QA_automated_tests
[virtualenv]: https://wiki.mozilla.org/QA/Execution/Web_Testing/Automation/Virtual_Environments
