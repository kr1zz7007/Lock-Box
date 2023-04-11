import oauth


class ManageOauth:
    def __init__(self):
        return None

    def __enter__(self):
        return self

    def create_new_acc(self, AccName, URI):
        new_totp = oauth.runOAuth([URI]).strip().split('\n')[-1]
        return f"Success,{new_totp}"

    def get_totp(self, AccName):
        totp = oauth.runOAuth(['--account', AccName]).strip()
        return totp

    def __exit__(self, exc_type, exc_value, traceback):
        return self
