from instapy import InstaPy
from instapy import smart_run

insta_username=''
insta_password=''

session=InstaPy(insta_username,
                insta_password,
                headless_browser=True)

with smart_run(session):
    session.set_relationship_bounds(enabled=True,
                                    potency_ratio=2.5,
                                    delimit_by_numbers=True,
                                    min_posts=10,
                                    min_followers=100,
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
                                peak_likes_daily=100,
                                peak_follows_daily=100,
                                peak_comments_daily=100,
                                peak_server_calls_daily=3600)

    session.like_by_feed(amount=10, randomize=True, interact=True, unfollow=False)
    session.like_by_tags(['tiktokindo','snackvideoindonesia'], amount=100, randomize=True)
    session.follow_by_tags(['tiktokindo'], amount=100, randomize=True)