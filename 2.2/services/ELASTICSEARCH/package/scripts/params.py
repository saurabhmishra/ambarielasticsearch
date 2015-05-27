from resource_management.libraries.functions.version import format_hdp_stack_version, compare_versions
from resource_management import *

# server configurations
config = Script.get_config()
tmp_dir = Script.get_tmp_dir()


conf_dir = "/etc/elasticsearch"

es_user = "root"
user_group = "root"


logging_yml = config['configurations']['logging']['content']
elasticsearch_yml = config['configurations']['elasticsearch']['elasticsearchymlcontent']
