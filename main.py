import praw
import pprint
#reddit = praw.reddit()

client_id = 'B8guQR51y7kPcg'
client_secret = 'PqJZZIK7FRBCMuwWQkSzQ1DXiqQ'
user_agent = 'kip'

reddit = praw.Reddit(client_id = client_id,
			client_secret = client_secret,
			user_agent = user_agent)
# pprint.pprint(vars(reddit))
random = reddit.random_subreddit().display_name
print('<----> {} <---->'.format(random))
for submission in reddit.subreddit(random).hot(limit=10):
	if not submission.stickied:
		# pprint.pprint(vars(submission))
		print('Author: ---> {}, Title: ---> {}, Upvotes: ---> {}, url: ---> {}, permalink: --> https://www.reddit.com{}'
			.format(submission.author, submission.title, submission.ups, submission.url, submission.permalink))
		# print([coms for coms in list(submission.comments)])
	