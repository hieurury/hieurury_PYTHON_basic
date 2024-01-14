import qrcode

# Dữ liệu bạn muốn chuyển thành mã QR
data = {
    "name": "hieurury",
    "age": 19,
    "email": "hieurury007@gmail.com",
    "phone": "0329878030"
}

# Tạo đối tượng mã QR
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Thêm dữ liệu vào mã QR
qr.add_data(data)
qr.make(fit=True)

# Tạo hình ảnh mã QR bằng thư viện Pillow (PIL)
img = qr.make_image(fill_color="black", back_color="white")

# Lưu hình ảnh mã QR vào một tệp tin
img.save("hieurury.png")
