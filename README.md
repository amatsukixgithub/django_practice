![django](https://img.shields.io/badge/-django-2a2d2e.svg?logo=django)
![python](https://img.shields.io/badge/-Python-F9DC3E.svg?logo=python)
![sqlite](https://img.shields.io/badge/-sqlite-informational.svg?&logo=sqlite)
![GitHub repo size](https://img.shields.io/github/repo-size/amatsukixgithub/django_practice)
![GitHub](https://img.shields.io/github/license/amatsukixgithub/django_practice)

![GitHub Repo stars](https://img.shields.io/github/stars/amatsukixgithub/django_practice?style=social)

# django_practice

Django REST frameworkの練習リポジトリ

## System Requirements

以下のライブラリがインストールされている事を前提とします。

```
pip install django
pip install djangorestframework
```

## Usage

クローン
```
git clone https://github.com/amatsukixgithub/django_practice.git
```

マイグレート
```
cd django_practice/

python manage.py migrate
```

起動
```
python manage.py runserver
```

## Sample Request

* POST

image_pathを指定した場合201が返却される
```
curl http://localhost:8000/example.com/ -d '{"image_path":"abc/abc"}' -v -H 'Content-Type:application/json' -XPOST
```

image_pathが空白の場合400が返却される
```
curl http://localhost:8000/example.com/ -d '{"image_path":""}' -v -H 'Content-Type:application/json' -XPOST
```

* GET

一覧取得
```
curl http://localhost:8000/example.com/ -v
```

一件取得
```
curl http://localhost:8000/example.com/1/ -v
```

* PUT

未実装

* DELETE

存在する場合は204が返却され、存在しない場合は404が返却される
```
curl http://localhost:8000/example.com/1/ -v -XDELETE
```
