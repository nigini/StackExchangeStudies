Example 2: Post's Editors
===================

Now we're interested in knowing who are the users how edits posts. This is important because maybe
this is related to emerging admin behavior.

First of all we'll need to download the site's 'PostHistory.xml' file (which is a huge file when
considering StackOverflow). Again you can use the first 1000 lines made available in 'examples' 
folder. This file contains data related to every change in each post, including user, timestamp,
what type of change, and sometimes even the post's content. Basically we're going to extract needed
columns, filter the entries by type of change, and then count.

Let's do it (Remember to set you environment as specified in the main example's page!):

  1. In this case, we will only need the following information: "UserId","Id","PostHistoryTypeId"!
As demonstrated in the first example we can extract these columns using the following command:
    1. python extractors/extract_csv.py UserId Id PostHistoryTypeId 
                < examples/so_201409_postshistory_1000.xml 
                > examples/so_postshistory.csv
    1. now you have the needed data in a CSV format.
  1. Considering the metadata information on PostHistory - available HERE: 
https://archive.org/download/stackexchange/readme.txt - you'll see that "PostHistoryTypeId=5"
refers to post's text edition. So lets filter our data consideting that. To do so, we'll use
a filter reducer, capable of comparing the value of a column with a given value and print only
those which are OK:
    1. execute: python reducers/filter_reducer.py 2 value:5 EQ 
                       < examples/so_postshistory.csv 
                       > examples/so_posts_bodyeditors.
    1. now you have a CSV file with only those post modifications related to body text editions.

If you want to know who are the users that made them you can use the count_reducer as explained
in the Example 1.
