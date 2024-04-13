import dropbox
import glob, os
#code --extensions-dir D:/VSCodeExtensions to open vscode with new extension location

#print("This should connect to my dropbox")
#print(os.path.expanduser("~"))
print("Enter date with dashes")
date = input()
dbx = dropbox.Dropbox("sl.BzSyo0VyFmfygaYHJGKwyy9Oa7jgIP-PnNfTBHVs9xWdFCqIRGgzZTFsKMdncYZYIfEemvOkrLjfUFDTu1bWJIJy1yZp6223TJ7wb_9Wbiar8UmTMYHouF1QiCSRP_zX_tDwol5_YPRa")
#print(dbx.users_get_current_account())

#this was taken from stack overflow : https://stackoverflow.com/questions/23894221/upload-file-to-my-dropbox-from-python-script 
def upload_file():
        """upload a file to Dropbox using API v2
        """
        for file in glob.glob(os.path.expanduser("~/Documents/Square Enix/FINAL FANTASY VII Steam/user_8888305/*.ff7")) :
            with open(file, 'rb') as f:
                dbx.files_upload(f.read(), "/FF7 Saves/("+ date + ")" + os.path.basename(file))
            
#--------------------------------------------------------

upload_file()