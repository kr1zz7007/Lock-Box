import json
from functions import *


class ManagePassword:
    def __init__(self, Password):
        # TODO Get File, convert it to stream and decrypt
        self.DecryptedFile = [{"label": "Website", "children": [{"label": "Programming", "children": [{"label": "Extras", "children": [{"label": "Miscellanoues", "children": [{"label": "some stuff", "children": [{"Name": "AccName", "Username": "UsrName", "Password": "UsrPass", "URL": "URL", "2FA": "TFA"}]}]}]}, {
            "label": "AHHH", "children": [{"label": "AccName", "Name": "AccName", "Username": "UsrName", "Password": "UsrPass", "URL": "URL", "2FA": "TFA"}]}]}, {"label": "Extras", "children": [{"label": "Discord", "Username": "kr1zz", "Password": "somerandompass", "URL": "https://discord.com/login", "2FA": "True"}]}]}]
        print('')

    def __enter__(self):
        return self

    def read_key(self):
        return self.DecryptedFile

    def edit_key(self, Accname=None, UsrName=None, UsrPass=None, URL=None, Path=None, TFA=None):
        edit_label(self.DecryptedFile, Accname, new_username=UsrName,
                   new_password=UsrPass, new_url=URL, new_tfa=TFA)

    def write_key(self, AccName, UsrName, UsrPass, URL, Path, TFA):
        # NOTE Path will be in the format 'Folder1/Folder2/Entry'
        ENTRYKEY = {"label": AccName, "Username": UsrName,
                    "Password": UsrPass, "URL": URL, "2FA": TFA}

        if get_label_info(self.DecryptedFile, AccName) == None or get_label_info(self.DecryptedFile, AccName)[0] == None:
            if Path != '':
                # * For elements with Path
                Path = Path.split('/')
                EntryObj = create_nested_object(Path, ENTRYKEY)
                self.DecryptedFile = merge_obj(EntryObj, self.DecryptedFile)

            else:
                self.DecryptedFile.append(ENTRYKEY)

            return 'Success'
        else:
            return 'Name already exists'

    def __exit__(self, exc_type, exc_value, traceback):
        print(json.dumps(self.DecryptedFile))


with ManagePassword('P') as MP:
    print('hji')
    print(MP.write_key('AccName', 'Minion', 'Discord@132', 'discord.com', 'Website/Prod', 'True'))
