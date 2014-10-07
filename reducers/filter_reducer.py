import sys
import CSV_IO as csvio

if len(sys.argv) == 4:
  field = int(sys.argv[1])
  #operation = sys.argv[2]
  value = sys.argv[2]

  csv_reader = csvio.UnicodeReader(sys.stdin)
  csv_writer = csvio.UnicodeWriter(sys.stdout)

  #WRITE HEADER
  csv_writer.writerow(csv_reader.next())

  for row in csv_reader:
    if row[field] == value:
      csv_writer.writerow(row)

else:
  print '''This script is a simple CSV filter (by equality) reducer, meaning:
           (1) reads a CSV file from STDIN;
           (2) tests for some field's property;
           (3) prints to STDOUT the lines that passed the test.
           INPUT: field_index value (where indexes starts by 0)'''
