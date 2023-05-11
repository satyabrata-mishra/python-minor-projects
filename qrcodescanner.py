import cv2
str=input("Enter the name of qrcode present in the folder -> ")
val, points, straight_qrcode=cv2.QRCodeDetector().detectAndDecode(cv2.imread("qrcodecolored.png"))
print(val)