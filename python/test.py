from json import dumps

def merge_obj(obj, OriginalArr):
    arr = OriginalArr  # make a copy of the original array
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


obj = {'label': 'Website', 'children': [{'label': 'Programming', 'children': [{'label': 'y', 'Username': 'y', 'Password': 'y', 'URL': 'y', '2FA': 'False'}]}]}
arr = [{"label":"Website","children":[{"label":"Programming","children":[{"label":"Extras","children":[{"label":"Miscellanoues","children":[{"label":"some stuff","children":[{"Name":"AccName","Username":"UsrName","Password":"UsrPass","URL":"URL","2FA":"True"}]}]}]}]}]}]

print(dumps(merge_obj(obj, arr)))