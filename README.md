
# Notes

A site for personal notes.
Writing, viewing and deleting notes. Viewing the history of notes written (including those that have been deleted), an administrator can view the history of all users.
Includes full authentication, different access rights for certain pages, for certain users.

## Language: 

Advanced Python.

## Libraries and more: 

**Flask**, 
**Pandas**, 
**Re**, 
**CSV**, 
**werkzeug.security**, 
**flask_login**, 
**flask_sqlalchemy**, 
**os**

**JINJA templating language & HTML templates**, **Bootstrap**



## How to use:

When you get into the site, you have no access to anything except Log-in and Sign-up.
You are right away navigated to the log-in page.
If your email doesn't exist you are navigated to sign-up.
After login/signup you get access to you home page, logout, and history.
In home page - you can view, add and delete your own notes,
in history page - your can watch all you notes details history since your first registration, includes the ones that have been deleted.
Administrator has access to all-users-history page - in addition to his own history he can watch the history of all users.

## Login:
### administrator - hardCoded:

**email**: tamar3242643@gmail.com

**password**: 123456789

### user:

**email**: t3242643@gmail.com

**password**: 3242643



## Setup & Installation
<sub> Make sure you have the latest version of Python installed. </sub>

> python --version : Python 3.12.1

<sub>install python: https://www.python.org/downloads/</sub>

> python -m django --version : 5.0.1

<sub>install django: pip install django / py -m pip install django</sub>



```
git clone <repo-url>
```
```
pip install -r requirements.txt
```
## Running The App
```
py manage.py migrate
```
```
py manage.py runserver
```

## Viewing The App
Go to http://127.0.0.1:8000


<h3 align="center">* * *</h3>
