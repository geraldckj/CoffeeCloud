# CoffeeCloud
CoffeeCloud with Django
<br>
Run program with: `python manage.py runserver`

To update db: <br>
`python manage.py makemigrations`<br>
`python manage.py migrate`<br>
You can update db structure post creation with migrations. <br>

To run SQL commands:
 <br>
`python manage.py sqlmigrate coffeeCloud 0001`
<br>*0001 is migration number. It's shown when `makemigrations` command is passed.
