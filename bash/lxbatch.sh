#!/bin/tcsh
echo "-----------------------------------------------------------------------"
echo "Using:"
echo $SHELL
echo ""
# Create shortcut for current working directory (tcsh script)
set curdir=`pwd`  
echo "--> Current Working Directory is:"
echo $curdir
echo ""
# OR, if using SHELL script:
# curdir=`pwd`
# echo $curdir

# Get to the source directory on my local area
echo "cd /afs/cern.ch/user/a/attikis/"
cd /afs/cern.ch/user/a/attikis/
# run the environment script:
echo "source cms_2_2_6_env.sh"
source cms_2_2_6_env.sh
#source cms_env_lxbatch.sh
echo ""
echo "-----------------------------------------------------------------------"
echo "------ Executing the necessary job steps ------"
echo "-----------------------------------------------------------------------"
echo ""
# Go pack to home directory on LXBATCH
cd $curdir
echo "--> Current Working Directory is:"
pwd

# create a working directory
#mkdir MssmHiggsAnalyzer
mkdir CMSSW
# get to the working directory
#cd MssmHiggsAnalyzer
cd CMSSW
echo ""
# run the python configuration file and save output to a log file:
echo ""
echo "-----------------------------------------------------------------------"
echo "cmsRun /afs/cern.ch/user/a/attikis/scratch0/CMSSW_2_2_6/src/analysis/MssmHiggsAnalyzer/attikis_test.py >& lxbatch_test_21apr09.log"
echo "-----------------------------------------------------------------------"
echo ""
cmsRun /afs/cern.ch/user/a/attikis/scratch0/CMSSW_2_2_6/src/analysis/MssmHiggsAnalyzer/attikis_test.py >& lxbatch_test_21apr09.log
echo ""
echo "--> Current Working Directory is:"
pwd
echo ""
echo "--> Listing files in Current Directory"
ls
echo ""
echo "-----------------------------------------------------------------------"
echo "------ Copying ROOT and log files to CASTOR and LXPLUS ------"
echo "-----------------------------------------------------------------------"
echo ""

# Copy complete ROOT file to CASTOR
# rfcp attikis_test.root /castor/cern.ch/user/a/attikis/.
rfcp attikis_test.root /castor/cern.ch/a/attikis/phd_thesis/test/gen/.
# Copy complete ROOT file to LXPLUS
# cp attikis_test.root /afs/cern.ch/user/a/attikis/scratch0/CMSSW_2_2_6/src/analysis/MssmHiggsAnalyzer/.

# Copy analysis ROOT file to CASTOR
rfcp attikis_test_analysis.root /castor/cern.ch/a/attikis/phd_thesis/test/gen/.
# Copy analysis ROOT file to LXPLUS
cp attikis_test_analysis.root /afs/cern.ch/user/a/attikis/scratch0/CMSSW_2_2_6/src/analysis/MssmHiggsAnalyzer/.

# Copy log file to CASTOR
rfcp lxbatch_test_21apr09.log /castor/cern.ch/a/attikis/phd_thesis/test/gen/.
# Copy log file to LXPLUS
cp lxbatch_test_21apr09.log /afs/cern.ch/user/a/attikis/scratch0/CMSSW_2_2_6/src/analysis/MssmHiggsAnalyzer/.

# clean up the working directory
cd $curdir
echo "-----------------------------------------------------------------------"
echo "------ Cleaning up the working directory ------"
echo "-----------------------------------------------------------------------"
rm -r CMSSW
echo ""
echo "--> Current Working Directory is:"
pwd
echo ""
echo "--> Listing files in Current Directory"
ls
echo ""
echo "-----------------------------------------------------------------------"
