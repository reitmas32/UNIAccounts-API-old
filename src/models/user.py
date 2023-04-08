from werkzeug.security import generate_password_hash, check_password_hash


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
    def __init__(self,nick_name,password,email,name ,last_name_fathers ,last_name_mothers,account_number,careers,role ,role_key,half_year):
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
    def from_dict(obj: dict):
        
        if obj.get('account_number') == None:
            return None, 'No account_number send in the request', 428
        if obj.get('password') == None:
            return None, 'No password send in the request', 428
        if obj.get('role') == None or obj.get('role_key') == None:
            return None, 'No role send in the request', 428
        if obj.get('account_number') == None:
            return None, 'No email, nick_name', 428
        # Auth
        nick_name           = str(obj.get("nick_name"))
        password            = generate_password_hash(str(obj.get("password")))
        
        # Email
        email               = str(obj.get("email"))
        
        # Name
        name                = str(obj.get("name")).upper()
        last_name_fathers   = str(obj.get("last_name_fathers")).upper()
        last_name_mothers   = str(obj.get("last_name_mothers")).upper()
        
        # Data Academic
        account_number      = str(obj.get("account_number"))
        if not account_number.isdigit() and len(account_number) != 9:
            return None, 'account_number invalid', 428
        careers             = str(obj.get("careers"))
        half_year           = int(obj.get("half_year"))
        
        # Permissions
        role                = str(obj.get("role"))
        role_key            = str(obj.get("role_key"))
        return User(nick_name,password,email,name ,last_name_fathers ,last_name_mothers,account_number,careers,role ,role_key,half_year), 'Succesful User', 200
    
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
    
