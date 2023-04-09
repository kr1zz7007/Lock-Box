from cv2 import imread, QRCodeDetector
from re import search

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


def get_label_info(data, label):
    for obj in data:
        if 'label' in obj and obj['label'] == label:
            return (obj.get('Username'), obj.get('Password'), obj.get('URL'), obj.get('2FA'))
        elif 'children' in obj:
            result = get_label_info(obj['children'], label)
            if result is not None:
                return result
    return None


def swap_username(new_username, url):
    match = search(r"otpauth:\/\/totp\/([A-Za-z]+):(.+)\?secret=([A-Za-z0-9]+)&issuer=([A-Za-z]+)", url)
    issuer = match.group(1)
    secret = match.group(3)
    old_username = match.group(2)
    new_url = f"otpauth://totp/{new_username}?secret={secret}&issuer={issuer}"
    return new_url

def read_qr_code(filename):
    image = imread(filename)

    detector = QRCodeDetector()

    data, vertices_array, binary_qrcode = detector.detectAndDecode(image)

    if vertices_array is not None:
        return data
    else:
        return 'There was some Error'