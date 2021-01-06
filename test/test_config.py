import os
import unittest
import argparse
from monitor.controllers import ConfigHandler


class TestConfig(unittest.TestCase):

    def test_config(self):
        args = argparse.Namespace()
        args.config_file =  os.path.abspath(os.getcwd() + "/../config.yaml")
        args.folder = ""
        args.queue_url = ""
        config: ConfigHandler = ConfigHandler(args)
        self.assertIsNotNone(config)
