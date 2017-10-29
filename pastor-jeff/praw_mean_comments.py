import praw
import random
reddit = praw.Reddit(client_id='EaHE4-kuS8fBDg',
                     client_secret='PMn0IOihfoCjYnYk7U8tXNTmhMc',
                     user_agent='desktop:com.example.myredditapp:v1.2.3 (by /u/PM-MEAN-COMMENTS)')
#initialize praw's Reddit instance, script is on account u/PM-MEAN-COMMENTS

def fetch_mean_comments(sub,num_comments,num_posts,sampleSize):
	"""Fetch mean comments using our reddit instance"""
	sample = []
	for submission in reddit.subreddit(sub).hot(limit=num_posts):
		if submission.num_comments > 0:
			submission.comments.replace_more(limit=100)
			submission.comment_sort='controversial'
			#allow to use body attribute
			mean_comments = list(submission.comments)
			#organizes mean comments to index
			for i in range(num_comments):
				sample.append(mean_comments[(i-1)%(len(mean_comments))].body)
				#appends each body of each comment to the larger scope mean_list
		else:
			continue
	random_num = random.randrange(0,len(sample)-sampleSize)
	#generates a random index that has at LEAST SampleSize	more elements in the list
	return sample[random_num:(random_num+sampleSize)]
print("".join(fetch_mean_comments("roastme",100,20,5)))
