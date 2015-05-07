from geopy import geocoders
from time import sleep
import sys, conf, traceback

# Uses a geocoder from geopy library to search for a location
# and return the first entry in a dictionary with (loc, lat, lon)
def get_location(location_str, geolocator):
  query_result = geolocator.geocode(location_str.encode('utf-8'), exactly_one=False)
  result = dict()
  if len(query_result) > 0:
    result['loc'] = query_result[0][0]
    result['lat'] = query_result[0][1][0]
    result['lon'] = query_result[0][1][1]
  else:
    result = None
  return result

# MAIN
geocoder = geocoders.GoogleV3()
#geocoder = geocoders.MapQuest(conf.MAPQUEST_KEY)
count = 0

if len(sys.argv) == 4:
  locations = open(sys.argv[1],'r')
  start = int(sys.argv[2])
  how_many = int(sys.argv[3])

  for i, line in enumerate(locations):
    if (i+1 >= start) and (count < how_many):
      location = line.strip().decode('utf-8')
#      if location not in known_locations:
      count += 1
      sleep(0.1)
      try:
        #todo(NIGINI): this should be a "LOCATION:COUNTRY" result and be added to known_locations
        geolocation = get_location(location, geocoder)
        if geolocation is not None:
          print 'SUCCESS : {} : {} : {} : {}'.format (location.encode('utf-8'), 
            geolocation['loc'].encode('utf-8'), geolocation['lat'], geolocation['lon'])
        else:
          print 'FAILED : {}'.format(location.encode('utf-8'))
      except Exception, e:
        print 'ERROR : {}'.format(location.encode('utf-8'))
        print traceback.format_exc()
else:
  print '''Please provide the following parameters: 
           (1) FILE_TO_SEARCH with a location string per line, 
           (2) the line from where I have to start considering FILE_TO_SEARCH and 
           (3) how many lines I should try to resolve.'''
