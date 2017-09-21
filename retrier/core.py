import time
import logging
from urllib import parse

import requests
from requests.exceptions import ConnectionError, Timeout, HTTPError


def try_fetch_until_success(url: str, retry_times: int=0) -> bool:
    ''' try to fetch url forever, until fetch success '''
    MAX_RETRY_TIMES = 1000

    if retry_times > MAX_RETRY_TIMES:
        logging.warn("try to max {retry} times,"
                     " but still can't access the page."
                     .format(retry=MAX_RETRY_TIMES))
        return False
    try:
        url = ensure_scheme(url)
        response = requests.get(url)
        response.raise_for_status()
        return True
    except (ConnectionError, Timeout) as e:
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


def ensure_scheme(url: str) -> str:
    ''' ensure the url contains scheme '''
    parsed = parse.urlparse(url)
    if parsed.scheme == "":
        # add default scheme(http) to url
        final_url = "".join(["http://", url])
    else:
        final_url = url
    return final_url
