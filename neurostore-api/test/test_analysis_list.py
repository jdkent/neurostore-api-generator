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
from neurostore_api.model.analysis_return import AnalysisReturn
from neurostore_api.model.metadata import Metadata
globals()['AnalysisReturn'] = AnalysisReturn
globals()['Metadata'] = Metadata
from neurostore_api.model.analysis_list import AnalysisList


class TestAnalysisList(unittest.TestCase):
    """AnalysisList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAnalysisList(self):
        """Test AnalysisList"""
        # FIXME: construct object with mandatory attributes with example values
        # model = AnalysisList()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
