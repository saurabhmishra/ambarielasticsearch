# ambarielasticsearch
The repo contain basic implementation of Elasticsearch Install Using Ambari 2.0

It uses https://cwiki.apache.org/confluence/pages/viewpage.action?pageId=38571133 as an example

Work Done:

1) Deploy Master and Slaves ES cluster using Ambari and Host_groups.
2) Deploy Elasticsearch plugin for HDFS
3) Convert configuration for elasticsearch.yml into key/value based configuration.
4) Create seperate script for starting Slave, as of now it will start master and slaves in each node.
5) Create Smoke test scripts

Inprogress:
1) Add Metrics to Elasticsearch
2) Add Alerts to Elasticsearch
