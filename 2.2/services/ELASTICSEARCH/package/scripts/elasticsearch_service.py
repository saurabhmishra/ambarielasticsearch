#!/usr/bin/env python

from resource_management import *
from resource_management.core.exceptions import ComponentIsNotRunning
from resource_management.core.logger import Logger
import signal
import sys
import os

from elasticsearch import elasticsearch

class ELASTICSEARCHService(Script):
    def install(self, env):
        self.install_packages(env)
        self.configure(env)

    def configure(self, env):
        import params
        env.set_params(params)
        elasticsearch()

    def start(self, env):
        import params
        env.set_params(params)
        elasticsearch()
        cmd = format("/etc/init.d/elasticsearch start")
        Execute(cmd,
                user=params.es_user,
                path='/usr/sbin:/sbin:/usr/local/bin:/bin:/usr/bin',
                logoutput=True) 

    def stop(self, env):
        import params
        cmd = format('/etc/init.d/elasticsearch stop')
        Execute(cmd,
                user=params.es_user,
                path='/usr/sbin:/sbin:/usr/local/bin:/bin:/usr/bin',
                logoutput=True)

    def status(self, env):
        import params
        cmd = format('/etc/init.d/elasticsearch status')
        Execute(cmd,
                user=params.es_user,
                path='/usr/sbin:/sbin:/usr/local/bin:/bin:/usr/bin',
                logoutput=True)                  

if __name__ == "__main__":
    ELASTICSEARCHService().execute()
