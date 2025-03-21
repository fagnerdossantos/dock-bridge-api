import socket


class IP:

    def get_local_ip(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))  # Google DNS
            ip_local = s.getsockname()[0]
            s.close()
            return ip_local
        except:
            return None
