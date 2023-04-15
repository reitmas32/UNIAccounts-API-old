from werkzeug.security import generate_password_hash, check_password_hash

import tools.functions_dict as TOOLS_Dict

class User:
    nick_name= '' 
    password= '' 
    email= '' 
    name = '' 
    last_name_fathers = '' 
    last_name_mothers= '' 
    account_number= '' 
    careers= '' 
    role = '' 
    role_key= '' 
    half_year = 0
    def __init__(self,nick_name='',password='',email='',name ='',last_name_fathers ='',last_name_mothers='',account_number='',careers='',role ='',role_key='',half_year =''):
                self.nick_name = nick_name
                self.password = password
                self.email = email
                self.name  = name 
                self.last_name_fathers  = last_name_fathers 
                self.last_name_mothers = last_name_mothers
                self.account_number = account_number
                self.careers = careers
                self.role  = role 
                self.role_key = role_key
                self.half_year = half_year

    @staticmethod
    def from_dict_password_nohash(obj: dict):
        
        
        user = User.from_dict(obj)
        user.password = str(TOOLS_Dict.get_from_dict(obj, "password"))

        return user
    
    @staticmethod
    def from_dict(obj: dict):
        # Auth
        nick_name           = str(TOOLS_Dict.get_from_dict(obj, "nick_name"))
        password            = generate_password_hash(str(TOOLS_Dict.get_from_dict(obj, "password")))
        # Email
        email               = str(TOOLS_Dict.get_from_dict(obj, "email"))
        
        # Name
        name                = str(TOOLS_Dict.get_from_dict(obj, "name")).upper()
        last_name_fathers   = str(TOOLS_Dict.get_from_dict(obj, "last_name_fathers")).upper()
        last_name_mothers   = str(TOOLS_Dict.get_from_dict(obj, "last_name_mothers")).upper()
        
        # Data Academic
        account_number      = str(TOOLS_Dict.get_from_dict(obj, "account_number"))
        careers             = str(TOOLS_Dict.get_from_dict(obj, "careers"))
        half_year           = int(TOOLS_Dict.get_from_dict(obj, "half_year", default_value = 0))
        
        # Permissions
        role                = str(TOOLS_Dict.get_from_dict(obj, "role"))
        role_key            = str(TOOLS_Dict.get_from_dict(obj, "role_key"))
        return User(nick_name,password,email,name ,last_name_fathers ,last_name_mothers,account_number,careers,role ,role_key,half_year)
    
    def __dict__(self):
        data = {
            'nick_name'         : self.nick_name,
            'password'          : self.password,
            'email'             : self.email,
            'name'              : self.name,
            'last_name_fathers' : self.last_name_fathers,
            'last_name_mothers' : self.last_name_mothers,
            'account_number'    : self.account_number,
            'careers'           : self.careers,
            'half_year'         : self.half_year,
            'role'              : self.role,
            'role_key'          : self.role_key,
        }
        
        return data
    
