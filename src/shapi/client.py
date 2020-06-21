"""client bindings to query software heritage API."""
import logging
import os
import sys
from functools import lru_cache

import requests
from requests.utils import quote

logger = logging.getLogger("SHClient")
logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))


class SHClient:

    URL = "https://archive.softwareheritage.org/api/1/"

    def __init__(self, rate_limit=None):
        self.rate_limit = rate_limit
        self.session = self._init_session()

    def _init_session(self):
        return requests.Session()

    def _form_url(self, path: str) -> str:
        return self.URL + quote(path)

    def _handle_response(self, response):
        if response.status_code == 429:
            logger.error("API request throttled, try again later.")
            sys.exit(1)
        elif response.status_code == 404:
            logger.error("API call triggered a bad request")
        elif response.status_code == 301:
            logger.error("API URL moved, check the URL")
            sys.exit(1)
        return response

    def _send_request(
        self, method: str, path: str, params: str = None, data=None, headers=None
    ):
        url = self._form_url(path)
        req = self.session.request(
            method=method, url=url, params=params, data=data, headers=headers
        )
        return req

    @lru_cache()
    def query(self, method, path, params=None, data=None, headers=None):
        req = self._send_request(method, path)
        resp = self._handle_response(req)
        return resp.json()
