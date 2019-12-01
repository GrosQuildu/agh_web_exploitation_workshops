# Django JSONField/HStoreField SQL Injection Vulnerability (CVE-2019-14234)

[中文版本(Chinese version)](README.zh-cn.md)

Django released a security update on August 1, 2019, which fixes a SQL injection vulnerability in the two model fields of JSONField and HStoreField.

Reference link:

- https://www.djangoproject.com/weblog/2019/aug/01/security-releases/
- https://www.leavesongs.com/PENETRATION/django-jsonfield-cve-2019-14234.html

The vulnerability requires the developer to use JSONField/HStoreField; moreover, the field name of the queryset can be controlled. Django's built-in application Django-Admin is affected, which gives us an easy way to reproduce the vulnerability.

## Start Vulnerability Application

Compile and start a vulnerable Django 2.2.3 by executing the following command:

```
Docker-compose build
Docker-compose up -d
```

After the environment is started, you can see the home page of Django at `http://your-ip:8000`.

## Vulnerability Reproduce

First, log in to the Django-Admin `http://your-ip:8000/admin/` with username `admin` and password `a123123123`.

Then go to the list-view `http://your-ip:8000/admin/vuln/collection/` of the model `Collection`:

![](1.png)

Add `detail__a'b=123` to the GET parameter, where `detail` is the JSONField:

http://your-ip:8000/admin/vuln/collection/?detail__a%27b=123

You can see that the single quote has been injected successfully, and the SQL statement reports an error:

![](2.png)