import sys
import argparse
import csv
from stack_io.extract import StackExchangeFileReader


parser = argparse.ArgumentParser(
  description='Reads specific values from a XML StackExchange dump file from STDIN and writes them in a CVS format')
parser.add_argument('--out', help='output CSV file name') 
parser.add_argument('names', nargs='+', help='one or more attributes to be extracted from the XML.')
args = parser.parse_args()

reader = StackExchangeFileReader(lines=sys.stdin, attrib_names=args.names)
if args.out:
  csvout = open(args.out,'w')
else:
  csvout = sys.stdout

writer = csv.DictWriter(csvout, fieldnames=args.names)
writer.writeheader()

for value in reader.next_values():
  if value:
    writer.writerow(value)