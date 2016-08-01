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
COUNTRIES_PER_PAGE = 20
PREFIX = "https://www.youtube.com/watch?v="

country_pages = [
                    COUNTRIES[start_index:start_index + COUNTRIES_PER_PAGE]
                    for start_index
                    in range(0, len(COUNTRIES), COUNTRIES_PER_PAGE)
                ]
num_pages = len(country_pages)


def search(query, max_results=5):
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


def search_countries(query, page_num):
    page = country_pages[page_num] if page_num < num_pages \
                else country_pages[-1]
    results = []
    for country in page:
        youtube_query = "{} {}".format(query, country)
        results.append({'country': country,
                        'query': youtube_query,
                        'results': search(youtube_query)})
    return results
