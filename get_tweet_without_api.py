# -*- coding: utf-8 -*-
"""
"""

from twitter_scraper import get_tweets
import pandas as pd
import os

user_name = os.environ['USERPROFILE'].replace('\\', '/')

tweet_list = [tweet for tweet in get_tweets('アカウントID', pages=1)]

df_sep = pd.io.json.json_normalize(tweet_list, sep='-')
df_sep.to_excel(user_name + '/Desktop/tweet.xlsx', index = None)
