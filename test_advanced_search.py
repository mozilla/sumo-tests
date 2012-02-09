# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""
Created 18 March 2010

@author James Socol <james@mozilla.com>

Performs a search on SUMO via the JSON API and asserts that there are some
results.
"""

import unittest
import json

from sumo import SumoURLopener

sumo = SumoURLopener()


class TestAdvancedSearch(unittest.TestCase):

    def test_categories(self):
        """Advanced KB searches with categories should return results."""

        url = 'https://support-stage.mozilla.com/search.php?q=install&%s&where=d&advanced=1&format=json'
        res = sumo.open(url % 'category[]=1')

        results = json.loads(res.read())
        self.assertNotEqual(0, results.get('total'))

        res = sumo.open(url % 'category[]=1&category[]=18')
        results = json.loads(res.read())
        self.assertNotEqual(0, results.get('total'))


if __name__ == '__main__':
    unittest.main()
