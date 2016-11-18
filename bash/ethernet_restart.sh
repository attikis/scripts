#Shutting down interface wifi: 
/etc/init.d/postfix stop

#Shutting down loopback interface: 
/etc/init.d/network stop

#cp /etc/X11/XF86Config.docked /etc/X11/XF86Config
cp /etc/sysconfig/network.cern /etc/sysconfig/network
#cp /etc/sysconfig/network-scripts/hp /etc/sysconfig/network-scripts/ifcfg-eth0
#cp /etc/resolv.conf.hp /etc/resolv.conf
#cp /etc/postfix/main.cf.hp /etc/postfix/main.cf

/etc/init.d/network start
/etc/init.d/postfix start