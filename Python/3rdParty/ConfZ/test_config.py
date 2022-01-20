#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from config import ExampleConfiguration

import unittest


class TestExampleConfiguration(unittest.TestCase):

    def setUp(self):
        self.config = ExampleConfiguration()

    def test_config_has_a_name_attrib_of_type_string(self):
        assert hasattr(self.config, "name") and isinstance(self.config.name, str)


if __name__ == "__main__":
    unittest.main()

# EOF