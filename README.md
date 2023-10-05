Prereqs:

First, you'll need to get a Consumer Key and Consumer Secret from Twitter. You'll find them in the Developer Portal:

Developer Portal -> Projects & Apps -> Overview -> Default project-XXXX

and in the Keys and tokens tab -> Consumer Keys -> API Key and Secret

Then, in your terminal, you must install the oauth lib to authenticate into the twitter api:

    $ pip3 install requests_oauthlib

Usage:

Run

    $ python3 get_access_tokens.py

You will be prompted to follow a link to do a one-time authorisation of this app (in your webbrowser - same screen you may have seen in the past if you logged into a non-Twitter app using Twitter). The output will be an access_token and access_token secret you can insert into create_tweet.py. These seem to last a long time (maybe until revoked?) so then you should be able to:

    $ python3 create_tweet.py

To tweet from code!

Next steps:

1. Hook up to Google Trends to get a topic to tweet about
2. Hook up to HuggingFace API to get a string to tweet about the topic
3. Schedule this to run once per hour from 7am EST to 11pm
