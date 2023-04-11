# **API to Manage UNICA System Accounts**

## **Information**

This is a API to Manage Accounts<br><br>
****
## **API Keys**
To consume the API, an API_KEY provided by us is necessary for each of the services, this must be sent in the Headers of each of the requests.

## **EndPoints** <br><br>

<style>
.route_text {
    font-size: 1.4em;
    margin: .25em 0;
    font-family: Monaco,Menlo,Consolas,Courier New,monospace;
}

.text_endpoint {
    font-size: 1.4em;
    margin: .25em 0;
    font-family: Monaco,Menlo,Consolas,Courier New,monospace;
}

.method-POST {
    text-transform: uppercase;
    background-color: rgbA(102, 255, 153, 1.0);
    color: #000;
    border-radius: 3px;
    padding: 4px 8px
}

.method-DELETE {
    text-transform: uppercase;
    background-color: red;
    color: #fff;
    border-radius: 3px;
    padding: 4px 8px
}

.method-GET {
    text-transform: uppercase;
    background-color: rgba(0,116,236,1.0);
    color: #fff;
    border-radius: 3px;
    padding: 4px 8px
}

.method-PUT {
    text-transform: uppercase;
    background-color: rgbA(255, 204, 0, 1.0);
    color: #000;
    border-radius: 3px;
    padding: 4px 8px
}

</style>
## Create Acount *signUp*

<p class="route_text">
    <span class="method-POST">POST</span> <code>https://unica-accounts.com/api/v1/signup/</code>
</p>

<h2>
    Examples
</h2>

<p class="text_endpoint">
    &emsp; - Request
</p>

```json
{
    "nick_name": "UserExample",
    "password": "passwordExample34*",
    "email": "example@email.com",
    "name": "Ruben Rodrigo",
    "last_name_fathers": "Pérez",
    "last_name_mothers": "Acosta",
    "account_number": "316259878",
    "careers": "Ingenieria en Computación",
    "role": "admin",
    "role_key": "sdasad4534junSD",
    "half_year": 4
}

```

<p class="text_endpoint">
    &emsp; - Response 200 OK
</p>

```json
{
    "message": "Succesfull signUp",
    "status_code": 200
}

```

<p class="text_endpoint">
    &emsp; - Response 500 ERROR
</p>

```json
{
    "message": "Error signUp",
    "status_code": 500
}

```

<h2>
    Table Types
</h2>
<p class="text_endpoint">
    &emsp; - Request
</p>

| Name              |             Description            |     Type |
| ----------------- |:----------------------------------:| --------:|
| nick_name         |       NickName of User signUp      |   String |
| password          |        Password of New User        |   String |
| email             |          Email of New User         |  *String |
| name              |          Name of New User          |   String |
| last_name_fathers |        Last Name of New User       |   String |
| last_name_mothers |        Last Name of New User       |   String |
| account_number    |     Number Account of New User     |   String |
| careers           |         Careers of New User        |   String |
| half_year         |          Half Year 1 to N          | *Integer |
| role              |          Role of New User          |   String |


<p class="text_endpoint">
    &emsp; - Response
</p>

| Name        |     Description     |    Type |
| ----------- |:-------------------:| -------:|
| message     | Message of Response |  String |
| status_code |   Status Code HTTP  | Integer |
## Detele Acount *signUp*

<p class="route_text">
    <span class="method-DELETE">DELETE</span> <code>https://unica-accounts.com/api/v1/signup/</code>
</p>

<h2>
    Examples
</h2>

<p class="text_endpoint">
    &emsp; - Request
</p>

```json
{
    "nick_name": "UserExample",
    "password": "passwordExample34*",
    "email": "example@email.com",
    "account_number": "316259878",
}

```
**Notes:**<br>
- For Authentication, only one is necessary  ```nick_name | email | account_number```
<br><br>

<p class="text_endpoint">
    &emsp; - Response 200 OK
</p>

```json
{
    "message": "Succesfull Delete Account",
    "status_code": 200
}

```

<p class="text_endpoint">
    &emsp; - Response 500 ERROR
</p>

```json
{
    "message": "Error to Delete",
    "status_code": 500
}

```

<h2>
    Table Types
</h2>
<p class="text_endpoint">
    &emsp; - Request
</p>

| Name           |         Description        |    Type |
| -------------- |:--------------------------:| -------:|
| nick_name      |      NickName of User      | *String |
| password       |    Password of New User    |  String |
| email          |      Email of New User     | *String |
| account_number | Number Account of New User | *String |


<p class="text_endpoint">
    &emsp; - Response
</p>

| Name        |     Description     |    Type |
| ----------- |:-------------------:| -------:|
| message     | Message of Response |  String |
| status_code |   Status Code HTTP  | Integer |
## Login Acount *signIn*

<p class="route_text">
    <span class="method-PUT">PUT</span> <code>https://unica-accounts.com/api/v1/signin/</code>
</p>

<h2>
    Examples
</h2>

<p class="text_endpoint">
    &emsp; - Request
</p>

