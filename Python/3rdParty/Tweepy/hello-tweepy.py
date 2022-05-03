#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import Union
from pathlib import Path

import yaml

import tweepy


def read_twitter_credentials(filename: Union[str,Path]) -> str:
    if isinstance(filename, str):
        filename = Path(filename)
    filename = filename.expanduser()
    if not filename.exists():
        raise ValueError(f"file {str(filename)} not found")
    try:
        with filename.open() as stream:
            return yaml.safe_load(stream)
    except:
        return None


if __name__ == "__main__":
    credentials = read_twitter_credentials("~/Documents/Config/twitter-credentials.yml")
    if not credentials:
        raise RuntimeError("Can't get the bearer token")

    bearer_token = credentials.get("bearer_token")
    client = tweepy.Client(bearer_token)
    for tweet in tweepy.Paginator(client.search_recent_tweets, "#Russia",
            max_results=100).flatten(limit=250):
        print(tweet.id, tweet.text)

# EOF
