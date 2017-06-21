# MemeCollector
A script to collect all memes from given subReddits.

Add new subreddits in list, add number of posts to ignore in each subreddit, and add the number of memes to download

The memes image title starts with a random digit. To order by popularity, sort by date, and to randomize, order by title.

At start of execution, cleans all memes from the target folder. After, gets all memes from both top and new section of subreddit, and puts then in respective folder.



#install PRAW
pip install praw

#run
python memes.py
