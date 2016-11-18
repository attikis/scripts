#!/usr/bin/env python

# Script docstrings
'''
Usage:
./ssh_cmd.py

Permissions: 
chmod +x ssh_cmd.py

Install python package:
|\> sudo easy_install package_name
e.g. |\> sudo easy_install paramiko

Description:
The Secure SHell (SSH) protocol allows one to securely connect to a remote
server, execute shell commands, transfer files and forward ports in both
directions (local<->remote). It is incredibly powerful and widely used. 

Using the ssh command in parallel with the full power of python can be
extremely useful. The dedicated library is called "paramiko".

Options:
  -h, --help            show this help message and exit
  -a ADDRESS OF REMOTE HOST, --hostname=ADDRESS OF REMOTE HOST
                        ADDRESS OF REMOTE HOST
  -u AUTHENTICATION USERNAME, --username=AUTHENTICATION USERNAME
                        AUTHENTICATION USERNAME
  -c SHELL COMMAND, --command=SHELL COMMAND
                        SHELL COMMAND TO REMOTELY EXECUTE ON HOST
  -r SHELL COMMAND, --report=SHELL COMMAND
                        SHELL COMMAND TO REMOTELY EXECUTE ON HOSTOptions:

Usage:
ssh.py -u attikis -a jade.hip.fi -c lsd - r True
'''

# All required modules here
import python_myFunctions as myFunctions
import paramiko
from optparse import OptionParser 
import getpass
from datetime import datetime

# Declarations here
mf = myFunctions.CreateObject()
parser = OptionParser()

parser.add_option("-a", "--hostname", default = "lxplus.cern.ch", dest = "hostname", help = "ADDRESS OF REMOTE HOST", metavar = "ADDRESS OF REMOTE HOST")
parser.add_option("-u", "--username", default = "attikis", dest = "username", help = "AUTHENTICATION USERNAME", metavar = "AUTHENTICATION USERNAME")
parser.add_option("-c", "--command", default = "ls -lt", dest = "cmd", help = "SHELL COMMAND TO REMOTELY EXECUTE ON HOST", metavar = "SHELL COMMAND")
parser.add_option("-r", "--report", default = False, dest = "report", help = "SHELL COMMAND TO REMOTELY EXECUTE ON HOST", metavar = "SHELL COMMAND")
(options, args) = parser.parse_args()

if not (options.hostname and options.username):
    print __doc__
    parser.error("REMOTE HOST and USERNAME are mandatory")

if __name__ == "__main__":
    mf.StopWatchStart()
    
    timeStamp = str(datetime.now())
    logFileName = ("ssh_" + options.username + "_" + options.hostname + "_" + timeStamp).replace(" ", "_").replace("-", "_").replace(".", "_") + ".log"
    paramiko.util.log_to_file(logFileName)

    # Create ssh instance
    mf.Cout("Connecting to %s@%s" % (options.username, options.hostname))    
    ssh = paramiko.SSHClient()

    # Load the host keys (comes from the "know_hosts" file)
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Connect to the SSH server
    ssh.connect(options.hostname, username = options.username, password = getpass.getpass("\tPassword = "))

    # Execute a command remotely
    mf.Cout("Executing the command %s remotely." % (options.cmd) )
    stdin, stdout, stderr = ssh.exec_command(options.cmd)

    # Return related handles
    mf.Cout("Returning three file handles associated with it.")
    mf.Cout("stderr.read():\n\t%s" % (stderr.read()))
    mf.Cout("stdout.read():\n\t%s" % (stdout.read()))

    # Close connection
    mf.Cout("Closing connection.")
    ssh.close()

    # Investigate report log
    if(options.report):
        logFile = open(logFileName, "r")
        mf.Cout("Logfile %s:\n\t" % (logFileName) )
        #print logFile.read()

    # Print elapsed time for script execution 
    mf.StopWatchStop()
