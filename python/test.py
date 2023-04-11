from json import dumps


def delete_label(data, label):
    for obj in data:
        if obj['label'] == label:
            if not obj.get('children'):
                data.remove(obj)
                return True
        elif 'children' in obj:
            if delete_label(obj['children'], label):
                if len(obj['children']) == 0:
                    data.remove(obj)
                return True
    return False



data = [{"label": "Website", "children": [{"label": "Programming", "children": [{"label": "Extras", "children": [{"label": "Miscellanoues", "children": [{"label": "some stuff", "children": [{"label": "AcccccName", "Username": "UsrName", "Password": "UsrPass", "URL": "URL", "2FA": "TFA", "Favourites": "True"}]}]}]}, {"label": "AHHH", "children": [{"label": "AccName", "Username": "UsrName", "Password": "UsrPass", "URL": "URL", "2FA": "TFA", "Favourites": "False"}]}]}, {"label": "Extras", "children": [{"label": "Discord", "Username": "kr1zz",
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         "Password": "somerandompass", "URL": "https://discord.com/login", "2FA": "True", "Favourites": "False"}]}, {"label": "Prod", "children": [{"label": "ARGHH", "Username": "Minion", "Password": "Discord@132", "URL": "discord.com", "2FA": "False", "Favourites": "False"}, {"label": "ARGHHH", "Username": "Minion", "Password": "Discord@132", "URL": "discord.com", "2FA": "False", "Favourites": "True"}, {"label": "Programming", "Username": "Minion", "Password": "Discord@132", "URL": "discord.com", "2FA": "False", "Favourites": "False"}]}]}]

print(delete_label(data, 'Programming'))
print(dumps(data))
