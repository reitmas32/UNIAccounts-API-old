# UNICA-ManagerAccounts-API
API to Manage UNICA System Accounts

## Instructions by Run Server Flask

### **Create Env**
```bash
python -m venv venv
```

### **Activate Env**
```bash
#Linux bash/zsh
source venv/bin/activate

#Windows cmd
venv\Scripts\activate.bat

#Windows PowerShell
venv\Scripts\activate.ps1
```

### **Install dependencies**

```bash
pip3 install -r requirements.txt
```
### **Run Server App**

```bash
# Debug Mode
flask --app src/app --debug run

#Release Mode
flask --app src/app run
```