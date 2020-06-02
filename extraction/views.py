from django.shortcuts import render
from django.http import HttpResponse

from . import helper as h

import pytesseract
from PIL import Image
from pdf2image import convert_from_path

#    path to media files
PATH_TO_MEDIA = '/home/oem/rest-api/pdf_extraction/media/'

#    input and output file names
input_pdf = "Spectro_Report.pdf"
output_file = "output.txt"

#    Home page
def main(request):
    return HttpResponse('<h2>Hey!! Welcome</h2>')

#    Extraction of images from PDF files
def get_image_data(request):
    
    #    helper function for extracting pdf content as images
    input_images = h.extract_images(input_pdf, PATH_TO_MEDIA)
    
    #    helper function for extracting data from images
    h.extract_data(input_images, PATH_TO_MEDIA)

    #    Removing Empty Lines
    with open(PATH_TO_MEDIA + "img_temp.txt") as infile, open(PATH_TO_MEDIA + output_file, 'w') as outfile:
        for line in infile:
            if not line.strip(): continue  # skip the empty line
            outfile.write(line)

    return HttpResponse('<h2> Check "media" directory for output file, titled: "' + output_file + '"</h2>')