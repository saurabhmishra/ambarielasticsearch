#!/usr/bin/env python
"""
Elasticsearch Params configurations
"""

from resource_management.libraries.functions.version import format_hdp_stack_version, compare_versions
from resource_management import *
import status_params

# server configurations
config = Script.get_config()

elastic_home = '/etc/elasticsearch/'
elastic_bin = '/usr/share/elasticsearch/bin/'

conf_dir = "/etc/elasticsearch"
elastic_user = config['configurations']['elastic-env']['elastic_user']
log_dir = config['configurations']['elastic-env']['elastic_log_dir']
pid_dir = '/var/run/elasticsearch'
pid_file = '/var/run/elasticsearch/elasticsearch.pid'
hostname = config['hostname']
user_group = config['configurations']['cluster-env']['user_group']
java64_home = config['hostLevelParams']['java_home']
elastic_env_sh_template = config['configurations']['elastic-env']['content']

template = config['configurations']['elastic-site']['template']
defaultName = config['configurations']['elastic-site']['defaultName']

authenticationType = config['configurations']['elastic-site']['authenticationType']
cluster_name = config['configurations']['elastic-site']['cluster_name']
node_data = config['configurations']['elastic-site']['node_data']
node_master = config['configurations']['elastic-site']['node_master']
node_master1 = config['configurations']['elastic-site']['node_master1']
node_master2 = config['configurations']['elastic-site']['node_master2']
node_master3 = config['configurations']['elastic-site']['node_master3']
node_name = config['configurations']['elastic-site']['node_name']
path_data = config['configurations']['elastic-site']['path_data']
http_port = config['configurations']['elastic-site']['http_port']
transport_tcp_port = config['configurations']['elastic-site']['transport_tcp_port']
recover_nodes = config['configurations']['elastic-site']['recover_nodes']
discovery_zen_ping_unicast_hosts = config['configurations']['elastic-site']['discovery_zen_ping_unicast_hosts']
recover_after_time = config['configurations']['elastic-site']['recover_after_time']
recover_after_data_nodes = config['configurations']['elastic-site']['recover_after_data_nodes']
expected_data_nodes = config['configurations']['elastic-site']['expected_data_nodes']
discovery_zen_ping_multicast_enabled = config['configurations']['elastic-site']['discovery_zen_ping_multicast_enabled']
index_merge_scheduler_max_thread_count= config['configurations']['elastic-site']['index_merge_scheduler_max_thread_count']
index_translog_flush_threshold_size = config['configurations']['elastic-site']['index_translog_flush_threshold_size']
index_refresh_interval = config['configurations']['elastic-site']['index_refresh_interval']

