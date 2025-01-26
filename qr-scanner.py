

import qrcode


# Fixed redirection URL or backend API endpoint
redirect_url = "https://drive.google.com/file/d/1vbfaoglO4cvmt1Zn00vJa2Fpl7jjzYK8/view?usp=drive_link"

# Generate the QR code
myQR = qrcode.make(redirect_url)
myQR.save("qr-code.png")  # Save the QR code

