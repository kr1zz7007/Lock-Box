from functions import *
import oauth


class ManageOauth:
    def __init__(self):
        return None

    def __enter__(self):
        return self

    def create_new_acc(self, AccName, QRCodePath):
        Path = swap_username(AccName, read_qr_code(QRCodePath))
        # print(Path)
        new_totp = oauth.runOAuth([Path]).strip().split('\n')[-1]
        return f"Success,{new_totp}"

    def get_totp(self, AccName):
        totp = oauth.runOAuth(['--account', AccName]).strip()
        return totp

    def __exit__(self, exc_type, exc_value, traceback):
        return self
