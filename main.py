import json

FOLLOWERS = 'followers_1.json'
FOLLOWING = 'following.json'

parsed_followers = []

with open(FOLLOWERS) as ers:
    loaded_followers = json.load(ers)
    for follower in loaded_followers:
        parsed_followers.append(follower["string_list_data"][0]["value"])

with open(FOLLOWING) as ing:
    loaded_following = json.load(ing)
    for followed in loaded_following["relationships_following"]:
        followed_username = followed["string_list_data"][0]["value"]
        if followed_username not in parsed_followers:
            print('{} does not follow you back!'.format(followed_username))