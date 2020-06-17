"""client bindings to query software heritage API."""

import json

import requests


class SHAPIClient:
    URL = "https://archive.softwareheritage.org/api/1/"

    def __init__(self, query, rate_limit=None, encoding="utf-8"):
        pass
