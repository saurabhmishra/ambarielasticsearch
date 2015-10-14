"""
Elastic service script.

"""

from resource_management import *
import signal
import sys
import os
from os.path import isfile

from elastic_slave  import elastic_slave


class Elasticsearch(Script):
    def install(self, env):
        import params
        env.set_params(params)
        print 'Install the Master'
        self.install_packages(env)
    def configure(self, env):
        import params
        env.set_params(params)
        elastic_slave()   
    def stop(self, env):
        import params
        env.set_params(params)
        stop_cmd = format("service elasticsearch stop")
        Execute(stop_cmd)
        print 'Stop the Master'
    def start(self, env):
        import params
        env.set_params(params)
        self.configure(env)
        start_cmd = format("service elasticsearch start")
        Execute(start_cmd)
        print 'Start the Master'
    def status(self, env):
        import params
        env.set_params(params)
        status_cmd = format("service elasticsearch status")
        Execute(status_cmd)
        print 'Status of the Master'
if __name__ == "__main__":
    Elasticsearch().execute()


