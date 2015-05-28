#!/usr/bin/env python
"""
ElasticSearch service params.

"""

from resource_management import *
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
	mode=0664,
        content=params.logging_yaml,
	owner=params.es_user,
	group=params.user_group
     )

    File(format("{params.conf_dir}/elasticsearch.yml"),
        mode=0664,
	content=params.elasticsearch_yaml,
	owner=params.es_user,
        group=params.user_group
    )

