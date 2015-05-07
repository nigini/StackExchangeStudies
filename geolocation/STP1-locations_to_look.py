import sys

def build_locations_map(locations_file_name):
  locations = {}
  with open(locations_file_name,'r') as known_locations:
    for line in known_locations:
      line_split = line.split(':')
      if len(line_split) == 2:
        location = line_split[0].strip() 
        country = line_split[1].strip()
        locations[location] = country
  return locations

if len(sys.argv) == 3:
  known_locations = build_locations_map(sys.argv[1])
  
  with open(sys.argv[2],'r') as locations_to_look:
    for line in locations_to_look:
      location = line.split(':')[0].strip()
      if location not in known_locations:
        print location

else:
  print('''Please give me two files: \n
           the known_locations (LOCATION:COUNTRY) and \n
           the toknow_locations (LOCATION:...)''')
