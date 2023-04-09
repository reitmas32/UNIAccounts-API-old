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

### **Run Local DataBase With Docker**
```bash
# Run and Build Image with volumes
docker run -d -p 27017:27017 -v $ABS_ROUTE_OF_PROJECT/UNICA-ManagerAccounts-API/DB:/data/db --name database mongo
```

### **Run Server With Docker**

```bash
# Build Image
docker build -t unica-acounts-api .

#Run Image
docker run -it -p 7000:4000 unica-acounts-api
```

### **Endpoints Dev Status**
| Method |             Endpoint            | Status |
| ------ |:-------------------------------:| ------:|
| POST   |         /api/v1/singup/         |      ✓ |
| DELETE |         /api/v1/singup/         |      × |
| PUT    |         /api/v1/singin/         |      ✓ |
| GET    |         /api/v1/singin/         |      ✓ |
| POST   | /api/v1/singup-change-password/ |      × |
| PUT    | /api/v1/singup-change-password/ |      × |