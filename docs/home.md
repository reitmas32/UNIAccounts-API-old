# **API to Manage UNICA System Accounts**

## **Information**

This is a API to Manage Accounts<br><br>
****
## **EndPoints** <br><br>

<style>
.v2-module__resource_url--lxU3z {
    font-size: 1.4em;
    margin: .25em 0;
    font-family: Monaco,Menlo,Consolas,Courier New,monospace;
}

.text_endpoint {
    font-size: 1.4em;
    margin: .25em 0;
    font-family: Monaco,Menlo,Consolas,Courier New,monospace;
}

.v2-module__resource_url_method--POST {
    text-transform: uppercase;
    background-color: rgbA(102, 255, 153, 1.0);
    color: #000;
    border-radius: 3px;
    padding: 4px 8px
}

.v2-module__resource_url_method--DELETE {
    text-transform: uppercase;
    background-color: red;
    color: #fff;
    border-radius: 3px;
    padding: 4px 8px
}

.v2-module__resource_url_method--GET {
    text-transform: uppercase;
    background-color: rgba(0,116,236,1.0);
    color: #fff;
    border-radius: 3px;
    padding: 4px 8px
}

.v2-module__resource_url_method--PUT {
    text-transform: uppercase;
    background-color: rgbA(255, 204, 0, 1.0);
    color: #000;
    border-radius: 3px;
    padding: 4px 8px
}

</style>

## Create Acount *SingUp*

<p class="v2-module__resource_url--lxU3z">
    <span class="v2-module__resource_url_method--POST">POST</span> <code>https://unica-accounts.com/api/v1/singup/</code>
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
    "half_year": 4
}

```

<p class="text_endpoint">
    &emsp; - Response 200 OK
</p>

```json
{
    "message": "Succesfull SingUp",
    "status_code": 200
}

```

<p class="text_endpoint">
    &emsp; - Response 500 ERROR
</p>

```json
{
    "message": "Error SingUp",
    "status_code": 500
}

```

<h2>
    Table Types
</h2>
<p class="text_endpoint">
    &emsp; - Request
</p>

| Name              |         Description        |     Type |
| ----------------- |:--------------------------:| --------:|
| nick_name         |   NickName of User SingUp  |   String |
| password          |    Password of New User    |   String |
| email             |      Email of New User     |  *String |
| name              |      Name of New User      |   String |
| last_name_fathers |    Last Name of New User   |   String |
| last_name_mothers |    Last Name of New User   |   String |
| account_number    | Number Account of New User |   String |
| careers           |     Careers of New User    |   String |
| half_year         |      Half Year 1 to N      | *Integer |


<p class="text_endpoint">
    &emsp; - Response
</p>

| Name        |     Description     |    Type |
| ----------- |:-------------------:| -------:|
| message     | Message of Response |  String |
| status_code |   Status Code HTTP  | Integer |
| jwt         |    JSON Web Token   |  String |

****

## Detele Acount *SingUp*

<p class="v2-module__resource_url--lxU3z">
    <span class="v2-module__resource_url_method--DELETE">DELETE</span> <code>https://unica-accounts.com/api/v1/singup/</code>
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
****


## Login Acount *SingIn*

<p class="v2-module__resource_url--lxU3z">
    <span class="v2-module__resource_url_method--PUT">PUT</span> <code>https://unica-accounts.com/api/v1/singin/</code>
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
    "message": "Succesfull SingIn",
    "status_code": 200,
    "jwt": "juasdhasdaj548456ad3ad64",
}

```

<p class="text_endpoint">
    &emsp; - Response 500 ERROR
</p>

```json
{
    "message": "Error SingIn",
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

****

## Check Acount *SingIn*

<p class="v2-module__resource_url--lxU3z">
    <span class="v2-module__resource_url_method--GET">GET</span> <code>https://unica-accounts.com/api/v1/singin/</code>
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
    "jwt": "juasdhasdaj548456ad3ad64*",
}

```
**Notes:**<br>
- For Check Authentication is necessary ``jwt``
<br><br>

<p class="text_endpoint">
    &emsp; - Response 200 OK
</p>

```json
{
    "message": "Succesfull Check Sesion",
    "status_code": 200,
    "status_sinin": true,
}

```
```json
{
    "message": "Succesfull Check Sesion",
    "status_code": 200,
    "status_sinin": false,
}

```

<p class="text_endpoint">
    &emsp; - Response 500 ERROR
</p>

```json
{
    "message": "Error SingIn",
    "status_code": 500
}

```

<h2>
    Table Types
</h2>
<p class="text_endpoint">
    &emsp; - Request
</p>

| Name      |      Description     |   Type |
| --------- |:--------------------:| ------:|
| nick_name |   NickName of User   | String |
| jwt       | Password of New User | String |
<p class="text_endpoint">
    &emsp; - Response
</p>

| Name         |     Description     |    Type |
| ------------ |:-------------------:| -------:|
| message      | Message of Response |  String |
| status_code  |   Status Code HTTP  | Integer |
| status_sinin | Status Code Session |    Bool |
****