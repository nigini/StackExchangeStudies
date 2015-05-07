import sys

def build_known_locations(file_stream):
  locations = dict()
  for line in file_stream:
    line_split = line.split(':')
    location = ':'.join(line_split[0:-1]).strip()
    locations[location] = line_split[-1].strip()
  return locations
  
if len(sys.argv) == 3:
  known_locations_file = open(sys.argv[2],'r')
  known_locations = build_known_locations(known_locations_file)
  known_locations_file.close()

  users = open(sys.argv[1],'r')
  for user in users:
    user_splits = user.split(',')
    if len(user_splits)>1:
      user_loc = ','.join(user_splits[1:]).strip().strip('\"')
      if not (user_loc == ''): #user have location info
        user_id = user_splits[0].strip().strip('\"')
        try:
          user_country = known_locations[user_loc]
          print '''\"{}\",\"{}\"'''.format(user_id,user_country)
        except KeyError:
          pass

  users.close()
else:
  print('''Please give me two files: \n
           the users_location (ID,LOCATION) and \n
           the known_locations (LOCATION:COUNTRY)''')
