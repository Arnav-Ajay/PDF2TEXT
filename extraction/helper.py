import pytesseract
from PIL import Image
from pdf2image import convert_from_path

def extract_images(input_pdf, PATH_TO_MEDIA):

    pages = convert_from_path(PATH_TO_MEDIA + input_pdf)
    images = []
    i = 0

    for page in pages:
        page.save(PATH_TO_MEDIA + "output_images/out" + str(i) + ".jpg", "JPEG")
        img = Image.open(PATH_TO_MEDIA + "output_images/out" + str(i) + ".jpg")
        images.append(img)
        i += 1

    return images

def extract_data(imgs, PATH_TO_MEDIA):

    text_file = open(PATH_TO_MEDIA + "img_temp.txt", "w+")

    for img in imgs:
        text = pytesseract.image_to_string(img)
        print(text)
        text_file.write(text) 

    text_file.close()