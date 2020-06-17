"""CLI entrypoint to shapi."""
import click
from . import __version__

#from  .client import Client

@click.group()
@click.version_option(version=__version__)
def cli() -> None:
    """SHApi - Software Herritage API.

    A Python client to interact with software herritage API
    to query for an object, upload new pkgs to the repo.
    """
