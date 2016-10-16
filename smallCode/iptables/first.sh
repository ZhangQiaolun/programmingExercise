#!/bin/sh
# delete all the rules
iptables -F -t filter
iptables -F -t nat
iptables -F -t mangle

# define new rules
# 1
iptables -t filter -I INPUT -p tcp --dport telnet -j ACCEPT
# 2
iptables -t filter -A INPUT -s 205.168.0.0/24 -j ACCEPT

# 5需要加上目的地址是本地的吗
iptables -t nat -A PREROUTING -i eth0 -p tcp --dport ftp -j DNAT --to 1.2.4.4:1008
