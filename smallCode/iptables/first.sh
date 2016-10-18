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
# 3
iptables -t nat -A POSTROUTING -o eth0 -j SNAT --to 1.2.3.4
# 4
iptables -t nat -A PREROUTING -i eth0 -s 202.127.14.61 -j DNAT --to 1.2.4.4

# 5
iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 20 -j DNAT --to 1.2.4.4:1008

# 6
iptables -A INPUT -p tcp -dport 21 -j ACCEPT
iptables -A OUTPUT -p tcp -dport 21 -j ACCEPT
iptables -A INPUT -p tcp --sport 20 -m state --state ESTABLISHED,RELATED -j ACCEPT
iptables -A OUTPUT -P tcp --sport 20 -m state --state ESTABLISHED,RELATED -j ACCEPT

# 7
iptalbes -t filter -A INPUT -s eth0 -p icmp --icmp-type 0 -j drop
