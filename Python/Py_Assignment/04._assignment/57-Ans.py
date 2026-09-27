#-----------------------------------------------------------#
#-----------------Q57. File Type Detector-------------------#
#-----------------------------------------------------------#
extension = input("Enter file extension: ")

match extension:
    case "py":
        print("Python File")
    case "txt":
        print("Text File")
    case "pdf":
        print("PDF File")
    case "jpg":
        print("Image File")
    case _:
        print("Unknown File Type")