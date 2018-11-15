from PyPDF2 import PdfFileMerger

merger = PdfFileMerger()

Path = input("Please enter the file path that contains the pdf files")
FileString = input("Please past in the space seperated file list from excel")
#Path = "C:\\Users\\HUFFMANN\\Desktop\\temp--\\test bom merging"
#FileString = "2038308.pdf 2038302.pdf 2038303.pdf 2038330.pdf 2038249.pdf 2038313.pdf 2038334.pdf 2038273.pdf 2002612.pdf 2027433.pdf 2038318.pdf 2038256.pdf 2038270.pdf 2038337.pdf 2038338.pdf 2038272.pdf 2038352.pdf 2038354.pdf 2038740.pdf"
FileList = FileString.split()

for file in FileList:
    merger.append(fileobj = Path+"\\" +file)

merger.write(Path+"\\PrintPackage.pdf")
