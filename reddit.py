#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import praw
from dotenv import load_dotenv
import pprint

from flask import Flask, request, jsonify


load_dotenv()

# reddit = praw.Reddit("mybot", user_agent="mybot v0.1")

# pprint.pprint(reddit)


# TAGS = os.getenv('tags').split()


# def filter_by_tags(posts, tags=TAGS):
#     return [post for post in posts 
#             if any(tag in post.title.lower() for tag in tags)]


def authenticate():
    return praw.Reddit("mybot", user_agent="mybot v0.1")


def get_posts(reddit):
    posts = reddit.subreddit(os.getenv('sub'))
    # posts = filter_by_tags(posts)
    return posts


# def main():
#     reddit = authenticate()
#     subs = get_posts(reddit)
#     x = subs[0]
#     import pprint
#     pprint.pprint(x.url)


# if __name__ == '__main__':
#     main()

# reddit = authenticate()
# subs = get_posts(reddit)


# # subs_read = [sub.title for sub in subs if not sub.stickied]
# pprint.pprint(dir(subs))

app = Flask(__name__)
@app.route('/')
def reddit_request():
    reddit = authenticate()
    subreddit = get_posts(reddit)

    # pprint.pprint(dir(subreddit.stream.submissions))
    
    # subs_read = [sub.title for sub in subs.stream if not sub.stickied]
    for submission in subreddit.stream.submissions():
        try: 
            pprint.pprint(submission.title.lower())
        except Exception as e:
            pass

    return jsonify(coms)

if __name__ == '__main__':
    app.run()