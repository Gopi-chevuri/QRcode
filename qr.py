import qrcode

qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=20, border=2)

# Defining the data we want to encode in the QR code
data =input()

# Adding the data to the QR code
qr.add_data(data)

# Generating the QR code
qr.make(fit=True)

# Creating an image from the QR code
qr_image = qr.make_image(fill_color="black", back_color="white")

# Save the image as a file with name scandata
qr_image.save("scandata.png")
