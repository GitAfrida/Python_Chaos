import os
import qrcode

# Information to store in the QR code
qr_data = """
Name: Afrida Ali
Email: afridaali006@gmail.com
GitHub: https://github.com/GitAfrida
"""

# Create output folder if it doesn't exist
os.makedirs("output", exist_ok=True)

# Create QR code object
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=4
)

# Add data to QR code
qr.add_data(qr_data)
qr.make(fit=True)

# Create the QR image
image = qr.make_image(fill_color="black", back_color="white")

# Save the image
file_path = "output/afrida_qr.png"
image.save(file_path)

print(f"QR code generated successfully: {file_path}")