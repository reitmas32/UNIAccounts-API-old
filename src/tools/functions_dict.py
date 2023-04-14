def get_from_dict(dictionary: dict, key: str, default_value = ''):
    value = dictionary.get(key)
    
    if value == None:
        return default_value
    return value