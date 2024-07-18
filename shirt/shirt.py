from PIL import Image, ImageOps
import sys

def shirt(image_in, image_out):
    shirt = Image.open("./shirt.png")
    try:
        if image_in.endswith((".jpg",".jpeg",".png")) and image_in.endswith((".jpg",".jpeg",".png")):
            with Image.open(image_in) as image:
                image = ImageOps.fit(image,(600,600))
                if image_in[image_in.find("."):] == image_out[image_out.find("."):]:
                    Image.Image.paste(image, shirt, mask=shirt)
                    image.save(image_out)
                else:
                    sys.exit("Extensions Don't Match")
        else:
            sys.exit("File is of unknown extension.")
    except FileNotFoundError:
        sys.exit("Image Could Not Be Opened")
        
if __name__ == "__main__":
    try:
        if len(sys.argv) > 3:
            sys.exit("Too Many Command Line Arguments.")
        shirt(sys.argv[1],sys.argv[2])
    except IndexError:
        sys.exit("Too Few Command Line Arguments.")