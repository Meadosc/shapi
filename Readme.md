## SHApi - Software Herritage API client

<p align="center">
  <img src="docs/images/shapi.jpeg" alt="himalayan_thar" width="300" height="300"/>
</p>

A python client to query software heritage API for:

- archived repo
- submit request to archive repo

### Usage

```bash
shapi --help

Usage: shapi [OPTIONS] COMMAND [ARGS]...

  SHApi - Software Heritage(SH) API.

  A Python client to interact with software heritage API to query for an
  object, upload new pkgs to the repo.

Options:
  --version  Show the version and exit.
  --help     Show this message and exit.

Commands:
  check  Check if a repo url is archived in SH.

```

#### Available commands

- Check if a repo is already archived and get the latest snapshot URI

```bash
shapi check <uri>
```

### Example

```bash
shapi check https://github.com/tensorflow/tensorflow
```


```python
=======================================================================
Archive found
Date: 2020-01-30T12:48:13.162613+00:00
Src URL: https://github.com/tensorflow/tensorflow
Archive URL: https://archive.softwareheritage.org/api/1/snapshot/50a5123ba58a352be71a143446e2021c8f0471c9/
=======================================================================
```
