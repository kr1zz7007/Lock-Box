from json import dumps, loads
from functions import *
from oauth_functions import ManageOauth


class ManagePassword:
    def __init__(self, Password):
        self.Password = Password
        self.DecryptedFile = loads(decrypt_file(self.Password))

    def __enter__(self):
        return self

    def read_key(self):
        return self.DecryptedFile

    def get_favourites(self):
        favourite_label_infos = get_favorites_labels(self.DecryptedFile)

        return favourite_label_infos

    def edit_key(self, Accname, NewAccName=None, UsrName=None, UsrPass=None, URL=None, Path=None, TFA=None, Favourites=None):
        edit_label(self.DecryptedFile, Accname, new_label=NewAccName, new_username=UsrName,
                   new_password=UsrPass, new_url=URL, new_tfa=TFA, new_favourites=Favourites)

    def write_key(self, AccName, UsrName, UsrPass, URL, Path, TFA, Favourites, QRURI=None):
        # NOTE Path will be in the format 'Folder1/Folder2/Entry'
        ENTRYKEY = {"label": AccName, "Username": UsrName,
                    "Password": UsrPass, "URL": URL, "2FA": TFA, "Favourites": Favourites}

        # * Adding 2FA
        if TFA == True:
            with ManageOauth() as MOauth:
                MOauth.create_new_acc(AccName, QRURI)

        # * Checking if name exists
        label_info = get_label_info(self.DecryptedFile, AccName)

        if len(label_info) == 0 or label_info[1] == None:
            if Path != '':
                # * For elements with Path
                Path = Path.split('/')
                entry_obj = create_nested_object(Path, ENTRYKEY)

                self.DecryptedFile = merge_obj(entry_obj, self.DecryptedFile)

            else:
                self.DecryptedFile.append(ENTRYKEY)

            encrypt_file(self.DecryptedFile, self.Password)

            # * Set self.DecryptedFile again
            self.DecryptedFile = loads(decrypt_file(self.Password))

            return 'Success'
        else:
            return 'Name already exists'

    def delete_key(self, label):
        if delete_label(self.DecryptedFile, label) == True:
            return 'Success'
        else:
            return 'Failed'

    def __exit__(self, exc_type, exc_value, traceback):
        print(dumps(self.DecryptedFile))
        return self


with ManagePassword('Hello') as MP:
    # print(MP.get_favourites())
    # MP.edit_key(Accname='Programming', Favourites='False')
    # print(MP.write_key('Chess', 'kr1zzler', 'Chess@132',
    #       'chess.com', 'Website/Programming', 'False', 'False'))
    print(MP.delete_key('Chess'))
