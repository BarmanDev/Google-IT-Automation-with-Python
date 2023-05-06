def identify_IP(IP_address):
    if IP_address == "192.168.1.1":
        IP_description = "Network router"
    elif IP_address == "8.8.8.8" or IP_address == "8.8.4.4":
        IP_description = "Google DNS server"
    elif IP_address == "142.250.191.46":
        IP_description = "Google.com"
    else:
        IP_description = "unknown"
    return IP_description


print(identify_IP("8.8.4.4"))  # Should print 'Google DNS server'
print(identify_IP("142.250.191.46"))  # Should print 'Google.com'
print(identify_IP("192.168.1.1"))  # Should print 'Network router'
print(identify_IP("8.8.8.8"))  # Should print 'Google DNS server'
print(identify_IP("10.10.10.10"))  # Should print 'unknown'
print(identify_IP(""))  # Should Should print 'unknown'
