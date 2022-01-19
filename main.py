from instapy import InstaPy
from up import username, password
login_id = InstaPy(username, password, headless_browser=False)
login_id.login()
login_id.unfollow_users(amount=10, nonFollowers=True, unfollow_after=1000, sleep_delay=600)
login_id.end()