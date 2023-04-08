def create_nested_object(arr, LastValue):
    obj = {'label': arr[0], 'children': []}
    current_level = obj['children']
    for item in arr[1:]:
        new_level = {'label': item, 'children': []}
        current_level.append(new_level)
        current_level = new_level['children']

    current_obj = obj

    while 'children' in obj and len(current_obj['children']) > 0:
        current_obj = current_obj['children'][-1]
    if 'children' not in current_obj:
        current_obj['children'] = []
    current_obj['children'].append(LastValue)

    return obj


def merge_obj(obj, OriginalArr):
    arr = OriginalArr
    if len(arr) == 0:
        arr.append(obj)
        return arr
    if obj["label"] == arr[0]["label"]:
        for child_obj in obj["children"]:
            found = False
            for child_arr in arr[0]["children"]:
                if "label" in child_arr and child_obj["label"] == child_arr["label"]:
                    merge_obj(child_obj, [child_arr])
                    found = True
                    break
            if not found:
                arr[0]["children"].append(child_obj)
    else:
        arr.append(obj)
    return arr


def edit_label(data, label, new_username=None, new_password=None, new_url=None, new_tfa=None):
    for obj in data:
        if obj['label'] == label:
            if new_username is not None:
                obj['Username'] = new_username
            if new_password is not None:
                obj['Password'] = new_password
            if new_url is not None:
                obj['URL'] = new_url
            if new_tfa is not None:
                obj['2FA'] = new_tfa
            return
        elif 'children' in obj:
            edit_label(obj['children'], label, new_username,
                       new_password, new_url, new_tfa)
