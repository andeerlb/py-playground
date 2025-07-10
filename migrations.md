# migrations commands
#### migrate, which is responsible for applying and unapplying migrations.
#### makemigrations, which is responsible for creating new migrations based on the changes you have made to your models.
#### sqlmigrate, which displays the SQL statements for a migration.
# showmigrations, which lists a project’s migrations and their status.

#### Your models will be scanned and compared to the versions currently contained in your migration files, and then a new set # of migrations will be written out. 
`python manage.py makemigrations`


#### Once you have your new migration files, you should apply them to your database to make sure they work as expected:
`python manage.py migrate`

#### If you want to give the migration(s) a meaningful name instead of a generated one, you can use the makemigrations --name # option:
`python manage.py makemigrations --name changed_my_model your_app_label`

#### You can prevent a migration from running in a transaction by setting the atomic attribute to False. For example:
```
from django.db import migrations

class Migration(migrations.Migration):
    atomic = False
```

# Reversing migrations

#### Migrations can be reversed with migrate by passing ## the number of the previous migration. For example, ## to reverse migration books.0003
```
$ python manage.py migrate books 0002
Operations to perform:
  Target specific migration: 0002_auto, from books
Running migrations:
  Rendering model states... DONE
  Unapplying books.0003_auto... OK
```

#### If you want to reverse all migrations applied for an app, use the name zero
```
python manage.py migrate books zero
Operations to perform:
  Unapply all migrations: books
Running migrations:
  Rendering model states... DONE
  Unapplying books.0002_auto... OK
  Unapplying books.0001_initial... OK
```

#### A migration is irreversible if it contains any irreversible operations. Attempting to reverse such migrations will raise IrreversibleError
```
$ python manage.py migrate books 0002
Operations to perform:
  Target specific migration: 0002_auto, from books
Running migrations:
  Rendering model states... DONE
  Unapplying books.0003_auto...Traceback (most recent call last):
django.db.migrations.exceptions.IrreversibleError: Operation <RunSQL  sql='DROP TABLE demo_books'> in books.0003_auto is not reversible
```