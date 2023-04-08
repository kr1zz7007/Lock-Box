from json import dumps
DecryptedFile = [{"label": "Website", "children": [{"label": "Programming", "children": [{"label": "Extras", "children": [{"label": "Miscellanoues", "children": [{"label": "some stuff", "children": [{"label": "AccName", "Username": "UsrName", "Password": "UsrPass", "URL": "URL", "2FA": "TFA"}]}]}]}, {
    "label": "AHHH", "children": [{"label": "AccName", "Username": "UsrName", "Password": "UsrPass", "URL": "URL", "2FA": "TFA"}]}]}, {"label": "Extras", "children": [{"label": "Discord", "Username": "kr1zz", "Password": "somerandompass", "URL": "https://discord.com/login", "2FA": "True"}]}]}]

def delete_label(data, label):
    for obj in data:
        if obj.get('label') == label:
            data.remove(obj)
            return True
        elif obj.get('children'):
            if delete_label(obj['children'], label):
                if not obj['children']:
                    data.remove(obj)
                return True
    return False
delete_label(DecryptedFile, 'AHHH')
print(dumps(DecryptedFile))
