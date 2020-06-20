"""client bindings to query software heritage API."""
import logging
import os
import sys
from urllib.parse import urlencode

import requests
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
        return self.URL + path

    def _handle_response(self, response):
        print(response.status_code)
        if response.status_code == 404:
            logger.info("API call triggered a bad request")
            sys.exit(1)
        return response

    def _send_request(
        self, method: str, path: str, params: str = None, data=None, headers=None
    ):
        url = self._form_url(path)
        logger.info(url)
        req = self.session.request(
            method=method,
            url=url,
            params=params,
            data=data,
            headers=headers
        )
        return req

    def query(self, method, path, params=None, data=None, headers=None):
        req = self._send_request(method, path)
        return self._handle_response(req)
