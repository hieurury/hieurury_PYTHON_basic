import cv2
from pyzbar.pyzbar import decode
import json

def read_qr_code(image_path):
    # Đọc ảnh nhận vào
    image = cv2.imread(image_path)

    # lấy dữ liệu từ ảnh QR
    value_img = decode(image)

    # nhận dữ liệu từ mã QR
    for result in value_img:
        data = result.data.decode("utf-8")

        if "'" in data:
    # Thay thế dấu nháy đơn bằng dấu nháy kép
            data = data.replace("'", "\"")

    # đọc dữ liệu json
    data_convert = json.loads(data)
    name = data_convert['age']
    print(name)

# link ảnh
image_path = "./hieurury.png"

# đọc mã QR code
read_qr_code(image_path)
