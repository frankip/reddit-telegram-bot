#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import praw
from dotenv import load_dotenv

from flask import Flask, request, jsonify

load_dotenv()
def authenticate():
    return praw.Reddit("mybot", user_agent="mybot v0.1")


def get_posts(reddit):
    posts = reddit.subreddit(os.getenv('sub'))
    # posts = filter_by_tags(posts)
    return posts


# app = Flask(__name__)
# @app.route('/')
# def reddit_request():
def main():
    reddit = authenticate()
    subreddit = get_posts(reddit)
    for submission in subreddit.stream.submissions():
        try:
            subs = {
                # "Author":submission.author.name,
                "Title":  submission.title,
                "media": submission.url,
                "link":  f'https://www.reddit.com{submission.permalink}'
            }

            print(subs)

        except Exception as e:
            print(str(e))

if __name__ == '__main__':
    # app.run()
    main()