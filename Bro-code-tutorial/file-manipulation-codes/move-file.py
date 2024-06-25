import os 

source = r"C:\Users\7000031725\Desktop\AWS Training & Certification - Certificate of Completion.pdf"
destination = r"C:\Users\7000031725\OneDrive - Sony\personal files\certificates\AWS Training & Certification - Certificate of Completion.pdf"
try:
    if os.path.exists(destination):
        print("The file already exists")
    else:
        os.replace(source,destination) # can also move folders with this 
        print("The file has been moved ")
except FileNotFoundError as e :
    print(e)
