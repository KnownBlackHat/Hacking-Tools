#!/bin/sh
p1=$(ifconfig wlan0 | grep "inet " | cut -d " " -f 10 | cut -d "." -f 1)
p2=$(ifconfig wlan0 | grep "inet " | cut -d " " -f 10 | cut -d "." -f 2)
p3=$(ifconfig wlan0 | grep "inet " | cut -d " " -f 10 | cut -d "." -f 3)
echo
echo
echo "Available IP(s) on "$p1"."$p2"."$p3".0 are :"
for i in $(seq 254)
do
ping -c1 $p1.$p2.$p3.$i | grep "64 bytes" | cut -d " " -f 4 | tr -d ":" &
#ip=$(ping -c1 $p1.$p2.$p3.$i | grep "64 bytes" | cut -d " " -f 4 | tr -d ":" &)
done
