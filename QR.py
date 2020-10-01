import pyqrcode
def qrcode():
    inp=pyqrcode.create(input("inter input"))
    inp.png("qrcode .png",scale=6)
    print("QR generated")



if __name__ == '__main__':
    qrcode()