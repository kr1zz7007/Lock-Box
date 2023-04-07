import json
from functions import *


class ManagePassword:
    def __init__(self, Password):
        # TODO Get File, convert it to stream and decrypt
        # print("Hi")
        # print(Password)
        self.DecryptedFile = [{"label":"Website","children":[{"label":"Programming","children":[{"label":"Extras","children":[{"label":"Miscellanoues","children":[{"label":"some stuff","children":[{"Name":"AccName","Username":"UsrName","Password":"UsrPass","URL":"URL","2FA":"TFA"}]}]}]},{"label":"AHHH","children":[{"label":"AccName","Name":"AccName","Username":"UsrName","Password":"UsrPass","URL":"URL","2FA":"TFA"}]}]}]}]
        print('')

    def __enter__(self):
        return self

    def write_key(self, AccName, UsrName, UsrPass, URL, Path, TFA):
        # !! Path will be in the format 'Folder1/Folder2/Entry'
        ENTRYKEY = {"label": AccName, "Username": UsrName,
                    "Password": UsrPass, "URL": URL, "2FA": TFA}
        if Path != '':
            # * For elements with Path
            Path = Path.split('/')
            EntryObj = create_nested_object(Path, ENTRYKEY)
            self.DecryptedFile = merge_obj(EntryObj, self.DecryptedFile)

        else:
            self.DecryptedFile.append(ENTRYKEY)

    def __exit__(self, self1, self2, self3):
        # TODO
        # print(dumps(self.MergedObj))
        print(json.dumps(self.DecryptedFile))
        print('')


with ManagePassword('P') as MP:
    MP.write_key('x', 'x', 'x', 'x', 'Website/Misc', 'True')
    MP.write_key('y', 'y', 'y', 'y', '', 'False')
