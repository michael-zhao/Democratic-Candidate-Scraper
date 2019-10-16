import praw
import pandas as pd
import datetime as dt
import top_posts_in_subreddit as top_posts

def main():
    my_account = top_posts.RedditAccount() #only cnmb for now
    reddit = my_account.get_auth()

# all names for candidates, including:
# PB: Pete, Buttigieg, Pete Buttigieg
# EW: Warren, Elizabeth, Elizabeth Warren
# 
pete_dict = {
    "Pete": 0,
    "Buttigieg": 0,
    "Pete Buttigieg": 0,
}

warren_dict = {
    "Warren": 0,
    "Liz": 0,
    "Elizabeth Warren": 0,
}

yang_dict = {
    "Yang": 0,
    "Andrew Yang": 0,
}

bernie_dict = {
    "Bernie": 0,
    "Sanders": 0,
    "Bernie Sanders": 0,
}

biden_dict = {
    "Joe": 0,
    "Biden": 0,
    "Joe Biden": 0,
}

trump_dict = {
    "Trump": 0,
    "Donald Trump": 0,
}

kamala_dict = {
    "Kamala": 0,
    "Harris": 0,
    "Kamala Harris": 0,
}

pete_sub = reddit.subreddit('Pete_Buttigieg')
top_pete = pete_sub.top(limit=1000)

# function to check comments for mentions of Pete Buttigieg and any relevant keywords
def check_pete(comment):
    # for each keyword for Pete, check if any words in the comment match
    # if there is a match, the value (count) for the keyword increments
    for keyword in pete_dict.keys():
        for word in comment.split():
            if keyword == word:
                pete_dict[keyword] += 1

# comment.body is a string
for post in top_pete:
    for comment in post.comments.list():
         check_pete(comment.body)

main()
