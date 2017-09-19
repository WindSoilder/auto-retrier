import time

import requests
from requests.exceptions import ConnectionError, Timeout, HTTPError


def try_fetch_until_success(url: str, retry_times: int=0):
    ''' try to fetch url forever, until fetch success '''
    MAX_RETRY_TIMES = 1000
    try:
        response = requests.get(url)
        response.raise_for_status()
    except ConnectionError, Timeout as e:
        # default every retry by 10 seconds
        time.sleep(10)
        try_fetch_until_success(url, retry_times + 1)
    except HTTPError as e:
        if is_server_side_error(response.status_code):
            try_fetch_until_success(url, retry_times + 1)


def is_server_side_error(status_code: int) -> bool:
    ''' check if the status code indicate the error is on server side '''
    checked_error_code = set([500, 501, 502, 503, 504])
    return status_code in checked_error_code
