import sys
import json 
import qrcode
import requests

from PIL import Image
from escpos.printer import Usb
from resizeimage import resizeimage
from config import URL, CHANNEL_ID

def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content

def send_message(text):
    url = URL + "sendMessage?text={}&chat_id={}&parse_mode={}".format(text, CHANNEL_ID, 'markdown')
    get_url(url)


def main():
  
  if len(sys.argv) == 19:
    try:
      file_name = sys.argv[1]
      gdrive_link = sys.argv[-1:][0].split('&')[0]

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

      qr.print_ascii()

      # printing image
      printer.set(align='center')
      printer.text("\nNunta Stefan si Catalina\n")
      printer.text("Scaneaza codul QR\npentru poza color!\n")
      printer.image(new_file_name)
      printer.cut()
    except Exception as e: 
      gdrive_link = sys.argv[-1:][0].split('&')[0]
      send_message("`Eroare la printare:` %s" %(e))
      qr = qrcode.QRCode(
          version=1,
          error_correction=qrcode.constants.ERROR_CORRECT_L,
          box_size=7,
          border=1,
      )
      qr.add_data(gdrive_link)
      img = qr.make_image()
      img.save("error_qr.png")

  else:
    print("Invalid argument count.")
if __name__ == "__main__":
    main()
