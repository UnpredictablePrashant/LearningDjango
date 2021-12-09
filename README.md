# LearningDjango
Quick guide to start with learning Django

[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FUnpredictablePrashant%2FLearningDjango&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)


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


## Registration Page
<p>
Django has inbuilt models defined for authentication, and authorization and we will use those models to create a registration form. You can find this models stored inside your lib folder under python installation. In my case the complete path is:
`C:\Python39\Lib\site-packages\django\contrib\auth`. Here in `forms.py`, you can see all the forms structure which we will use. <br><br>
Let's start by creating a function called as `register` inside `views.py` and then create a route through `urls.py`.
</p>
```
def register(request):
    f = UserCreationForm()
    return render(request, 'register.html', {'form': f})
```
<p>Create a register.html file inside the templates directory. Once done, start the migration process, which basically setup your database.</p>

```
python manage.py makemigrations
python manage.py migrate
```

Once done, you can check your `postgres` database and you can see tables being created.

```
djangosample=# \dt
                   List of relations
 Schema |            Name            | Type  |  Owner
--------+----------------------------+-------+----------
 public | auth_group                 | table | postgres
 public | auth_group_permissions     | table | postgres
 public | auth_permission            | table | postgres
 public | auth_user                  | table | postgres
 public | auth_user_groups           | table | postgres
 public | auth_user_user_permissions | table | postgres
 public | django_admin_log           | table | postgres
 public | django_content_type        | table | postgres
 public | django_migrations          | table | postgres
 public | django_session             | table | postgres
(10 rows)
```

Now, run the server using `python manage.py runserver`.



# Creating Admin Views

```
python manage.py createsuperuser
```