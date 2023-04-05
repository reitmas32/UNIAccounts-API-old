## Request Change Password of Acount *SingUp*

Send a email to user mail for Change Password of Acount 

<p class="v2-module__resource_url--lxU3z">
    <span class="v2-module__resource_url_method--POST">POST</span> <code>https://unica-accounts.com/api/v1/singup-change-password/</code>
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
| nick_name | NickName of User SingUp | String |
| email     |    Email of New User    | String |


<p class="text_endpoint">
    &emsp; - Response
</p>

| Name        |     Description     |    Type |
| ----------- |:-------------------:| -------:|
| message     | Message of Response |  String |
| status_code |   Status Code HTTP  | Integer |