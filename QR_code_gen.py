import pyqrcode
def qrcode():
    s="hii aman your code execute sucessfully:   aman8894420983@gmail.com"
    d=pyqrcode.create(s)
    d.png("my_img.png",scale=6)
    print("your code execute sucessfully")
if __name__=='__main__':
    qrcode()