"""Tests for BscExplorerUrlBuilder."""
import unittest
from main import build_url


class TestTool(unittest.TestCase):
    def test_main_function(self):
        self.assertEqual(build_url('0x2BfA103a54aeEa61c67836490d0e2A3847EA0ae3'), 'https://bscscan.com/address/0x2BfA103a54aeEa61c67836490d0e2A3847EA0ae3')


if __name__ == "__main__":
    unittest.main()
