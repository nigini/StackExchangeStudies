import sys
import CSV_IO as csvio

if len(sys.argv) == 5:
  second_csv = csvio.UnicodeReader(open(sys.argv[1],'r'))
  
  by_x = int(sys.argv[2])
  by_y = int(sys.argv[3])
  column_y = int(sys.argv[4])

  #build a consultation map
  second_csv_header = second_csv.next()
  consult_map = {}
  for row in second_csv:
    consult_map[row[by_y]] = row[column_y]
    
  csv_reader = csvio.UnicodeReader(sys.stdin)
  csv_writer = csvio.UnicodeWriter(sys.stdout)

  #WRITE HEADER
  main_csv_header = csv_reader.next()
  main_csv_header.append(second_csv_header[column_y])
  csv_writer.writerow(main_csv_header)

  for row in csv_reader:
    try:
      new_value = consult_map[row[by_x]]
    except KeyError:
      new_value = u''
    row.append(new_value)
    csv_writer.writerow(row)

else:
  print '''This script is a CSVs merger reducer, meaning:
           (1) reads a MAIN_CSV file from STDIN;
           (2) reads a SECOND_CSV named file to have the column to be added at MAIN_CSV;
           (3) the column (BY.X) to be compared from SOURCE_CSV;
           (4) the column (BY.Y) to be compared from SECOND_CSV;
           (5) the column from SECOND_CSV to be added at MAIN_CSV;
           (6) prints to STDOUT the lines from MAIN_CSV with the added column.
           INPUT: all column indexed starts by 0'''
