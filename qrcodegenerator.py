import qrcode as qr
mode = input(
    "Which type of qr you want to create? (1-For Black And White, 2-For Colored) ")
if (mode == "1"):
    str = input("Enter the data you want to put in the qrcode. \n")
    img = qr.make(str)
    img.save("qrcode.png")
    print("QR Code Generated.")
elif (mode == "2"):
    qr = qr.QRCode(
        version=1,
        error_correction=qr.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    str = input("Enter the data you want to put in the qrcode. \n")
    qr.add_data(str)
    qr.make(fit=True)
    back=input("Enter background color of the qr->")
    fore=input("Enter foreground color of the qr->")
    img = qr.make_image(fill_color=back, back_color=fore)
    img.save("qrcodecolored.png")
    print("Colored QR Code Generated.")