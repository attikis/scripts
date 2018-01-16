#!/bin/bash

# Definitions
DIRECTORY=/Users/attikis/root

#printf "=== RootSetup.sh:\n\tStart"
if [ "$1" == "l" ]; then
    printf "=== RootSetup.sh:\n\tThe available versions are:\n"
  ls $DIRECTORY | grep v
  exit
fi

if [ ! -d $DIRECTORY/${1} ]; then
  printf "\n=== RootSetup.sh:\n\tThe ROOT version $1 does not exist. The available versions are:"
  ls $DIRECTORY/ | grep v 
  exit
fi

printf "\n=== RootSetup.sh:\n\tSetting up ROOT ${1}"
if [ "$1" == "v6-06-08" ]; then
. $DIRECTORY/${1}/bld-root/bin/thisroot.sh
else
. $DIRECTORY/${1}/bin/thisroot.sh
fi

#printf "\n=== RootSetup.sh:\n\tEnd\n"
echo


#if [ $1 == "v5" ];
#then  
  #export PYTHIA6=/Users/attikis/pythia6
  #export PYTHIA8=/Users/attikis/pythia8185
  #export LHA=/sw/codes/lhapdf_5.9.1
  #export LHAPDF=$LHA/lib
  #export LHAPATH=$LHA/share/lhapdf/PDFsets
  #export PATH=$PATH:$LHA/bin
  #export PYTHIA8DATA=$PYTHIA8/xmldoc
  #export DYLD_LIBRARY_PATH=$DYLD_LIBRARY_PATH:$PYTHIA6:$PYTHIA8/lib:$LHAPDF
  #export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$PYTHIA6:$PYTHIA8/lib:$LHAPDF
#fi

