"""
A FancyURLopener subclass for accessing SUMO.
"""

import urllib


class SumoURLopener(urllib.FancyURLopener):
    def prompt_user_passwd(self, host, realm):
        return ('support', 'stage')
