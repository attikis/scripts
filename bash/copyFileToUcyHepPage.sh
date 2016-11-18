#! /bin/bash
echo -n "*** Please type filename to put copied to ZEUS: "
read -e FILENAME
echo -n "*** scp "$FILENAME" attikis@zeus.cc.ucy.ac.cy:~/wwwdata/UCYHEP/."
echo
scp $FILENAME attikis@zeus.cc.ucy.ac.cy:~/wwwdata/UCYHEP/.
