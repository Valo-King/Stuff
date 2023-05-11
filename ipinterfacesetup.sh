sudo ip address add 192.168.0.78/24 broadcast + dev eno1
sudo ip link set eno1 up
sudo ip route add default via 192.168.0.1 dev eno1
