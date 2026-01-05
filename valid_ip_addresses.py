def int_str(string, start, size):
    n = string[start:start + size]
    if len(n) > 1 and n.startswith("0"):
        return None
    if int(n) > 255:
        return None
    return n

def validIPAddresses(string):
    ip_addresses = []
    size = len(string)
    for s1 in range(1, 4):
        for s2 in range(1, 4):
            for s3 in range(1, 4):
                for s4 in range(1, 4):
                    if s1 + s2 + s3 + s4 != size:
                        continue
                    a1 = int_str(string, 0, s1)
                    a2 = int_str(string, s1, s2) 
                    a3 = int_str(string, s1 + s2, s3)
                    a4 = int_str(string, s1 + s2 + s3, s4)
                    if a1 == None or a2 == None or a3 == None or a4 == None:
                        continue
                    address =  a1 + "." + a2 + "." + a3 + "." + a4 
                    ip_addresses.append(address)
    return ip_addresses
