# Proiect MSS

# API Docs

# 📁 Collection: Auth 


## End-point: Authentication
### Method: POST
>```
>http://localhost:9000/api/auth
>```
### Body (**raw**)

```json
{
    "email": "test@example.com",
    "password": "1234"
}
```

### Response: 200
```json
{
    "result": {
        "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ0ZXN0QGV4YW1wbGUuY29tIn0.MUKL-FUJfb2sSqCd0ZV3_vPf7lS3Ec3CfLH2RBXStoc"
    }
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃
# 📁 Collection: Users 


## End-point: Create user
### Method: POST
>```
>http://localhost:9000/api/users
>```
### Body (**raw**)

```json
{
    "name": "Test Testulescu",
    "email": "test@example.com",
    "password": "1234"
}
```

### Response: 400
```json
{
    "message": "Email is already in use",
    "status": 400
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Get user
### Method: GET
>```
>http://localhost:9000/api/users/34572930-e914-470c-a276-3751d4078bd2
>```
### Response: 200
```json
{
    "result": {
        "email": "test@example.com",
        "name": "Test Testulescu",
        "uuid": "34572930-e914-470c-a276-3751d4078bd2"
    }
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃
# 📁 Collection: Groups 


## End-point: Get groups
Get all user groups
### Method: GET
>```
>http://localhost:9000/api/groups
>```
### Response: 200
```json
{
    "results": {
        "groups": [
            {
                "created_by": "test@example.com",
                "expenses": [],
                "members": [
                    {
                        "email": "test@example.com",
                        "name": "Test Testulescu"
                    },
                    {
                        "email": "some-email@example.com",
                        "name": "Nume"
                    }
                ],
                "name": "My trip",
                "uuid": "3c590bca-d626-4aa1-926f-50aa3085999a"
            },
            {
                "created_by": "test@example.com",
                "expenses": [],
                "members": [
                    {
                        "email": "test@example.com",
                        "name": "Test Testulescu"
                    },
                    {
                        "email": "some-email@example.com",
                        "name": "Nume"
                    }
                ],
                "name": "My other trip",
                "uuid": "46883bd4-9466-435e-9b72-b5d726e0fa1d"
            }
        ]
    }
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Create group
Create a new group
### Method: POST
>```
>http://localhost:9000/api/groups
>```
### Body (**raw**)

```json
{
    "name": "My trip",
    "members": [
        "some-email@example.com"
    ]
}
```

### Response: 200
```json
{
    "result": {
        "created_by": "test@example.com",
        "expenses": [],
        "members": [
            {
                "email": "test@example.com",
                "name": "Test Testulescu"
            },
            {
                "email": "some-email@example.com",
                "name": "Nume"
            }
        ],
        "name": "My trip",
        "uuid": "3c590bca-d626-4aa1-926f-50aa3085999a"
    }
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Get group
Get an existing group
### Method: GET
>```
>http://localhost:9000/api/groups/3c590bca-d626-4aa1-926f-50aa3085999a
>```
### Response: 200
```json
{
    "result": {
        "created_by": "test@example.com",
        "expenses": [],
        "members": [
            {
                "email": "test@example.com",
                "name": "Test Testulescu"
            },
            {
                "email": "some-email@example.com",
                "name": "Nume"
            }
        ],
        "name": "My trip",
        "uuid": "3c590bca-d626-4aa1-926f-50aa3085999a"
    }
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Add group member
Add new member to existing group
### Method: POST
>```
>http://localhost:9000/api/groups/3c590bca-d626-4aa1-926f-50aa3085999a/members
>```
### Body (**raw**)

```json
{
    "email": "some-other-email@example.com"
}
```

### Response: 200
```json
{
    "results": {
        "members": [
            {
                "email": "test@example.com",
                "name": "Test Testulescu"
            },
            {
                "email": "some-email@example.com",
                "name": "Nume"
            },
            {
                "email": "some-other-email@example.com",
                "name": "Nume"
            }
        ]
    }
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃
_________________________________________________
Powered By: [postman-to-markdown](https://github.com/bautistaj/postman-to-markdown/)
