# Install PyDrive
# Create Project in GCP, Enable Google Drive API
# Fill the oAuthConscent Form
# Put URI and Redirect URI : http://localhost:8000/
# Download JSON file, put this in the same folder as py code, rename it to client_secrets.json
# Run this piece of code
# To Get folder ID, open folder in browser, look at URL and extract folder ID


from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os

g_login = GoogleAuth()
g_login.LocalWebserverAuth()
drive = GoogleDrive(g_login)

# Delete all Previous APK and IPA files
file_list = drive.ListFile({'q': "'1bEbmdJRq4cf3CwB' in parents and trashed=false"}).GetList()
for file in file_list:
    if str(file['title']) == "customer.apk" or str(file['title']) == "valet.apk":
        # Initialize GoogleDriveFile instance with file id.
        file1 = drive.CreateFile({'id': file['id']})
        file1.Delete()  # Permanently delete the file.


path = '../appfolder'
files = os.listdir(path)
link_urls = []

for file in files:
    with open(path+"/"+file, "r" ,encoding="utf-8") as f:
        fn = os.path.basename(f.name).replace(path,"")
        file_drive = drive.CreateFile({
            'parents': [{'id': '1bEbmdJRq4cf3CwB6j03TnZC99yS3GyoY'}],
            'title': fn})
        file_drive.SetContentFile(f.name)
        file_drive.Upload()

        permission = file_drive.InsertPermission({
            'type': 'anyone',
            'value': 'anyone',
            'role': 'reader',
            'withLink': True})

        # SHARABLE LINK
        link = file_drive['alternateLink']

        # To use the image in Gsheet we need to modify the link as follows
        link = file_drive['alternateLink']
        link = link.split('?')[0]
        link = link.split('/')[-2]
        link = 'https://docs.google.com/uc?export=download&id=' + link

        link_urls.append(fn + " : " + link + '\n')
        print(fn + " : " + link + '\n')

        f.close()


linkText = open(path + "/" + "links.txt", 'w+')
linkText.write("\n".join(link_urls))
linkText.close()
