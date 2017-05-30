import os
import sys
import json

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

import unittest
import meterbus
from meterbus.exceptions import *


class TestSequenceFunctions(unittest.TestCase):
    def setUp(self):
        self.frame = "\x68\x03\x03\x68\x08\x0b\xFF\x16"

    def test_json(self):
        hdr = meterbus.TelegramHeader()
        hdr.load(self.frame)
        jd = json.loads(hdr.to_JSON())

        with self.subTest():
            self.assertEqual(jd['start'], "0x68")
        with self.subTest():
            self.assertEqual(jd['stop'], "0x16")
        with self.subTest():
            self.assertEqual(jd['length'], "0x3")
        with self.subTest():
            self.assertEqual(jd['a'], "0xb")
        with self.subTest():
            self.assertEqual(jd['crc'], "0xff")

if __name__ == '__main__':
    unittest.main()