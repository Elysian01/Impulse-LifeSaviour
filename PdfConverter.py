import tempfile
import os
from pdf2image import convert_from_path
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)

# outputPath = "D:\\IT\\Hackathon\\Impulse\\ML Frontend\\Received_Files\\"
outputPath = "Received_Files\\"


def Convert(PdfFile):
    ImageName, extension = os.path.splitext(PdfFile)
    print("\n", ImageName, "\n", extension)
    with tempfile.TemporaryDirectory() as path:
        images_from_path = convert_from_path(os.path.join(
            outputPath + PdfFile), output_folder=outputPath)
    print("Before Path WOrking")
    Image = os.path.join(outputPath, str(ImageName).strip() + ".png")
    for image in images_from_path:
        image.save(Image, 'PNG')
    print("File Successfully Converter to PNG and Stored")


if __name__ == '__main__':
    Convert('Test3.pdf')
    # pass
