
import sys
import praw
import config
from prawcore.exceptions import NotFound
from praw.exceptions import ClientException


class SubredditAccess(object):

    def __init__(self, sub_name):
        self.SUBREDDIT_NAME = sub_name.replace(' ', '')
        self.USER_AGENT = "Subreddit Sentiment Analysis v0.1.0 for /r/" + self.SUBREDDIT_NAME
        self.SUBMISSION_LIMIT = 1000
        self.VALID_SUB = False
        self.REDDIT_INSTANCE = praw.Reddit(username=config.username,
                                           password=config.password,
                                           client_id=config.client_id,
                                           client_secret=config.client_secret,
                                           user_agent=self.USER_AGENT)
        self.SUBREDDIT = None
 
    def access_sub(self):
        self.validate_sub()
        if self.VALID_SUB:
            self.SUBREDDIT = self.REDDIT_INSTANCE.subreddit(self.SUBREDDIT_NAME)
            return self.SUBREDDIT
        else:
            sys.exit(1)  # Not necessary, remove later
    
    def validate_sub(self):
        self.VALID_SUB = False
        try: 
            response = self.REDDIT_INSTANCE.subreddits.search_by_name(self.SUBREDDIT_NAME, exact=True)
            if len(response) == 0:
                raise ClientException("Invalid input, must not be empty")
            else:
                self.VALID_SUB = True  # Only valid here, must not throw any Exception and must not be empty input
        except NotFound:
            self.VALID_SUB = False
            print("This subreddit does not exist, make sure you input a valid subreddit")
            sys.exit(1)
        except Exception:
            print("Unexpected Error Occurred")
            raise
