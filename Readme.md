## SHApi - Software Herritage API client

<p align="center">
  <img src="docs/images/shapi.jpeg" alt="himalayan_thar" width="300" height="300"/>
</p>

A python client to query Software Heritage API for:

- archived repo
- submit request to archive repo

### Install SHApi

```bash
git clone https://github.com/rahulunair/shapi && cd shapi && pip install .
```

### Usage

```python
Usage: shapi [OPTIONS] COMMAND [ARGS]...

  SHApi - Software Heritage(SH) API.

  A Python client to interact with software heritage API to query for an
  object, upload new pkgs to the repo.

Options:
  --version  Show the version and exit.
  --help     Show this message and exit.

Commands:
  check         Check if a repo url is archived in SH.
  status_check  API Health check.
  submit        Submit a repo to be archived in SH.
```

#### Available commands

- Check if a repo is already archived and get the latest snapshot URI

```bash
shapi status_check
shapi check <uri>
shapi submit <version_control_tool> <uri>
```

### Examples

```bash
shapi status_check
```

```python
=======================================================================
SH API is alive and kicking.
=======================================================================
```

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

```bash
shapi submit git https://github.com/tensorflow/tensorflow
```

```python
=======================================================================
Date: 2020-06-21T17:21:26.152749+00:00
Src URL: https://github.com/tensorflow/tensorflow
Save status: accepted
=======================================================================
```
