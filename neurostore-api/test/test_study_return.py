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
from neurostore_api.model.analysis import Analysis
from neurostore_api.model.read_only import ReadOnly
from neurostore_api.model.study import Study
globals()['Analysis'] = Analysis
globals()['ReadOnly'] = ReadOnly
globals()['Study'] = Study
from neurostore_api.model.study_return import StudyReturn


class TestStudyReturn(unittest.TestCase):
    """StudyReturn unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testStudyReturn(self):
        """Test StudyReturn"""
        # FIXME: construct object with mandatory attributes with example values
        # model = StudyReturn()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
