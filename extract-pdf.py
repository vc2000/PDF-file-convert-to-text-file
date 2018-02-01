import PyPDF2

#================= Extract PDF =====================
try:
    pdfFileObj = open('/Users/venuschau/Desktop/code/pdf-txt/pdf-files/2017FallADM570 Syllabus.pdf','rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    print("extracting data to interim...")
    pages = pdfReader.getNumPages()
    for i in range(pages):
        pageObj = pdfReader.getPage(i)
        text = str(pageObj.extractText())

        with open('/Users/venuschau/Desktop/code/pdf-txt/text/download.txt', 'ab') as f:
            f.write(text.encode('utf-8'))
    print("txt data in interim")
except Exception as e:
    print("{} \n {} \n".format("="*30 + " EXTRACT LOG " + "="*30,str(e)))
