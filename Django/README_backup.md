#Django CLI Commands
# Project
django-admin startproject myproject

# App
python manage.py startapp myapp

# Server
python manage.py runserver

# Migration
python manage.py makemigrations
python manage.py migrate
python manage.py showmigrations

# Admin
python manage.py createsuperuser

# Shell / ORM
python manage.py shell

# Check
python manage.py check

# Tests
python manage.py test

# Database
python manage.py dbshell

# Version
python manage.py version

# Help
python manage.py help

# Fields In Django

◆ Text & String Fields
CharField → For short text with a maximum length (e.g. name, title).
TextField → For long text (e.g. description, content).
SlugField → For URL-friendly text (e.g. my-first-blog).
EmailField → For storing & validating email addresses.
URLField → For storing & validating URLs.

◆ Number Fields
IntegerField → Whole numbers (e.g., age = 25).
PositiveIntegerField → Only positive numbers (no negatives).
SmallIntegerField → Small range of integers.
BigIntegerField → Large range of integers.
DecimalField → Fixed decimal numbers (e.g., price = 99.99).
FloatField → Floating-point numbers (approximate decimals).

◆ Date & Time Fields
DateField → Stores only date (YYYY-MM-DD).
TimeField → Stores only time (HH:MM:SS).
DateTimeField → Stores both date and time.
DurationField → Stores time duration (e.g., 2 hours 30 mins).

◆ Boolean & Choices
BooleanField → True / False values.
NullBooleanField → True / False / Null (deprecated, use BooleanField with null=True instead).
ChoiceField → Not a separate field, but you can define choices inside CharField or
IntegerField.

◆ File & Media Fields
FileField → For file uploads.
ImageField → For image uploads (requires Pillow library).

◆ Relational Fields
ForeignKey → One-to-Many relationship (e.g., Blog → Author).
OneToOneField → One-to-One relationship (e.g., User → Profile).
ManyToManyField → Many-to-Many relationship (e.g., Students ↔ Courses).

◆ Miscellaneous Fields
UUIDField → Universally Unique ID (often used as primary key).
BinaryField → For raw binary data (e.g., encrypted data, files).
JSONField → For storing JSON data (supported in PostgreSQL, MySQL 5.7+, SQLite 3.9+).
GenericIPAddressField → Stores IP addresses (both IPv4 & IPv6).


# Retrieving data From database

1.Django ORM QuerySet
2.all() -> Fetches all records
3.get() -> Fetches single record (error if multiple/none)
4.filter() -> Fetches records with condition
5.Use Django Shell output
6.Ordering & Chaining
7.exclude() -> opposite of filer(skip condition)
8.values() -> returns data as dictionaris
9.first() / last() -> get first or last record
10.count() -> total number of records

# Retrieve Data from Database Table ? HTML Templates

1.Define your model in models.py.
2.Run migrations: makemigrations & migrate.
3.Fetch data from DB.
4.Pass data to template via views.py context.
5.Display in HTML