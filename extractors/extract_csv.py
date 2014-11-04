import sys
import CSV_IO as csvio
from lxml import etree

def get_attribs(row, attrib_names, parser):
  values = []
  try:
    result = etree.XML(row.strip(), parser)
  except etree.XMLSyntaxError:
    pass
  else:
    if result.tag == 'row':
      for attrib in attrib_names:
        if attrib in result.keys():
          values.append(result.attrib[attrib])
        else:
          values.append('')
  return values

if len(sys.argv) >= 2:
  parser = etree.XMLParser()
  attribs_num = len(sys.argv)-1
  attrib_names = sys.argv[-attribs_num:]

  csv_writer = csvio.UnicodeWriter(sys.stdout)
  #Printing HEADER
  csv_writer.writerow(attrib_names)
  #Printing DATA
  for line in sys.stdin:
    values = get_attribs(line, attrib_names, parser)
    if len(values)==attribs_num:
      csv_writer.writerow(values)
else:
  print '''This script is a basic data extractor to StackExchange\'s XML dumpfiles.
           INPUT: a space sepated list of attributes to be extracted from the XML 
                  (the XML is readed from STDIN)
           OUTPUT: attributes on a CSV formatted line-by-line in the STDOUT.'''
