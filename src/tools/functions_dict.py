######################################################################
# author = Rafael Zamora
# copyright = Copyright 2023, UNICA-ManagerAccounts
# date = 10/04/2023
# license = PSF
# version = 1.0
# maintainer = Rafael Zamora
# email = rafa.zamora.rals@gmail.com
# status = Development
######################################################################

def get_from_dict(dictionary: dict, key: str, default_value = ''):
    """Wrapper to get a dictionary value

    Args:
        dictionary (dict): Data Dictionary
        key (str):
        default_value (str, optional): Default value in case there is no coincidence

    Returns:
        Any: value
    """
    value = dictionary.get(key)
    
    if value == None:
        return default_value
    return value