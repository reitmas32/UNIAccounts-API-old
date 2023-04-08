## Check Acount *SingIn*

<p class="route_text">
    <span class="method-GET">GET</span> <code>https://unica-accounts.com/api/v1/singin/</code>
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