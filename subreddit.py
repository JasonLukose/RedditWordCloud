
import praw
import logging


class SubredditDataCollection(object):
    
    def __init__(self, sub_name):
        self.userAgent = "Subreddit Sentiment Analysis Data Collection"
        self.submissionLimit = 1000
        self.subredditName = sub_name

    def setup(self):
        self.redditInstance = praw.Reddit('ssa', user_agent=self.userAgent)
    
    

    

if __name__ == "__main__":
    ssabot = SubredditDataCollection('classsetup')
    ssabot.setup()
    print(ssabot.subredditName)
