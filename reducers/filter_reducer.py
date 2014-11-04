import sys
import CSV_IO as csvio

if len(sys.argv) == 4:
  field = int(sys.argv[1])
  values = sys.argv[2].split(':')
  value = values[1]
  operation = sys.argv[3]

  csv_reader = csvio.UnicodeReader(sys.stdin)
  csv_writer = csvio.UnicodeWriter(sys.stdout)

  #WRITE HEADER
  csv_writer.writerow(csv_reader.next())

  for row in csv_reader:
    if values[0] == 'index':
      value = row[int(values[1])]

    #APPLY OPERATION
    test = False
    if operation == 'DIF':
      test = row[field] != value
    else: #DEFAULT is EQ
      test = row[field] == value

    if test:
      csv_writer.writerow(row)

else:
  print '''This script is a simple CSV filter reducer, meaning:
           (1) reads a CSV file from STDIN;
           (2) tests for some field's property;
           (3) prints to STDOUT the lines that passed the test.
           INPUT: field_index {value:number OR index:value} operation {= EQ or DIF}
                  (where indexes starts by 0)'''
