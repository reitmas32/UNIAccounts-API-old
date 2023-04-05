## Create Acount *SingUp*

<p class="route_text">
    <span class="method-POST">POST</span> <code>https://unica-accounts.com/api/v1/singup/</code>
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