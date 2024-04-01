from pyzbar.pyzbar import decode
from PIL import Image
from picamera import PiCamera
from io import BytesIO
import time
from time import sleep

camera = PiCamera()
camera.start_preview()
sleep(5)
camera.capture('/tmp/image.jpg')
camera.stop_preview()

qr_results = ""

try:
	while True:
		stream = BytesIO()
		camera.capture(stream, format='jpeg')
		stream.seek(0)

		decoded_data = decode(Image.open(stream))

		if decoded_data:
			qr_results = decoded_data[0].data.decode('utf-8')
			print(f"QR Code Detected: {qr_results}")
		else:
			print("Scanning for QR Codes")

		time.sleep(1)
except KeyboardInterrupt:
	print("Stopping QR code scanner...")
finally:
	camera.close()
