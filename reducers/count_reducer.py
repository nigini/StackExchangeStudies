import sys
import CSV_IO as csvio

if len(sys.argv) == 1:
  csv_reader = csvio.UnicodeReader(sys.stdin)
  csv_writer = csvio.UnicodeWriter(sys.stdout)

  count_map = {}
  for row in csv_reader:
    if row[0] in count_map:
      count_map[row[0]]=count_map[row[0]]+1
    else:
      count_map[row[0]]=1

  for key in count_map.keys():
    csv_writer.writerow([key,str(count_map[key])])

else:
  print '''This script is a simple CSV count reducer, meaning:
           (1) reads a CSV file from STDIN;
           (2) counts the number of times each value in the first CSV field appears;
           (3) prints to STDOUT a tuple (field,count) in CSV format.'''