```json
{
    "nick_name": "UserExample",
    "password": "passwordExample34*",
    "email": "example@email.com",
    "account_number": "316259878",
}

```
**Notes:**<br>
- For Authentication, only one is necessary  ```nick_name | email | account_number```
<br><br>

<p class="text_endpoint">
    &emsp; - Response 200 OK
</p>

```json
{
    "message": "Succesfull signIn",
    "status_code": 200,
    "jwt": "juasdhasdaj548456ad3ad64",
}

```

<p class="text_endpoint">
    &emsp; - Response 500 ERROR
</p>

```json
{
    "message": "Error signIn",
    "status_code": 500
}

```

<h2>
    Table Types
</h2>
<p class="text_endpoint">
    &emsp; - Request
</p>

| Name           |         Description        |    Type |
| -------------- |:--------------------------:| -------:|
| nick_name      |      NickName of User      | *String |
| password       |    Password of New User    |  String |
| email          |      Email of New User     | *String |
| account_number | Number Account of New User | *String |

<p class="text_endpoint">
    &emsp; - Response
</p>

| Name        |     Description     |    Type |
| ----------- |:-------------------:| -------:|
| message     | Message of Response |  String |
| status_code |   Status Code HTTP  | Integer |
| jwt         |    JSON Web Token   |  String |
## Check Acount *signIn*

<p class="route_text">
    <span class="method-GET">GET</span> <code>https://unica-accounts.com/api/v1/signin/</code>
</p>

<h2>
    Examples
</h2>

<p class="text_endpoint">
    &emsp; - Request
</p>

```bash
AUTH
TOKEN: 'sklndansd548488a4dajndbkabdbasd'
```
**Notes:**<br>
- For Check Authentication is necessary ``jwt``
<br><br>

<p class="text_endpoint">
    &emsp; - Response 200 OK
</p>

```json
{
    "message": "Valid Token",
    "status_code": 200
}

```
```json
{
    "message": "Token Expired",
    "status_code": 200
}

```

<p class="text_endpoint">
    &emsp; - Response 500 ERROR
</p>

```json
{
    "message": "Invalid Token",
    "status_code": 401
}

```

<h2>
    Table Types
</h2>
<p class="text_endpoint">
    &emsp; - Request
</p>

| Name  |      Description     |   Type |
| ----- |:--------------------:| ------:|
| TOKEN | Password of New User | String |
<p class="text_endpoint">
    &emsp; - Response
</p>

| Name         |     Description     |    Type |
| ------------ |:-------------------:| -------:|
| message      | Message of Response |  String |
| status_code  |   Status Code HTTP  | Integer |
## Request Change Password of Acount *signUp*

Send a email to user mail for Change Password of Acount 

<p class="route_text">
    <span class="method-POST">POST</span> <code>https://unica-accounts.com/api/v1/signup-change-password/</code>
</p>

<h2>
    Examples
</h2>

<p class="text_endpoint">
    &emsp; - Request
</p>

```json
{
    "nick_name": "UserExample",
    "email": "example@email.com"
}

```

<p class="text_endpoint">
    &emsp; - Response 200 OK
</p>

```json
{
    "message": "Succesfull Request Change Password of Acount",
    "status_code": 200
}

```

<p class="text_endpoint">
    &emsp; - Response 500 ERROR
</p>

```json
{
    "message": "Error Request Change Password of Acount",
    "status_code": 500
}

```

<h2>
    Table Types
</h2>
<p class="text_endpoint">
    &emsp; - Request
</p>

| Name      |       Description       |   Type |
| --------- |:-----------------------:| ------:|
| nick_name | NickName of User signUp | String |
| email     |    Email of New User    | String |


<p class="text_endpoint">
    &emsp; - Response
</p>

| Name        |     Description     |    Type |
| ----------- |:-------------------:| -------:|
| message     | Message of Response |  String |
| status_code |   Status Code HTTP  | Integer |
## Request Change Password of Acount *signUp*

Change Password of Acount 

<p class="route_text">
    <span class="method-PUT">PUT</span> <code>https://unica-accounts.com/api/v1/signup-change-password/</code>
</p>

<h2>
    Examples
</h2>

<p class="text_endpoint">
    &emsp; - Request
</p>

```json
{
    "nick_name": "UserExample",
    "new_password": "newPassword12*"
}

```

<p class="text_endpoint">
    &emsp; - Response 200 OK
</p>

```json
{
    "message": "Succesfull Change Password of Acount",
    "status_code": 200
}

```

<p class="text_endpoint">
    &emsp; - Response 500 ERROR
</p>

```json
{
    "message": "Error Change Password of Acount",
    "status_code": 500
}

```

<h2>
    Table Types
</h2>
<p class="text_endpoint">
    &emsp; - Request
</p>

| Name         |       Description       |   Type |
| ------------ |:-----------------------:| ------:|
| nick_name    | NickName of User signUp | String |
| new_password | New Password of Account | String |


<p class="text_endpoint">
    &emsp; - Response
</p>

| Name        |     Description     |    Type |
| ----------- |:-------------------:| -------:|
| message     | Message of Response |  String |
| status_code |   Status Code HTTP  | Integer |
