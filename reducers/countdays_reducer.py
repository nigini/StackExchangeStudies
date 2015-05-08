import sys
import CSV_IO as csvio
from datetime import datetime

if len(sys.argv) == 2:
  csv_reader = csvio.UnicodeReader(sys.stdin)
  csv_writer = csvio.UnicodeWriter(sys.stdout)
  #base_date = datetime.strptime(sys.argv[1],'%Y-%m-%d')
  timestamp_index = int(sys.argv[1])

  #deal with header
  header = csv_reader.next()
  header.append(u'NUM_DAYS')
  csv_writer.writerow(header)
  #deal with first line
  row = csv_reader.next()
  base_date = datetime.strptime(row[timestamp_index],'%Y-%m-%dT%H:%M:%S.%f').date()
  row.append(str(0))
  csv_writer.writerow(row)
  #deal with the rest of the file
  for row in csv_reader:
    new_date = datetime.strptime(row[timestamp_index],'%Y-%m-%dT%H:%M:%S.%f').date()
    diff = new_date-base_date
    row.append(str(diff.days))
    csv_writer.writerow(row)

else:
  print '''This script counts the days passed from a BASE_DATE, for each line in the data. 
           The BASE_DATE is the DATE found in the first line in STDIN:
           (1) reads a CSV file from STDIN;
           (2) gets a COLUMN_INDEX from the CSV that contains a TIMESTAMP (starts in 0)
           (3) prints to STDOUT each line with an added NUM_DAYS column in CSV format.'''
