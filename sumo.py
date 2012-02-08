# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""
A FancyURLopener subclass for accessing SUMO.
"""

import urllib


class SumoURLopener(urllib.FancyURLopener):
    def prompt_user_passwd(self, host, realm):
        return ('support', 'stage')
