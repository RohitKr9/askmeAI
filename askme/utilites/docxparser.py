import docx2txt

def getText(docxfile):

    content = docx2txt.process(docxfile)
    print(content)
    return content