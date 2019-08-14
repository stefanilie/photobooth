import sys
from PIL import Image

def main():
    if len(sys.argv) == 2:
        #loading image
        file_name = sys.argv[1]
        picture = Image.open(file_name)
 
        #loading frame
        frame = Image.open('rama_foto_02.png').convert('RGB')
        pic_w, pic_h = picture.size
        fr_w, fr_h = frame.size

        #pasing the image to the center of the frame
        offset = ((fr_w - pic_w) // 2, (fr_h - pic_h) // 2)
        frame.paste(picture, offset)

        # saving
        frame.save(file_name)
    else:
        print("Invalid argument count")

if __name__ == "__main__":
    main()
