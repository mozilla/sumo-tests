#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from unittestzero import Assert
import pytest
import requests


@pytest.mark.skip_selenium
@pytest.mark.nondestructive
class TestRedirects:

    _user_agent_firefox = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:10.0.1) Gecko/20100101 Firefox/10.0.1'

    def _check_redirect(self, testsetup, start_url, expected_url, user_agent=_user_agent_firefox, locale='en-US'):
        start_url = testsetup.base_url + start_url
        expected_url = testsetup.base_url + expected_url

        headers = {'user-agent': user_agent,
                   'accept-language': locale}
        r = requests.get(start_url, headers=headers)
        Assert.equal(r.url, expected_url)

    @pytest.mark.parametrize(('input', 'expected'), [
        ('/ja-JP-mac/kb', '/ja/home'),
        ('/nn-NO/kb', '/no/home'),
        ('/es-ES/kb', '/es/home'),
        ('/es-AR/kb', '/es/home'),
        ('/es-CL/kb', '/es/home'),
        ('/en-US/kb', '/en-US/home'),
        ('/en/kb', '/en-US/home')])
    def test_redirect_locale_to_home(self, mozwebqa, input, expected):
        self._check_redirect(mozwebqa, input, expected)

    @pytest.mark.parametrize(('input', 'expected'), [
        ('/windows7-support', '/en-US/home?as=u')])
    def test_support_links(self, mozwebqa, input, expected):
        self._check_redirect(mozwebqa, input, expected)

    @pytest.mark.xfail(reason='Tests redirect to production')
    @pytest.mark.parametrize(('input', 'expected'), [
        ('/1/mobile/4.0/android/en-US/firefox-help', '/en-US/home?as=u'),
        ('/1/mobile/4.0/iphone/en-US/firefox-help', '/en-US/home?as=u'),
        ('/1/mobile/4.0/nokia/en-US/firefox-help', '/en-US/home?as=u')])
    def test_old_mobile_redirects(self, mozwebqa, input, expected):
        self._check_redirect(mozwebqa, input, expected)

    @pytest.mark.parametrize(('input', 'expected'), [
        ('/contribute', '/en-US/home?as=u')])
    def test_contribute_redirects(self, mozwebqa, input, expected):
        self._check_redirect(mozwebqa, input, expected)

    @pytest.mark.parametrize(('input', 'expected'), [
        ('/1/firefox-home/4.0/iPhone/en-US/log-in', '/en-US/kb/Cannot%20log%20in%20to%20Firefox%20Home%20App?as=u')])
    def test_contribute_redirects(self, mozwebqa, input, expected):
        self._check_redirect(mozwebqa, input, expected)
