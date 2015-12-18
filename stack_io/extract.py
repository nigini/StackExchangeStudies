import sys
from lxml import etree

class StackExchangeFileReader:

  def __init__(self, lines, attrib_names=[]):
    self.attrib_names = attrib_names
    self.lines = lines
    self.xml_parser = etree.XMLParser()

  def _get_attribs(self, xml_row):
    values = None
    try:
      result = etree.XML(xml_row.strip(), self.xml_parser)
    except etree.XMLSyntaxError:
      pass
    else:
      if result.tag == 'row':
        values = {}
        for attrib in self.attrib_names:
          if attrib in result.keys():
            values[attrib] = result.attrib[attrib]
          else:
            values[attrib] = None
    return values

  def next_values(self):
    for line in self.lines:
      yield self._get_attribs(line)