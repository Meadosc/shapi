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


@cli.command("check")
@click.argument("url", type=str)
def check(url: str) -> None:
    """Check if a repo url is archived in SH.

    Give the full URL of the repo hosted in git, svn etc.

    Args:
        url: repo url to check, eg: https://github.com/tensorflow/tensorflow
    """
    url = _origin_check(url)
    #TODO (unrahul): cache
    resp = sh_client.query("GET", url)
    print("=" * 71)
    print("Archive found")
    print("Date: {}".format(resp["date"]))
    print("Src URL: {}".format(resp["origin"]))
    print("Archive URL: {}".format(resp["snapshot_url"]))
    print("=" * 71)
