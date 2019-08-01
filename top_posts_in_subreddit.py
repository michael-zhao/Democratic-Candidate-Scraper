# fun little subreddit scraper to see how often each candidate
# is mentioned in each other's subreddits

import praw
import pandas as pd
import datetime as dt

# AUTHENTICATION #

class reddit_account(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.auth = praw.Reddit(client_id='ZSvHHWbPcTZvmQ', \
        client_secret='YcxxrJARllGxOao7O1AOvXMs8mw', \
            user_agent='candidate_subreddit_scraper', \
                username=username, \
                    password=password)
    
    def get_auth(self):
        return self.auth

# ------------------ #
# PETE BUTTIGIEG #

my_account = reddit_account("cnmb", "zhaolib1")
reddit = my_account.get_auth()
pete_sub = reddit.subreddit('Pete_Buttigieg')
top_pete = pete_sub.top(limit=1000)

pete_dict = {
    "title": [],
    "score": [],
    "id": [],
    "url": [],
    "comments_count": [],
    "created": [],
    "body": []
}

def num_to_date(date):
    return dt.datetime.fromtimestamp(date)

for submission in top_pete:
    pete_dict["title"].append(submission.title)
    pete_dict["score"].append(submission.score)
    pete_dict["id"].append(submission.id)
    pete_dict["url"].append(submission.url)
    pete_dict["comments_count"].append(submission.num_comments)
    pete_dict["created"].append(num_to_date(submission.created))
    pete_dict["body"].append(submission.selftext)

pete_data = pd.DataFrame(pete_dict)

# print(topics_data.to_string())

# --------------------------------------- #
# ELIZABETH WARREN #

warren_sub = reddit.subreddit('ElizabethWarren')
top_warren = warren_sub.top(limit=1000)

warren_dict = {
    "title": [],
    "score": [],
    "id": [],
    "url": [],
    "comments_count": [],
    "created": [],
    "body": []
}

for submission in top_warren:
    warren_dict["title"].append(submission.title)
    warren_dict["score"].append(submission.score)
    warren_dict["id"].append(submission.id)
    warren_dict["url"].append(submission.url)
    warren_dict["comments_count"].append(submission.num_comments)
    warren_dict["created"].append(num_to_date(submission.created))
    warren_dict["body"].append(submission.selftext)

warren_data = pd.DataFrame(warren_dict)