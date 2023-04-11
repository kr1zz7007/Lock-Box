
# * Imports
from os import urandom
from json import dumps
from base64 import urlsafe_b64encode as B64Encode
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from dotenv import dotenv_values


# * Set Constants
config = dotenv_values(".env")


# * Encrypt file
def encrypt_file(file_data: str, password: str):
    SECRET_KEY = config['SECRET_KEY'].encode()

    # Generate a random salt
    salt = urandom(16)

    # Generate a key using PBKDF2HMAC
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,  # 256-bit key
        salt=salt,
        iterations=480000,  # Recommended number of iterations for PBKDF2HMAC
    )
    key = kdf.derive(SECRET_KEY + password.encode())

    # Use AES-GCM to encrypt the data
    aesgcm = AESGCM(key)
    nonce = urandom(12)  # 96-bit nonce
    ciphertext = aesgcm.encrypt(nonce, dumps(file_data).encode(), None)

    # Write the encrypted data to file
    with open(config['PASSWORD_FILE_PATH'], 'wb') as file:
        file.write(salt + nonce + ciphertext)

    return 'Success'


# * Decrypt file
def decrypt_file(password: str) -> str:
    SECRET_KEY = config['SECRET_KEY'].encode()

    with open(config['PASSWORD_FILE_PATH'], 'rb') as file:
        salt = file.read(16)
        nonce = file.read(12)
        ciphertext = file.read()

    # Generate a key using PBKDF2HMAC
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,  # 256-bit key
        salt=salt,
        iterations=480000,  # Recommended number of iterations for PBKDF2HMAC
    )
    key = kdf.derive(SECRET_KEY + password.encode())

    # Use AES-GCM to decrypt the data
    aesgcm = AESGCM(key)
    try:
        decrypted_file = aesgcm.decrypt(nonce, ciphertext, None).decode()
    except ValueError:
        raise ValueError("Invalid password or file has been tampered with")
    return decrypted_file


# * Create a Nested Object
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


# * Merge an object with an array
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


# * Edit label
def edit_label(data, label, new_label=None, new_username=None, new_password=None, new_url=None, new_tfa=None, new_favourites=None):
    for obj in data:
        if obj['label'] == label:
            if not obj.get('children'):
                if new_label is not None:
                    obj['label'] = new_label
                if new_username is not None:
                    obj['Username'] = new_username
                if new_password is not None:
                    obj['Password'] = new_password
                if new_url is not None:
                    obj['URL'] = new_url
                if new_tfa is not None:
                    obj['2FA'] = new_tfa
                if new_favourites is not None:
                    obj['Favourites'] = new_favourites
                return
        elif obj.get('children'):
            edit_label(obj['children'], label, new_label, new_username,
                       new_password, new_url, new_tfa, new_favourites)
    return None


# * Deletes label
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


# * Get label info
def get_label_info(data, label):
    results = []
    for obj in data:
        if 'label' in obj and obj['label'] == label:
            results.append((obj.get('label'), obj.get('Username'), obj.get(
                'Password'), obj.get('URL'), obj.get('2FA'), obj.get('Favourites')))
        elif 'children' in obj:
            results += get_label_info(obj['children'], label)
    return results


# * Get all labels which have Favourites as True
def get_favorites_labels(data):
    labels = []
    for item in data:
        if isinstance(item, dict):
            if "label" in item and "children" in item:
                if "Favourites" in item and item["Favourites"] == "True":
                    labels += get_label_info(data, item["label"])
                labels += get_favorites_labels(item["children"])
            elif "label" in item:
                if "Favourites" in item and item["Favourites"] == "True":
                    labels += get_label_info(data, item["label"])
    return labels
