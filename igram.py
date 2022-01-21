import igramscraper
from igramscraper.instagram import Instagram
from up import username, password
import time
from time import sleep
import datetime
import os
from os import path
import ast



def unfollowers(current, old):
    return list(set(old) - set(current))


limit = 10 ** 5

running = True
while running:
    try:
        instagram = Instagram()
        instagram.with_credentials(username, password)
        instagram.login(force=False, two_step_verificator=True)
        time.sleep(2)
        account = instagram.get_account("enter the account you wanna monitor")
        followers = instagram.get_followers(account.identifier, limit, 100, delayed=True)
        current_followers = []
        now = datetime.datetime.now()
        now = now.strftime("%b %d, %Y - %H:%M:%S")

        for follower in followers:
            current_followers.append(follower.username)
        if not path.exists('followers.txt'):
            f = open('followers.txt', 'w')
            f.write(current_followers)
            f.close()
        else:
            f = open('followers.txt', 'r+')
            old_followers = f.read()
            f.close()
            old_followers = ast.literal_eval(old_followers)
            unfollowers(current_followers, old_followers)
            change = len(old_followers) - len(current_followers)
            follow_count = len(followers)
            unfollowers_count = len(unfollowers)
            f = open('followers.txt', 'w')
            f.write(current_followers)
            f.close()
        print(unfollowers_count)
    except KeyboardInterrupt:
        print("exiting")
    except Exception as e:
        print(e)
    sleep(3600)

