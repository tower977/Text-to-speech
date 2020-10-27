#import all required libraries
import pyttsx3
import PyPDF2
import argparse
import sys
#parsing input from command line
file_name = sys.argv[1]
page_num = sys.argv[2]

#open the book in question and store inaa variable
book = open(file_name, 'rb')
#initialize the pdf to python function
pdfReader = PyPDF2.PdfFileReader(book)
#take the number of pages for  reference
pages = pdfReader.numPages
#print(pages)
#initialize speaking functionality
speaker = pyttsx3.init()
for num in range(int(page_num), pages):
    page = pdfReader.getPage(int(page_num))
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
    speaker.runAndWait()
