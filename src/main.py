import sys

import qrcode
from api.routes import app
from core.local_ip import IP  # From local archive


if __name__ == '__main__':
    ip = IP().get_local_ip()
    if ip:
        qr = qrcode.QRCode(border=2)
        qr.add_data(f'http://{ip}:5000')
        qr.make(fit=True)
    
        qr.print_ascii()
        app.run(debug=False, host=ip, port=5000)

    else:
        print("It was not possible to get the local IP address.")
        sys.exit(1)
