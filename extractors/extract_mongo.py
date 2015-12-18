import sys
import argparse
from pymongo import MongoClient
from stack_io.extract import StackExchangeFileReader


parser = argparse.ArgumentParser(
  description='Reads specific values from a XML StackExchange dump file from STDIN and writes them in a CVS format')
parser.add_argument('--site', help='site name as in the URL - remove .COM', required=True)
parser.add_argument('--file', help='what are we reading? posts? users? - lowcaps and remove .XML', required=True, 
    choices=['badges','comments','posthistory','postlinks','posts','tags','users','votes'])
parser.add_argument('names', nargs='+', help='one or more attributes to be extracted from the XML.')
args = parser.parse_args()

reader = StackExchangeFileReader(lines=sys.stdin, attrib_names=args.names)
client = MongoClient()
db = client.stack_exchange
site = args.site
collection = db[args.file]

for value in reader.next_values():
  if value:
    value['site']=site
    collection.insert_one(value).inserted_id