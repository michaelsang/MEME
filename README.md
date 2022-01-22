# MEME
The application you build must:

Interact with a variety of complex filetypes. This emulates the kind of data you’ll encounter in a data engineering role.
Load quotes from a variety of filetypes (PDF, Word Documents, CSVs, Text files).
Load, manipulate, and save images.
Accept dynamic user input through a command-line tool and a web service. This emulates the kind of work you’ll encounter as a full stack developer.
This project will give you a hands-on opportunity to practice what you've learned in this course, such as:

Object-oriented thinking in Python, including abstract classes, class methods, and static methods.
DRY (don’t repeat yourself) principles of class and method design.
Working with modules and packages in Python.
As you're building your project, be sure to demonstrate coding best practices for style and documentation. Ensure your code, docstrings, and comments adhere to PEP 8 Standards.


# Quote Engine
The Quote Engine module is responsible for ingesting many types of files that contain quotes. For our purposes, a quote contains a body and an author:

"This is a quote body" - Author
This module will be composed of many classes and will demonstrate your understanding of complex inheritance, abstract classes, classmethods, strategy objects and other fundamental programming principles.

# Quote Format
Example quotes are provided in a variety of files. Take a moment to review the file formats in ./_data/SimpleLines and ./_data/DogQuotes. Your task is to design a system to extract each quote line-by-line from these files.


# Ingestors
An abstract base class, IngestorInterface should define two methods with the following class method signatures:

def can_ingest(cls, path: str) -> boolean

def parse(cls, path: str) -> List[QuoteModel]

Separate strategy objects should realize IngestorInterface for each file type (csv, docx, pdf, txt).

A final Ingestor class should realize the IngestorInterface abstract base class and encapsulate your helper classes. It should implement logic to select the appropriate helper for a given file based on filetype.


# Meme module
The module uses the Pillow library to perform basic image operations. It has following responsibilities:

-Loading of a file from disk.

-Transform image by resizing to a maximum width of 500px while maintaining the input aspect ratio

-Add a caption to an image (string input) with a body and author to a random location on the image.


The class depends on the Pillow library to complete the defined, incomplete method signatures so that they work with JPEG/PNG files.


# Running app
After running app using Flask, the application is accessed on http://127.0.0.1:5000/.  The file "Screenshot of Running Application" is an example. 