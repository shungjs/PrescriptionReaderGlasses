from picamera import PiCamera
from time import sleep
from pyzbar.pyzbar import decode
from PIL import Image

camera = PiCamera()

def capture_image(image_path):

	camera.capture(image_path)
	print(f"Captured image saved at {image_path}")

def decode_qr(image_path):

	qr_image = Image.open(image_path)
	decoded_info = decode(qr_image)

	if decoded_info:
		print("Decoded data:" , decoded_info[0].data.decode())
	else:
		print("No QR code found.")

try:
	while True:
		camera.start_preview()
		image_path = '/home/wa/qrcode.jpg'
		capture_image(image_path)
		decode_qr(image_path)
		sleep(5)
		camera.stop_preview()
		sleep(5)
except KeyboardInterrupt:
	print("Stopping the QR code scanner.")
	camera.stop_preview()
