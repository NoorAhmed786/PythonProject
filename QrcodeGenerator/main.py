# import os # Import the required module for file handling
# import qrcode # Import the required module for generating QR code
# # Generate the QR code
# data = qrcode.make('dont forget to subscribe')
# qr= qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
# qr.add_data(data) # Add the data to the QR code
# qr.make(fit=True) # Generate the QR code
# img= qr.make_image(fill_color='red', back_color='white') # Create an image from the QR code
# img.save('D:/qrcode/qr_code.png')
# print('QR code saved to D:/python/qr_code.png') # Print a message


# # Generate the QR code
# img = qrcode.make('dont forget to subscribe')

# # Save the QR code image
# img.save('D:/qrcode/qr_code.png') # Save the QR code image 
# print('QR code saved to D:/python/qr_code.png') # Print a message

# ==================  encoding ==================
# ================== decoding ==================

from pyzbar.pyzbar import decode # Import the required module for decoding the QR code
from PIL import Image # Import the required module for image handling  pillow
img2= Image.open('D:/qrcode/qr_code.png') # Open the QR code image

result= decode(img2) # Decode the QR code image

print(result)
