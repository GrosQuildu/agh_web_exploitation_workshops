# Vulnerable Flask Blog

This is vulnerable web application prepared for this laboratory.

# Prerequisites

1. Docker

# Usage

To build app locally, download source from github
```
git clone https://github.com/GrosQuildu/agh_binary_exploitation_workshops.git
```

Then to run app, just type:

```
cd lab5/idor/src
docker build --tag lab5idor .
docker run -p 80:5000 -d lab5idor
```

Content will be available at http://localhost:80
