import pymupdf

def getText(pdffile):
    pdf = pymupdf.open(stream=pdffile, filetype='pdf')
    content = '' 
    for page in pdf:
        content += page.get_text()
    pdf.close()

    print(content)
    return content