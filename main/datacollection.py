#!/usr/bin/python3

import sys
import praw
import time
import config
from prawcore.exceptions import Forbidden, NotFound
from subaccess import SubredditAccess


class DataCollection(object):

    def __init__(self):
        self.USER_AGENT_URL = "Subreddit Word Cloud and Sentiment Analysis v0.1.0 for submission URLs"
        self.OUTPUT_FILE = open("data1.txt", "w+")

    def access_submissions_sub(self, subreddit_name, submission_limit=1000, comment_replace_limit=1, skip_sticky=True):
        subreddit_name = subreddit_name.replace(' ', '')
        reddit_instance = SubredditAccess(subreddit_name)
        subreddit = reddit_instance.access_sub()

        try:
            count = 1
            for submission in subreddit.hot(limit=submission_limit):
                if skip_sticky and submission.stickied:  # Hacky, should add submission_limit to meet input
                    continue
                else:
                    self.process_submission(submission, comment_replace_limit, count)
                    count = count + 1

        except Forbidden:
            print("You do not have access to this sub!")
            print("Printing Traceback now...")
            time.sleep(1)  # Not required, just here for simple pause before traceback
            raise
        except Exception:
            print("Unexpected Error Occurred while accessing submissions")
            raise

    def access_submission_url(self, submission_url, comment_replace_limit=10):
        reddit_instance = praw.Reddit(username=config.username, password=config.password,
                                      client_id=config.client_id, client_secret=config.client_secret,
                                      user_agent=self.USER_AGENT_URL)

        submission = reddit_instance.submission(url=submission_url)
        try:
            self.process_submission(submission, comment_replace_limit)
        except NotFound:
            print("This submission cannot be found, make sure the id matches!")
            time.sleep(0.5)
            raise

    def process_submission(self, submission, comment_replace_limit=1, count=1):
        print("Starting processing on submission {}".format(count))
        if submission.is_self:
            self.OUTPUT_FILE.write(submission.selftext)
            self.OUTPUT_FILE.write(submission.title)
        else:
            self.OUTPUT_FILE.write(submission.title)

        count = 0
        submission.comments.replace_more(limit=comment_replace_limit)
        for comment in submission.comments.list():
            count = count + 1
            self.OUTPUT_FILE.write(comment.body)
        print("Number of comments processed for this submission: {}".format(count))


if __name__ == "__main__":
    dc = DataCollection()
    dc.access_submissions_sub("gatech", 1000)

