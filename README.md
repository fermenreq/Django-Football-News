# Django-Football-News

This is an academic project which shows a simply web application about football news

The following requirements are mandatory to run this project:
Python 2.7.12
Django 1.10
Bs4

-----------------------------------------------------------------
We built a web application that the database (SQLite) is updated by the information retrieved from the web http://www.mundodeportivo.com.
We have to make web scraping with the tool call BeautifulSoup. 

It is necessary to have the Crispy Forms module installed to deploy the server with no issues. (__Pip install - update django-crispy- forms__)

To run the app, first be sure you have installed the minimun requirements. and then run the server with the following steps: 
  - cd mundoDeportivo/src/src 
  - python manage.py runserver
  
 If all be alright, you will see a connection log like this:
 
 Performing system checks...

System check identified no issues (0 silenced).
January 14, 2017 - 01:01:57
Django version 1.10.3, using settings 'src.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

The Script call "SaveData.py" is the responsible to capturing the data and storing on the BD. Due to the large amount of data, we have modified the script's pagination value to a constant. If you want all the data, you must only comment the line. See SaveData.py script output
 
