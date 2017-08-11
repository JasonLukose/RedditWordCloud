#!/usr/bin/python3

import sys
import praw
import time
from prawcore.exceptions import Forbidden
from subaccess import SubredditAccess

class DataCollection(object):

    def __init__(self, sub_name):
        self.subreddit = SubredditAccess(sub_name).setup()
        self.submissionLimit = 1000

    def access_submissions(self):
        try:
            for submission in self.subreddit.hot(limit=10):
                print(type(submission.selftext))
        except Forbidden:
            print("You do not have access to this sub!")
            print("Printing Traceback now...")
            time.sleep(1)
            raise



if __name__ == "__main__":
    dc = DataCollection("AskReddit")
    print(dc.subreddit)
    dc.access_submissions()
