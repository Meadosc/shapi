"""CLI entrypoint to shapi."""
import json

import click

from . import __version__
from .client import SHClient

sh_client = SHClient()


@click.group()
@click.version_option(version=__version__)
def cli() -> None:
    """SHApi - Software Heritage(SH) API.

    A Python client to interact with software heritage API
    to query for an object, upload new pkgs to the repo.
    """


def _origin_check(url: str) -> str:
    return "origin/{}/visit/latest/".format(url)


def _repo_submit(visit_type: str, url: str) -> str:
    return "origin/save/{0}/url/{1}/".format(visit_type, url)


@cli.command("check")
@click.argument("url", type=str)
def check(url: str) -> None:
    """Check if a repo url is archived in SH.

    Give the full URL of the repo hosted in git, svn etc.

    Args:
        url: repo url to check, eg: https://github.com/tensorflow/tensorflow
    """
    url = _origin_check(url)
    # TODO (unrahul): cache
    resp = sh_client.query("GET", url)
    print("=" * 71)
    print("Archive found")
    print("Date: {}".format(resp["date"]))
    print("Src URL: {}".format(resp["origin"]))
    print("Archive URL: {}".format(resp["snapshot_url"]))
    print("=" * 71)


@cli.command("submit")
@click.argument("type", type=str)
@click.argument("url", type=str)
def check(type: str, url: str) -> None:
    """Submit a repo to be archived in SH.

    Give the full URL of the repo hosted using git, svn or hg.

    Args:
        url: repo url to submit a repo, eg: https://github.com/tensorflow/tensorflow
    """
    url = _repo_submit(type, url)
    resp = sh_client.query("GET", url)
    print("=" * 71)
    print("Date: {}".format(resp[0]["save_request_date"]))
    print("Src URL: {}".format(resp[0]["origin_url"]))
    print("Save status: {}".format(resp[0]["save_request_status"]))
    print("=" * 71)

@cli.command("status_check")
def check() -> None:
    """
    API Health check.
    """
    resp = sh_client.query("GET", "ping")
    print("=" * 71)
    if resp == "pong":
        print("SH API is alive and kicking.")
    print("=" * 71)