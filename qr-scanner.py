

import qrcode


# Fixed redirection URL or backend API endpoint
redirect_url = "https://drive.google.com/file/d/11k3ofuVJZgGjjEv2jFqkM4Wci8NoC4y_/view?usp=drive_link"

# Generate the QR code
myQR = qrcode.make(redirect_url)
myQR.save("qr-code.webp")  # Save the QR code

# run command
# python qr-scanner.py