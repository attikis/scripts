#! /bin/bash
echo -n "*** Please type filename to put copied to ZEUS: "
read -e FILENAME
#echo -n "*** scp "$FILENAME" php7aa2@zeus.cc.ucy.ac.cy:~/wwwdata/PHYS_101/."
echo -n "*** scp "$FILENAME" attikis@zeus.cc.ucy.ac.cy:~/wwwdata/PHYS_101/."
echo
scp $FILENAME attikis@zeus.cc.ucy.ac.cy:~/wwwdata/PHYS_101/.
