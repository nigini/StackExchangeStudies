import unittest
from stack_io.extract import StackExchangeFileReader

class TestStackExchangeFileReader(unittest.TestCase):

  def setUp(self):
    mock_xml_file = [
      '﻿<?xml version="1.0" encoding="utf-8"?>',
      '<posts>',
      '<row Id="1" PostTypeId="1" AcceptedAnswerId="7" />',
      '<row Id="2" PostTypeId="2" ParentId="1" />'
    ]
    self.reader = StackExchangeFileReader(lines=mock_xml_file, attrib_names=['Id','ParentId'])

  def test_extract(self):
    values = self.reader.next_values()
    value = next(values)
    self.assertIsNone(value)
    value = next(values)
    self.assertIsNone(value)

    value = next(values)
    self.assertEqual(2,len(value))
    self.assertEqual('1',value['Id'])
    self.assertEqual(None,value['ParentId'])

    value = next(values)
    self.assertEqual(2,len(value))
    self.assertEqual('2',value['Id'])
    self.assertEqual('1',value['ParentId'])

    self.assertRaises(StopIteration, next, values)

if __name__ == '__main__':
  unittest.main()
