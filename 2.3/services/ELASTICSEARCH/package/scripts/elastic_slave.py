#!/usr/bin/env python
"""
elasticsearch service params.

"""

from resource_management import *
from properties_config import properties_config
import sys
from copy import deepcopy

def elastic_slave():
    import params

    Directory([params.log_dir, params.pid_dir, params.conf_dir],
              owner=params.elastic_user,
              group=params.user_group,
              recursive=True
          )

    File(format("{conf_dir}/elastic-env.sh"),
          owner=params.elastic_user,
          content=InlineTemplate(params.elastic_env_sh_template)
     )

    configurations = params.config['configurations']['elastic-site']

    File(format("{conf_dir}/elasticsearch.yml"),
       content=Template(
                        "elasticsearch.slave.yaml.j2",
                        configurations = configurations),
       owner=params.elastic_user,
       group=params.user_group
    )
