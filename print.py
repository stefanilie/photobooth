import sys
import qrcode

from PIL import Image
from escpos.printer import Usb
from resizeimage import resizeimage


def main():

  if len(sys.argv) == 2:
    file_name = sys.argv[0]
    gdrive_link = sys.argv[1]

    # initializing printer
    printer = Usb(0x416, 0x5011)

    # initializing qr code generator
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=4,
        border=1,
    )
    
    # resize image
    picture = Image.open(file_name)
    resizedPicture = resizeimage.resize_height(picture, 375)

    # generating qr
    qr.add_data(gdrive_link)
    qr.make(fit=True)
    img_qr = qr.make_image(fill_color="black", back_color="white")

    # adding qr to resized image
    pos = (resizedPicture.size[0] - img_qr.size[0], resizedPicture.size[1] - img_qr.size[1])
    resizedPicture.paste(img_qr, pos)

    # rotating it for printing and saving the new file
    resizedPicture = resizedPicture.transpose(Image.ROTATE_90)
    new_file_name = file_name + '_rotated_qr.jpg'
    resizedPicture.save(new_file_name)

    # printing image
    printer.image(new_file_name)
    printer.cut()

if __name__ == "__main__":
    main()