## SHApi - Software Herritage API client

A python client to call the software heritage API to query for:

- archived repos
- submit requests for new one

### Usage

```bash
shapi --help
```

```bash

shapi check git <url>
shapi check  sv <url>
````

### Example

```bash
shapi check git https://github.com/tensorflow/tensorflow.git


```bash
{
  "origin": "https://github.com/tensorflow/tensorflow",
  "date": "2020-01-30T12:48:13.162613+00:00",
  "status": "full",
  "type": "git",
  "snapshot": "50a5123ba58a352be71a143446e2021c8f0471c9",
  "metadata": {},
  "visit": 50,
  "origin_url": "https://archive.softwareheritage.org/api/1/origin/https://github.com/tensorflow/tensorflow/get/",
  "snapshot_url": "https://archive.softwareheritage.org/api/1/snapshot/50a5123ba58a352be71a143446e2021c8f0471c9/"
}

```
