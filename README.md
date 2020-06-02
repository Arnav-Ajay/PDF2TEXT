# Extraction of Data from PDF files

Developed using Python3.6 on Ubuntu-18.04 System

# Installing and Running

RUN pip install -r requirements.txt, after cloning the directory

Main implementation is in views.py and helper.py under pdf_extraction/extraction/

The media directory contains input and output files

To run, type: 
    python3 manage.py runserver

# Directory Structure
.
└── pdf_extraction
    ├── db.sqlite3
    ├── extraction
    │   ├── admin.py
    │   ├── apps.py
    │   ├── helper.py                helper file with basic functions
    │   ├── __init__.py
    
    │   ├── migrations
    │   │   ├── __init__.py
    │   │   └── __pycache__
    │   │       └── __init__.cpython-36.pyc
    │   ├── models.py
    │   ├── __pycache__
    │   │   ├── admin.cpython-36.pyc
    │   │   ├── helper.cpython-36.pyc
    │   │   ├── __init__.cpython-36.pyc
    │   │   ├── models.cpython-36.pyc
    │   │   └── views.cpython-36.pyc
    │   ├── tests.py
    │   └── views.py                Main implementation here
    ├── manage.py
    ├── media                       Contains all input and output files
    │   ├── foo.pdf
    │   ├── img_temp.txt
    │   ├── MultiColumn.pdf
    │   ├── output_images
    │   │   └── out0.jpg
    │   ├── output.txt
    │   ├── Sample_Invoice.pdf
    │   └── Spectro_Report.pdf
    ├── pdf_extraction
    │   ├── asgi.py
    │   ├── __init__.py
    │   ├── __pycache__
    │   │   ├── __init__.cpython-36.pyc
    │   │   ├── settings.cpython-36.pyc
    │   │   ├── urls.cpython-36.pyc
    │   │   └── wsgi.cpython-36.pyc
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── README.md
    └── requirement.txt

9 directories, 34 files
