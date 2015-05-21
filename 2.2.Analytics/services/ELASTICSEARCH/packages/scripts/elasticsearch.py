#!/usr/bin/env python
"""
ElasticSearch service params.

"""

from resource_management import *
from properties_config import properties_config
import sys
from copy import deepcopy

def bdse():
    import params

    Directory([params.log_dir, params.pid_dir, params.conf_dir],
              owner=params.es_user,
              group=params.user_group,
              recursive=True
          )

    File(format("{conf_dir}/logging.yml"),
          content=params.logging_yaml,
	  owner=params.es_user,
          content=InlineTemplate(params.bdse_env_sh_template)
     )

    File(format("{conf_dir}/elasticsearch.yaml"),
        content=params.elasticsearch_yaml,
	owner=params.es_user,
        group=params.user_group
    )

