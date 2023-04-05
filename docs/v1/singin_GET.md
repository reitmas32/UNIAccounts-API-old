## Check Acount *SingIn*

<p class="route_text">
    <span class="method-GETGET">GET</span> <code>https://unica-accounts.com/api/v1/singin/</code>
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