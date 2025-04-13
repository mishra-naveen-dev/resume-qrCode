# QR Code Generator and Scanner

This project generates a QR code for a given URL and saves it as an image file. The QR code can be scanned to redirect users to the specified URL.

## How It Works

1. The script generates a QR code for the provided URL.
2. The QR code is saved as an image file named `qr-code.webp` in the project directory.

## Generated QR Code

After running the script, you can find the QR code image in the project directory. Below is an example of the generated QR code:

![Generated QR Code](qr-code.webp)

## How to Run

1. Install the required dependencies:
   ```
   pip install qrcode[pil]
   ```
2. Run the script:
   ```
   python qr-scanner.py
   ```
3. Open the `qr-code.webp` file to view the generated QR code.
