from requests_oauthlib import OAuth1Session
import os
import json

# insert your keys here - the ones under:
# Developer Portal -> Projects & Apps -> Overview -> Default project-XXXX
# and in the Keys and tokens tab -> Consumer Keys -> API Key and Secret
consumer_key = ''
consumer_secret = ''

# Then, insert values from get_access_tokens.py:
access_token = '' # the access_token: value from get_access_tokens
access_token_secret = '' # the access_token_secret: value from get_access_tokens

# Be sure to add replace the text of the with the text you wish to Tweet. You can also add parameters to post polls, quote Tweets, Tweet with reply settings, and Tweet to Super Followers in addition to other features.
payload = {"text": "i am making a new tweet"}

# Make the request
oauth = OAuth1Session(
    consumer_key,
    client_secret=consumer_secret,
    resource_owner_key=access_token, #access_token,
    resource_owner_secret=access_token_secret,
)

# Making the request
response = oauth.post(
    "https://api.twitter.com/2/tweets",
    json=payload,
)

if response.status_code != 201:
    raise Exception(
        "Request returned an error: {} {}".format(response.status_code, response.text)
    )

print("Response code: {}".format(response.status_code))

# Saving the response as JSON
json_response = response.json()
print(json.dumps(json_response, indent=4, sort_keys=True))
