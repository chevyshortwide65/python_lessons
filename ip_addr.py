#input for ip address and split/join
ip_addr = "10.132.23.0"
network = "255.255.255.0"

#put strings in an octet list
ip_addr_oct = ip_addr.split(".")
network_oct = network.split(".")

#binary conversions
ip_addr_bin0 = bin(int(ip_addr_oct[0]))
ip_addr_bin1 = bin(int(ip_addr_oct[1]))
ip_addr_bin2 = bin(int(ip_addr_oct[2]))
ip_addr_bin3 = bin(int(ip_addr_oct[3]))

#hex conversions
ip_addr_hex0 = hex(int(ip_addr_oct[0]))
ip_addr_hex1 = hex(int(ip_addr_oct[1]))
ip_addr_hex2 = hex(int(ip_addr_oct[2]))
ip_addr_hex3 = hex(int(ip_addr_oct[3]))

#format in to a table
print ("%20s %50s") % ("IP Add", "Netmask")
print ("%20s %30s") % ("Binary Conversion", "Hex Conversion")
print ("%s %s %s %s %s %s %s %s") % (ip_addr_bin0, ip_addr_bin1, ip_addr_bin2, ip_addr_bin3 , ip_addr_hex0, ip_addr_hex1, ip_addr_hex2, ip_addr_hex3)
