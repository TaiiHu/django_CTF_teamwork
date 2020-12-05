# django_ctf_teamwork
练习django

todo:
1. django配置
2. django普通业务代码
3. ctf相关功能
4. docker和c++
----
+ `` $ django-admin startproject mysite``
+ `` $ python manage.py runserver``
+ `` $ python manage.py runserver 0:8000``
+ `` $ python manage.py runserver 8080``
+ `` $ python manage.py startapp polls``
+ `` $ python manage.py migrate`` #检查INSTALLED_APP设置，**自动**为其中的每一个应用创建需要的数据表
+ 使用app/models.py创建数据库模型
+ `` $ python manage.py makemigrations app_name`` # Django会检测对模型文件的修改，并且把修改的部分储存为一次迁移
+ `` $ python manage.py sqlmigrate polls 0001`` # 输出将要迁移的SQL语句
+ `` $ python manage.py check`` # 检查项目中的问题

改变模型需要这三步：

    编辑 models.py 文件，改变模型。
    运行 python manage.py makemigrations 为模型的改变生成迁移文件。
    运行 python manage.py migrate 来应用数据库迁移。

