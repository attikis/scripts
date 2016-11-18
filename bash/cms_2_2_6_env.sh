#To run this script type: 
# [lxplus238]~ > source CMSenv.sh   or [lxplus238]~ >source ~/CMSenv.sh
# Writing: [lxplus238]~ > ./CMSenv.sh    #Will NOT work!
#----------------------------------------------------------------------#
#!/bin/bash
# Set up your Environment
echo "\n------> Setting up CMS Runtime Environment <------\n"
#----------------------------------------------------------------------#
# Get to the source directory
echo "cd /afs/cern.ch/user/a/attikis/scratch0/CMSSW_2_2_6/src"
cd /afs/cern.ch/user/a/attikis/scratch0/CMSSW_2_2_6/src
echo "\n------> Using CMSSW_2_2_6 <------\n"
#----------------------------------------------------------------------#
# Now build the work area
echo "cmsenv"
cmsenv
# which is short for:
# eval 'scramv1 runtime -csh'
#----------------------------------------------------------------------#
#Set up ROOT: Authenticated CVS access (kserver)
echo "\n------> Setting up ROOT <------\n"
project CMSSW
echo project CMSSW
#----------------------------------------------------------------------#
# For Anonymous CVS access (pserver) use:
#cmscvsroot CMSSW
echo "\nCVSROOT is"
echo $CVSROOT
echo "\nCurrent Working Directory is:" 
pwd
echo "\n----> CMS Environment now SET <----\n"
#end of document
#----------------------------------------------------------------------#
