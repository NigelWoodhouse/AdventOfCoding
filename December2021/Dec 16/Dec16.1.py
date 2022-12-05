hex_string = "8A004A801A8002F478"

h_size = len(hex_string) * 4
binary_string = ( bin(int(hex_string, 16))[2:] ).zfill(h_size)

print(binary_string)

packet_version  = int(binary_string[0:3], 2)
packet_type  = int(binary_string[3:6], 2)
length_type_ID = int(binary_string[6], 2)

if length_type_ID == 0:
    bit_length = 15
elif length_type_ID == 1:
    bit_length = 11


print(packet_version, packet_type, length_type_ID, number_of_packets)
print(sum)