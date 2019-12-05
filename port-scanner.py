import socket
import sys

target = "localhost"

print("PORT SCANNER")

try:
    for port in range(65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = s.connect_ex(("localhost",port))
        if result ==0:
            print("[{}]:OPEN".format(port))

        else:
            pass

except KeyboardInterrupt:
        print("You pressed Ctrl+C")
        sys.exit()

