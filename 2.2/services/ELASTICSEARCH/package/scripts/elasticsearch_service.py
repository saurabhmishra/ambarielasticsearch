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
        print 'Install plugins';
        output = os.system("/usr/share/elasticsearch/bin/plugin -DproxyHost= -DproxyPort=8080 --install mobz/elasticsearch-head")
        print output
        output = os.system("/usr/share/elasticsearch/bin/plugin -DproxyHost= -DproxyPort=8080 --install elasticsearch/elasticsearch-repository-hdfs/2.0.2")
        print output
	output = os.system("mkdir /mnt/es_data")
	print output
	output = os.system("chown elasticsearch:elasticsearch /mnt/es_data")
	print output
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
