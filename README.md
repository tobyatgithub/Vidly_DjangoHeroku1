# Vidly_DjangoHeroku1
A tutorial on how to create a django web app (movie rating) and deploy via heroku.

2020-12-16:
Made Heroku deployment work! Some important line of code:
```
heroku login 
heroku create

git push heroku main 
heroku run python manage.py makemigrations
heroku run python manage.py migrate

heroku ps:scale web=1
heroku open

heroku ps:scale web=0 # to turn off
```
