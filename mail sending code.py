from tkinter.filedialog import askdirectory
from tkinter import Tk
from pathlib import Path
import os,hashlib
import yagmail

Tk().withdraw()
SMTP_GMAIL_USERNAME = "chittaranjanmore1996@gmail.com"
SMTP_GMAIL_PASSWORD = "Chitta@8275"
RECEIVER_LISIT = "chittaranjanmore96@gmail.com,koradejyoti94@gmail.com" #,"koradejyoti94@gmail.com"

def main():
    path=askdirectory(title="Select a Folder")
    file_list=os.listdir(path)
    unique=dict()
    for file in file_list:
        f=open("log.txt","a")
        file_name=Path(os.path.join(path,file))
        if file_name.is_file():
            fileHash=hashlib.md5(open(file_name,"rb").read()).hexdigest()
            if fileHash not in unique:
                unique[fileHash]=file_name
            else:
                print(file)
                f.writelines(str(file))
                f.write("\n")
                f.close()
                os.remove(file_name)
                print(file_name)
                print("Successfully deleted",(file_name))
        else:
            print("Operation not successful")
    '''
    Below Written code used to send mail to the user 
    '''
    yagmail.register(SMTP_GMAIL_USERNAME,SMTP_GMAIL_PASSWORD)
    yag = yagmail.SMTP(SMTP_GMAIL_USERNAME)
    yag.send(to = RECEIVER_LISIT.split(',') ,subject= 'Log File Of Removed Duplicate Files From User Selected Folder', 
    contents = "Below Attached File Shows Removed Duplicate Files Name.",attachments="log.txt")
    
if __name__=="__main__":
    main()