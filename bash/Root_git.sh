#! /bin/bash
#==============
# if you have /sw from a fink setup if not you could install it 
# on your home directory so you want need sudo
#  $1 is the version of root. The pro version is v6-08-06
#===============
MyRoot=/usr/local/Codes/root
cd $MyRoot
Sudo git clone http://root.cern.ch/git/root.git src_$1
cd src_$1
sudo git checkout -b $1 $1
cd $MyRoot
sudo mkdir $1         # you need to build it in a different directory
sudo cd $1
sudo cmake $MyRoot/src_$1 -DRooFit=ON -Dminuit2=ON -Dbuiltin_fftw3=ON
sudo cmake --build . -- -j4       # watch the . after the build

# You need the CMake executable you download the dmg from cmake.org
# After installation add the CMake to the path
# export PATH=/Applications/CMake.app/Contents/bin:$PATH
# 
# You will need the latest xcode and xcode_command_tools 
# xcode-select -p         # to see if you have it 
# xcode-select --install  # to install the latest
#
# ccmake <source dir> (you will need sudo if the root build dir is in system)
# toggle roofit=ON
# toggle minuit2=ON
# toggle builtin_fftw3=ON
# exit and recompile
