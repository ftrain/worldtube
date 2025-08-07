import config
import countries
import time
from apiclient.discovery import build
from apiclient.errors import HttpError
from apiclient.http import BatchHttpRequest
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


def search(query, max_results=5, region_code=None, youtube_service=None, execute=True):
    youtube = youtube_service or build(YOUTUBE_API_SERVICE_NAME,
                                       YOUTUBE_API_VERSION,
                                       developerKey=DEVELOPER_KEY)

    request = youtube.search().list(
        q=query,
        part="id,snippet",
        type='video',
        order='rating',
        maxResults=max_results,
        regionCode=region_code,
    )
    return request.execute() if execute else request


def search_countries(query, page_num):
    page = country_pages[page_num] if page_num < num_pages else country_pages[-1]
    youtube = build(YOUTUBE_API_SERVICE_NAME,
                    YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)

    results_by_country = {}

    def _callback(request_id, response, exception):
        results_by_country[request_id] = {
            'country': request_id,
            'query': query,
            'results': None if exception else response
        }

    batch = BatchHttpRequest(callback=_callback)
    has_requests = False

    for country in page:
        region_code = countries.COUNTRY_CODES.get(country)
        if not region_code:
            results_by_country[country] = {'country': country,
                                           'query': query,
                                           'results': None}
            continue
        req = search(query,
                     region_code=region_code,
                     youtube_service=youtube,
                     execute=False)
        batch.add(req, request_id=country)
        has_requests = True

    if has_requests:
        batch.execute()

    return [results_by_country[country] for country in page]
