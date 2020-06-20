## SHApi - Software Herritage API client

<p align="center">
  <img src="docs/images/shapi.jpeg" alt="himalayan_thar" width="300" height="300"/>
</p>

A python client to call the software heritage API to query for:

- archived repos
- submit requests for new one

### Usage

```bash
shapi --help
```

#### Available commands

- Check if a repo is already archived and get the latest snapshot URI

```bash
shapi check <repo_tool> <uri>
```

### Example

```bash
shapi check git https://github.com/tensorflow/tensorflow.git
```


```bash
  "component_no": 1
  "component_url" : "https://github.com/tensorflow/tensorflow"
  "date_archived": "2020-01-30T12:48:13.162613+00:00"
  "archived_url": "https://archive.softwareheritage.org/api/1/snapshot/50a5123ba58a352be71a143446e2021c8f0471c9/"
```
