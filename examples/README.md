StackExchangeStudies
====================

This is a project to support studies based on the StackExchange dump data.

Let's try an example: Pretend you're interested in knowing how many posts a user made in a site.
To know that you'll make use to the site's 'Post.xml' file. For now we'll will make use of a piece 
of StackOverflow's file (the first 1000 lines) that is available in 'examples' folder. 
  1. Make sure you're in project's root directory;
  1. Set the PYTHONPATH to ".:./resources/";
  1. Now we can use of our simplest tool: the attributes extractor. XML are complicated files, and
each StackExchange's file have a lot of data that will not be used in each of our analysis. In this
case, we will only need one information, the 'OwnerUserId', but just to show that it is possible,
we'll extract, for each line of out example file the post's owner and the post's id.
    1. execute: python extractors/extract_csv.py OwnerUserId Id < examples/so_201405_posts_1000.xml 
                > examples/so_users_posts.csv
    1. now you have the needed data in a CSV format.
  1. but we need more than that, we want to count how many times each user appears in that file,
because this is exactly the amount of posts he/she produced. We have just that tool: the counter
reducer. This scripts takes only the first attribute in a csv file and counts how many times it
exists in a file. Actually, this is a pretty common data analysis task:
    1. execute: python reducers/count_reducer.py < examples/so_users_posts.csv 
                > examples/so_users_numposts.csv 
    1. now you have a CSV file containing tuples like (user_id,num_posts) in CSV format
    1. OBS: some users that removed their account have their id removed from 'Posts', so you'll find
an entry like this: "","19", meaning that there were 19 posts that have no users to be attributed.

This is just an example, right. But now you can easily extract and play with StackExchange's site
data. Search for the documentation/examples for each available script to know more.

Have fun!
  
