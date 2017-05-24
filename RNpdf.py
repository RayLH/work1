#-*- coding: utf-8  -*-
from pyPdf import PdfFileWriter, PdfFileReader
import pyPdf
import os
for fileName in os.listdir('E:\python_sp\mypdf'):
    pathfile = 'E:\\python_sp\\mypdf\\'+fileName
    actfile = file(pathfile, 'rb')
    try:
        if fileName.lower()[-3:] != "pdf":
            continue
        input1 = pyPdf.PdfFileReader(actfile)
        # print the title of document1.pdf
        print  "##1",fileName,"##2",input1.getDocumentInfo().title
    except Exception,e:
        print Exception,":", e

    try:
        trgtfilename = input1.getDocumentInfo().title + ".pdf"
    except:
        print "\n## ERROR ## %s Title could not be extracted. PDF file may be encrypted!" % fileName


    del input1
    actfile.close()

    print "Trying to rename from:", fileName, '\n to', trgtfilename

    newnamepath = 'E:\\python_sp\\mypdf\\'+trgtfilename
    try:
        os.rename(pathfile,newnamepath)
    except:
        print fileName, 'could not be renamed!'
        print '\n## ERROR ## Maybe the filename already exists or the document is already opened!'

