from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed
from pdfminer.layout import LAParams, LTFigure

def parse(Layout):

            for out in Layout:
                # check component type
                if isinstance(out, LTFigure):
                    print("there is a LTFigure, recalling function parse() to iterate through it")
                    parse(out)
                if hasattr(out, "get_text"):
                    # writer words into text file
                    with open('doc.txt','a') as f:
                        f.write(out.get_text()+'\n')


if __name__ == '__main__':
    # open a pdf file
    fn = open('pdfminer-docs.pdf', 'rb')
    # create pdf parser
    parser = PDFParser(fn)
    # create pdf document
    doc = PDFDocument()
    parser.set_document(doc)
    doc.set_parser(parser)
    doc.initialize("")

    # find convertible component
    if not doc.is_extractable:
        raise PDFTextExtractionNotAllowed
    else:
        # create resource manager
        resource = PDFResourceManager()
        laparams = LAParams()
        device = PDFPageAggregator(resource, laparams=laparams)
        interpreter = PDFPageInterpreter(resource, device)
        # go through each page
        for page in doc.get_pages():
            # process the page
            interpreter.process_page(page)
            layout = device.get_result()
            # layout is a LTPage object
            parse(layout)

