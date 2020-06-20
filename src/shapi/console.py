"""CLI entrypoint to shapi."""
import click

from . import __version__

from  client import SHClient


@click.group()
@click.version_option(version=__version__)
def cli() -> None:
    """SHApi - Software Heritage API.

    A Python client to interact with software heritage API
    to query for an object, upload new pkgs to the repo.
    """


@cli.command("check")
@cli.argument("hash", type=str)
def check(hash: str) -> None:
    """Check if a package is available using its hash.

    The hash can be sha1 or sha2."""
    """
    res: dict = client.check(hash)
    if res["available"]:
        print("pkg in Software Heritage,")
        print("src url: {}".format(res["url"]))
    else:
        print("couldn't fine the package in SH, consider upload it.")
    """
