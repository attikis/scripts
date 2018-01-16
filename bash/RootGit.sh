#!/bin/bash
#======================================================================
# Options:
# $1 is the version of root. The pro version is v6-08-06
#
# Prerequisites (macOS):
# 1) You need the CMake executable you download the dmg from cmake.org
# After installation add the cmake to the path
# export PATH=/Applications/cmake.app/Contents/bin:$PATH
# 
# 2) You will need the latest xcode and xcode_command_tools 
# xcode-select -p         # to see if you have it 
# xcode-select --install  # to install the latest
#======================================================================
printf "=== RootGit.sh:\n\tDefinitions\n"
BASE_DIR=/Users/attikis/root
GIT_REPO=http://root.cern.ch/git/root.git
GIT_BRANCH=$1
SRC_DIR=src_$1

# Check if $BASE_DIR exists. If not create it
if [ -d "$BASE_DIR" ]; then
    cd $BASE_DIR
else
    printf "=== RootGit.sh:\n\tCreating directory $BASE_DIR\n"
    mkdir $BASE_DIR
    cd $BASE_DIR
fi

printf "=== RootGit.sh:\n\tChanging directory to $BASE_DIR\n"
cd $BASE_DIR
printf "=== RootGit.sh:\n\t`pwd`\n"

# Git clone the ROOT repository
printf "=== RootGit.sh:\n\tCloning git repo of ROOT ($GIT_REPO) to new directory ($SRC_DIR)\n"
sudo git clone $GIT_REPO $SRC_DIR

printf "=== RootGit.sh:\n\tChanging directory to $SRC_DIR\n"
cd $SRC_DIR
printf "=== RootGit.sh:\n\t`pwd`\n"

printf "=== RootGit.sh:\n\tChecking-out git branch ($GIT_BRANCH) as new branch ($GIT_BRANCH)\n"
sudo git checkout -b $GIT_BRANCH $GIT_BRANCH

printf "=== RootGit.sh:\n\tChanging directory to $BASE_DIR\n"
cd $BASE_DIR
printf "=== RootGit.sh:\n\t`pwd`\n"

printf "=== RootGit.sh:\n\tCreating new directory $GIT_BRANCH\n"
sudo mkdir $GIT_BRANCH # you need to build it in a different directory

printf "=== RootGit.sh:\n\tChanging directory to $GIT_BRANCH\n"
cd $GIT_BRANCH
printf "=== RootGit.sh:\n\t`pwd`\n"

printf "=== RootGit.sh:\n\tCMaking code under $BASE_DIR/$SRC_DIR\n"
sudo cmake $BASE_DIR/$SRC_DIR

# printf "=== RootGit.sh:\n\tEnabling ROOT fit by switching on toggles\n"
# toggle roofit=ON
# toggle minuit2=ON
# toggle builtin_fftw3=ON

printf "=== RootGit.sh:\n\tChanging directory to $BASE_DIR/$GIT_BRANCH\n"
sudo cd $BASE_DIR/$GIT_BRANCH

printf "=== RootGit.sh:\n\tCMaking --build . -- -j 4\n"
sudo cmake --build . -- -j4       # watch the . after the build

printf "=== RootGit.sh:\n\tEnd"
printf
