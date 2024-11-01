# import network

# wlan = network.WLAN(network.STA_IF)
# wlan.active(True)
# wlan.connect('MSI 6218', 'abcd0113')

# wlan.status() # 3 == success
# # print( wlan.ifconfig() )
# wlan.ifconfig()

# # Get IP address for google.com
# import socket
# ai = socket.getaddrinfo("google.com", 80)
# addr = ai[0][-1]

# # Create a socket and make a HTTP request
# s = socket.socket()
# s.connect(addr)
# s.send(b"GET / HTTP/1.0\r\n\r\n")
# # Print the response
# print(s.recv(512))

# Connect to network
import network
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('MSI 6218', 'abcd0113')
 
 # Make GET request
import urequests
r = urequests.get("http://www.google.com")
print(r.content)
r.close()