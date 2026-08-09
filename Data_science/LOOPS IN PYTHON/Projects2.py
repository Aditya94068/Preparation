# import qrcode
# data ="https://www.codewithharry.com/courses/the-ultimate-job-ready-data-science-course/data-transformation-1745501074797"
# qr = qrcode.QRCode(version = 1,error_correction = qrcode.constants.ERROR_CORRECT_H, box_size = 20,border = 5,)
# qr.add_data(data)
# qr.make(fit = True)

# img = qr.make_image(fill_color = "black",back_color="White")
# img.save("My_Learning.png")
import qrcode
data = "https://www.codewithharry.com/courses/the-ultimate-job-ready-data-science-course/data-transformation-1745501074797"
qr = qrcode.QRCode(version = 1 , error_correction = qrcode.constants.ERROR_CORRECT_H,box_size = 10,border=4)
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color = "blue",back_color = "white")
img.save("My_learning.png")