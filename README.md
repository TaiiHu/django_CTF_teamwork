# django_CTF_teamwork
练习django

TODO:
1. Django配置
2. Django普通业务代码
3. CTF相关功能
4. docker和c++
-----
## 2020/12/04/:+django poll demo
+ 新建project：``$ django-admin startproject preject_name``
+ 新建应用：``$ python manage.py startapp newapp_name``
+ 运行服务
  + ``python manage.py runserver`` #默认开启8000端口
  + ``python manage.py runserver 8080`` #指定服务监听的端口
  + ``python manage.py runserver 0:8000`` #服务器监听指定IP和端口（0.0.0.0和8000）

