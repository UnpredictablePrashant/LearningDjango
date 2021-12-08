# LearningDjango
Quick guide to start with learning Django

## Installing Django

```
pip install Django==3.2.9
```


## Creating a project

```
django-admin startproject blog
```

This will create a folder called as blog and inside which there will be folder `blog` and `manage.py`


## Understanding the structure
<p>
manage.py − This file is kind of your project local django-admin for interacting with your project via command line (start the development server, sync db...).<br>
__init__.py − Just for python, treat this folder as package.<br>
settings.py − As the name indicates, your project settings.<br>
urls.py − All links of your project and the function to call. A kind of ToC of your project.<br>
wsgi.py − If you need to deploy your project over WSGI.<br>
asgi.py – Successor of wsgi supports multiple protocols apart from async fashion.<br>
</p>

## Running Django App
```
python manage.py runserver
```

## Creating an app

```
python manage.py startapp blogpage
```

Apps are standalone module which can be used in other places in the project.

## Hello World
<p>
Go inside views.py create a hello world function.<br>
When a page is requested, Django creates an HttpRequest object that contains metadata about the request. <br>
Then Django loads the appropriate view, passing the HttpRequest as the first argument to the view function. <br>
Each view is responsible for returning an HttpResponse object. <br>
Create a file called as urls.py inside the app folder which you created (in our case it is `blogpage`).<br>
Add the urlpattern for the function that you created. Later on we will add this on the project configuration.<br>
Finally configure the urls.py file inside the  project folder (in our case that would be blog folder).<br>
Here we will create the route and add the instance of urls.py from the app folder (`blogpage`).<br>
Run the server!
</p>