import dropbox
import glob, os
import config

#print("This should connect to my dropbox")
#print(os.path.expanduser("~"))
print("Enter date with dashes")
date = input()
dbx = dropbox.Dropbox(app_key = config.AppKey, app_secret = config.AppSecret, oauth2_refresh_token = config.RefreshToken)
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
