"""
    neurostore api

    Create datasets for meta-analysis  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: jamesdkent21@gmail.com
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import neurostore_api
from neurostore_api.model.image_return import ImageReturn
from neurostore_api.model.metadata import Metadata
globals()['ImageReturn'] = ImageReturn
globals()['Metadata'] = Metadata
from neurostore_api.model.image_list import ImageList


class TestImageList(unittest.TestCase):
    """ImageList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testImageList(self):
        """Test ImageList"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ImageList()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
