import sys
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
          values.append('\"{}\"'.format(result.attrib[attrib].encode('utf-8')))
        else:
          values.append('\"\"')
  return values

if len(sys.argv) >= 2:
  parser = etree.XMLParser()
  attribs_num = len(sys.argv)-1
  attrib_names = sys.argv[-attribs_num:]
  attrib_names_str = map(lambda x: '\"{}\"'.format(x), attrib_names)

  #Printing HEADER
  print ','.join(attrib_names_str)
  #Printing DATA
  for line in sys.stdin:
    values = get_attribs(line, attrib_names, parser)
    if len(values)==attribs_num:
      print ','.join(values)
else:
  print '''This script expects a list of Attrbutes to be extracted from a StackExchange\'s XML
           dumpfile. The XML itself will be received in the STDIN and the OUTPUT will be printed
           line by line in the STDOUT.'''
