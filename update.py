# -*- coding: utf-8 -*-
import urllib3
from lxml import etree
import html
import re
import os
import json

urllib3.disable_warnings()

baseUrl = 'https://api.github.com/repos/'

def getUpdateTime(owner, repo):
    url = baseUrl + owner + '/' + repo + '/commits'
    http = urllib3.PoolManager()
    r = http.request('GET', url, headers = headers)
    date = json.loads(r.data.decode('utf-8'))[0]['commit']['author']['date']
    return date

def writeReadme():
    f = open('README.md', 'w+')

    dgraphDate = getUpdateTime("dgraph-io","dgraph")

    head = """
# awesome-graph-database

<div align="center">
<img border="0" src="https://camo.githubusercontent.com/54fdbe8888c0a75717d7939b42f3d744b77483b0/687474703a2f2f6a617977636a6c6f76652e6769746875622e696f2f73622f69636f2f617765736f6d652e737667" />
<img border="0" src="https://camo.githubusercontent.com/1ef04f27611ff643eb57eb87cc0f1204d7a6a14d/68747470733a2f2f696d672e736869656c64732e696f2f7374617469632f76313f6c6162656c3d254630253946253843253946266d6573736167653d496625323055736566756c267374796c653d7374796c653d666c617426636f6c6f723d424334453939" />
<a href="https://github.com/Unstructured-Data-Community/awesome-graph-database/issues">     <img border="0" src="https://img.shields.io/github/issues/Unstructured-Data-Community/awesome-graph-database" /> </a>
<a href="https://github.com/Unstructured-Data-Community/awesome-graph-database/network/members">     <img border="0" src="https://img.shields.io/github/forks/Unstructured-Data-Community/awesome-graph-database" /> </a>
<a href="https://github.comUnstructured-Data-Community/awesome-graph-database/stargazers">     <img border="0" src="https://img.shields.io/github/stars/Unstructured-Data-Community/awesome-graph-database" /> </a>
</div>

This project collects graph database related products and cloud services, for each open-source product, it will be followed by the most recent update time to help you quickly judge whether the project is active or not.

该项目收集了图数据库相关产品与云服务，对于每个开源产品，会在其后面标注最近的更新时间帮助大家快速判断该项目是否活跃。

*排名不分先后 <br/> In no particular order*

## Products

| **Name** |  **Introduction**  | **Open source** | **Last updated** |
|:-----|:--------:|:----------:|:-----------:|
| [dgraph](https://dgraph.io/) | Dgraph is a horizontally scalable and distributed GraphQL database with a graph backend. It provides ACID transactions, consistent replication, and linearizable reads. It's built from the ground up to perform for a rich set of queries. Being a native GraphQL database, it tightly controls how the data is arranged on disk to optimize for query performance and throughput, reducing disk seeks and network calls in a cluster. | [yes](https://github.com/dgraph-io/dgraph) | """ + dgraphDate + """ |

___
## Contributors

<a href="https://github.com/Unstructured-Data-Community/awesome-graph-database/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=Unstructured-Data-Community/awesome-graph-database" />
</a>

Made with [contrib.rocks](https://contrib.rocks).

## LICENSE

[MIT license](./LICENSE)
    """

    f.write(head)
    f.close

if __name__ == "__main__":
    Authorization = 'Bearer ' + os.environ["token"]
    headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36', 'Accept': 'application/vnd.github+json', 'Authorization': Authorization} 
    writeReadme()

