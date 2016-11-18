#kill all connections first
killall dhclient

#connect to any access point in range - change "ANY" with desirable network
 /sbin/iwconfig eth1  essid ANY

#do not specify address of access point 
 /sbin/iwconfig eth1  ap ANY
 
 sleep 1
 
 /sbin/dhclient eth1

#to run the script type: 
#localhost> sh wifi_connect.sh 

