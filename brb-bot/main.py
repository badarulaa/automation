from contextlib import suppress
from pathlib import WindowsPath
from sys import path
from instapy import InstaPy
from instapy import smart_run
from instapy import set_workspace

import schedule
import time

set_workspace=('backup')

insta_username = ''
insta_password = ''

session=InstaPy(username=insta_username,
                password=insta_password,
                headless_browser=True,
                bypass_security_challenge_using='sms')

with smart_run(session):
    session.set_relationship_bounds(enabled=True,
                                    potency_ratio=None,
                                    delimit_by_numbers=True,
                                    min_posts=5,
                                    min_followers=50,
                                    min_following=50)

    session.set_skip_users(skip_private=True,
                            private_percentage=100,
                            skip_business=False,
                            skip_non_business=False,
                            skip_no_profile_pic=True,
                            business_percentage=100)

    session.set_quota_supervisor(enabled=True,
                                sleep_after=['likes','comments_d', 'follows'],
                                stochastic_flow=True,
                                notify_me=True,
                                peak_likes_daily=1000,
                                peak_follows_daily=1000,
                                peak_comments_daily=1000,
                                peak_server_calls_daily=3600)

    session.set_user_interact(amount=3, 
                            percentage=75, 
                            randomize=False, 
                            media='Photo')

    #session.like_by_feed(amount=10, randomize=True, interact=True, unfollow=False)
    #session.like_by_tags(['tiktokindo', 'tiktokhot', 'tiktokindonesia'], amount=50, randomize=True)
    session.follow_user_followers(['dagelan', 'crazyrichsurabayans', 'raffinagita1717'], amount=25, randomize=True, sleep_delay=300, interact=True)


