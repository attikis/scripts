#!/usr/bin/env python

# Script docstrings
'''
Usage: kinit.py [options]

Options:
  -h, --help            show this help message and exit
  -a ADDRESS OF REMOTE HOST, --hostname=ADDRESS OF REMOTE HOST
                        ADDRESS OF REMOTE HOST
  -u AUTHENTICATION USERNAME, --username=AUTHENTICATION USERNAME
                        AUTHENTICATION USERNAME
  -c SHELL COMMAND, --command=SHELL COMMAND
                        SHELL COMMAND TO REMOTELY EXECUTE ON HOST
Permissions: 
chmod +x kinit.py

URL help:
http://linux.web.cern.ch/linux/docs/kerberos-access.shtml
https://hypernews.cern.ch/HyperNews/CMS/get/comp-ops/194/2/2.html

Description:
Kerberos is shared-secret networked authentication system. Its use at CERN serves a dual purpose:
user convenience: once signed in, authentication is handled "automagically" on the users' behalf.
security: by reducing the need to enter passwords into potentially compromised machines, the impact of 
such a compromise can be greatly reduced.

For an overview and introduction into the concepts, please see man kerberos, 
MIT's site or the Kerberos FAQ. Several books exist on the subject as well.
'''

# All required modules here
#import paramiko
from optparse import OptionParser 
import subprocess

# Declarations here
parser = OptionParser()

parser.add_option("-a", "--hostname", default = "CERN.CH", dest = "hostname", help = "ADDRESS OF REMOTE HOST", metavar = "ADDRESS OF REMOTE HOST")
parser.add_option("-u", "--username", default = "attikis", dest = "username", help = "AUTHENTICATION USERNAME", metavar = "AUTHENTICATION USERNAME")
parser.add_option("-c", "--command", default = "kinit -f", dest = "cmd", help = "SHELL COMMAND TO REMOTELY EXECUTE ON HOST", metavar = "SHELL COMMAND")
(options, args) = parser.parse_args()

if not (options.hostname and options.username):
    print __doc__
    parser.error("REMOTE HOST and USERNAME are mandatory")

if __name__ == "__main__":

    # Create ssh instance
    print "*** Creating kerberos ticket for %s@%s" % (options.username, options.hostname)

    # Execute a command remotely
    cmd = options.cmd + " " + options.username + "@" + options.hostname
    subprocess.call(cmd, shell=True)
    
    print "*** Can now ssh or scp from remote host:\n\tusername@lxplus.cern.ch"
