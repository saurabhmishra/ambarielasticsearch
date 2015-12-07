#!/usr/bin/env python
"""
Elasticsearch service checks.

"""
from __future__ import print_function
from resource_management import *
import  sys,subprocess,os
import urllib2 
import time

class ServiceCheck(Script):
    def service_check(self, env):
        import params
        env.set_params(params)

	print("Running Elastic search  service check", file=sys.stdout)
        # There is a race condition by the time the BDSE server starts and service checks.  Hence added the below sleep for 30 seconds
        time.sleep(30)
	r = urllib2.urlopen('http://localhost:9200/') 

        if r.getcode() == 200:
	    print(r.json(), file=sys.stdout)
            sys.exit(0)
        else:
	    print("Elastic service is not running", file=sys.stderr)
            sys.exit(1)


if __name__ == "__main__":
    ServiceCheck().execute()
