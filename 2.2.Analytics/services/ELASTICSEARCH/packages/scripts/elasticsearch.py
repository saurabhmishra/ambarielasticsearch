#!/usr/bin/env python
"""
ElasticSearch service params.

"""

from resource_management import *
from properties_config import properties_config
import sys
from copy import deepcopy

def elasticsearch():
    import params

    Directory(params.conf_dir,
              owner=params.es_user,
              group=params.user_group,
              recursive=True
          )

    File(format("{params.conf_dir}/logging.yml"),
	mode=0644,
        content=params.logging_yaml,
	owner=params.es_user,
	group=params.user_group
     )

    File(format("{params.conf_dir}/elasticsearch.yaml"),
        mode=0644,
	content=params.elasticsearch_yaml,
	owner=params.es_user,
        group=params.user_group
    )

