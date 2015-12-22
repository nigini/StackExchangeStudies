from pymongo import MongoClient

def count_posts(db,posttype,tablename):
  pipeline = [
    {'$match' : {'PostTypeId':posttype}},
    {'$group' : {'_id': {'site':'$site','user':'$OwnerUserId'}, 
                 'count': {'$sum':1}}},
    {'$sort': {'_id.user' : 1}},
    {'$out': tablename}
  ]
  db['posts'].aggregate(pipeline)

def count_comments(db,tablename):
  pipeline = [
    {'$group' : {'_id': {'site':'$site','user':'$UserId'}, 
                 'count': {'$sum':1}}},
    {'$sort': {'_id.user' : 1}},
    {'$out': tablename}
  ]
  db['comments'].aggregate(pipeline)



db = MongoClient()['stack_exchange']
count_posts(db,'1','user_participation_q')
db['user_participation_q'].find_one()
db['user_participation_q'].count()

count_posts(db,'2','user_participation_a')
db['user_participation_a'].find_one()
db['user_participation_a'].count()

count_comments(db,'user_participation_c')
db['user_participation_c'].find_one()
db['user_participation_c'].count()
