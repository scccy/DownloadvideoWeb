def find_dict_key(json, key):
    if not isinstance(json, dict):
        return None
    if key in json.keys():
        return key
    ans = None
    for json_key in json.keys():
        r = find_dict_key(json[json_key], key)
        if r is None:
            continue
        else:
            ans = "{}.{}".format(json_key, r)
    return ans
