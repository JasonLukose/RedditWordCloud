
import sys
import praw
from prawcore.exceptions import NotFound 
from praw.exceptions import ClientException

class SubredditAccess(object):
    
    def __init__(self, sub_name):
        self.subredditName = sub_name.replace(' ', '')
        self.userAgent = "Subreddit Sentiment Analysis for /r/" + self.subredditName
        self.submissionLimit = 1000

    def setup(self):
        self.redditInstance = praw.Reddit('ssa', user_agent=self.userAgent)
        self.access_sub()
 
    def access_sub(self):
        self.validate_sub()
        if (self.validSub):
            self.subreddit = self.redditInstance.subreddit(self.subredditName)    
        else:
            sys.exit(1) # Not necessary, remove later
    
    def validate_sub(self):
        self.validSub = False
        try:
            response = self.redditInstance.subreddits.search_by_name(self.subredditName, exact=True)
            if len(response) == 0:
                raise ClientException("Invalid input, must not be empty")
            else:
                self.validSub = True ## Only valid here, must not throw any Exception and must not be empty input
        except NotFound as e:
            self.validSub = False
            print("This subreddit does not exist, make sure you input a valid subreddit")
            sys.exit(1)
        except Exception as e:
            print("Unexpected Error Occurred")
            raise
