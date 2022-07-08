# codeScanner

This project serves as a UI wrapper for the OSS Review Toolkit (ORT)

# Architecture:
I have split the code into three modules. The backend, frontend and the middleware

```

*
|_backend
|_frontend
|_middleware

```

## backend:
The backend is the the code for the  ORT scanner that I have cloned from their official repo. Link to the repo is <a href="https://github.com/oss-review-toolkit/ort">here</a>. It should be noted that I have dockerized the code for development ease.

## frontend:
The frontend is to be built using react. This is something that I will work on at a later time. My current priority is getting the middleware up and running.

## middleware:
The middleware is in Flask. This is somthing that I am actively working to get completed on priority.

Feel free to poke about my code and use it. Do give credits though :)