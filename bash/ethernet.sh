#kill all connections first
killall dhclient

#connect to any access point in range - change "ANY" with desirable network
 /sbin/iwconfig eth0  essid ANY

#do not specify address of access point 
 /sbin/iwconfig eth0  ap ANY
 
 sleep 1
 
 /sbin/dhclient eth0

#to run the script type: 
#localhost> sh ethernet.sh 

