# Banking-App

type "virtualenv onlinebankenv" in your anaconda prompt or "python -m venv myvenv"
 in ur cmd - For creating environment in a directory.
navigate into the folder created and type 'Scripts\activate' and it goes into the 
environment
go back out of environment folder by "cd.." and type "django-admin startproject
 'name of project?'"
Root folder or base folder is the folder containing the project folder, they are 
of the same name.
The django automatically creates the project folder inside the root folder and 
they are of the same name.

Django moves from: Template to Urls to View to Model
Templates is interface where the user interacts.
Urls or links
View is where the background process takes place
Model or database is where the data is fetched from
Will always go from view to Templates, can not go from view bact to url

All your projects must have different applications.

An app must have template,view,urls,models and forms.
to run your server on manage python folder 'python manage.py runserver'. It is 
created automatically along with ur project folder
in the base folder.

You can't change your table directly from database in phpmyadmin, It has to be 
from django model we will be working on
You can also only use django forms not html will be allowed.

Next step is to copy the link of local host and paste on your browser. 
It is found in the
There is Development, Testing and Development or deployment project.

You can fill in the site for bank in "ALLOWED_HOSTS" but you would have needed 
permission from the host provider.
auth - authentication is anything about users
admin - is for people behind websites
messages - have been created already, dont have to do anything from scratch. 
This are messages that are displayed for interacting with the user.
staticfiles - 

Under the Email part;
smtp means you want to use email services, while the console is for sending to 
console since you want to be offline.
TLS uses 585 port. while SSH...
If you are using a 3rd party mail, you use their config and add it there
Download mysqlclient 

To migrate models: "python manage.py migrate"

Types of users:
Super User, Staff, Ordinary user
To create a Superuser "python manage.py createsuperuser"
LOGIN PROCEDURES
csrf_token is a form security and sends a token with the details when a user 
logs in. method should always be post.
{{form.as_table}} -  This displays your bootstrap form in a table form.

You work on your login aand password reset pages. And you extend them from one
page to another.

"django-admin startapp nameofapp" to start your different apps.
There are 5 names of apps; customer, staff, transactions, operations and store.
But the first three are the ones to create folder for.

Registration will be created in staff app. Will have to create url for each apps
Text field in HTML = CharField
"help_text" is for user label whether compulsory or not.
You make sure your html files sees your css and local images and links.
Then you create some files under registration.
Since you want all pages to display navbar and all, make sure you cut out the 
changeable ones and put it in a different file
and use some keywords to connect the branched file to the main one so as not to cause 
confusion.
Then you have to connect each pages in the url. 
 
"python manage.py makemigrations" to migrste ur models created in ur app. and then type 
'python manage.py migrate'.
You will see the table on the list.
After all that you go to design form templates for the forms created ot be stored in datbase. 
The templates are created 
in staffapp folder under templates. After making the templates for staff, you go to views and 
set people that can see the forms.
'render' is to tell it which template to load.

HttpResponseRedirect and HttpResponsePermanentRedirect. Render takes it from views to template 
straight. while the former og=f the three
will take it from views to url back to views then to template.

for the login form, this is what is created:
<input type="text" name="username" autofocus="" autocapitalize="none" autocomplete="username" 
       maxlength="150" class="my-username-class" required="" id="id_username">

'POST' is for when the form id filled already while 'GET' is for an empty form
get_object_or_404 is used to get info from the database to help fill a form.	

from view to template, use render. But for a new link u use, HTTpsResponseRedirect, 
if its to redierect to a link with a 
argument, use HttpResponsepermanentRedirect. 

if user.is_authenticated

you can use .get() for one person instead of .all() that u use for many people.
is_valid means if the field is filled correctly, it can easily correct it.
cleaned_data is to collect the field and pass in the model you want to call, but for 
form model, you will need to call each
field, one by one. 

You can use TextField for a for that requires alot of words without a limit.
ForeignKey and OnetoOneField is for relating to other tables.


def registration(request):
	if request.method='POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		new_user = User.objects.create(username=username, password=password)
		new_user.save()
	render(request, "signup.html")


## For use in my post_edit.html second

DJANGO GINGERS
TWILO
drf django restful
try and add logs to the banking app

<!--  -->


                            

processor has a process id that is given to it
