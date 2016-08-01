import config
import countries
import time
from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser

YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
DEVELOPER_KEY = config.API_KEY
COUNTRIES = countries.COUNTRIES
PREFIX = "https://www.youtube.com/watch?v="


def youtube_search(query, max_results=5):
    youtube = build(YOUTUBE_API_SERVICE_NAME,
                    YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)

    return youtube.search().list(
        q=query,
        part="id,snippet",
        type='video',
        order='rating',
        maxResults=max_results,
    ).execute()

def youtube_search_countries(query):
    results = []
    for country in COUNTRIES:
        youtube_query = "{} {}".format(query, country)
        results.append({'country': country,
                        'query': youtube_query,
                        'results': youtube_search(youtube_query)})
    return results
