It is a college management system built using Django framework. It is designed for interactions between students and teachers. Features include courses, grades, etc.

The website is hosted live at **lakshmankattunga.pythonanywhere.com/**

The procedure to run the project on local machine is as follows: 

## Installation

Python and Django need to be installed

```bash
pip install django
```

## Usage

Go to the erp folder and activate the virtual environment by pressing ctrl+Shift+~

```bash
python manage.py runserver
```

 Make sure that the above command is run in the folder where manage.py file is present 
 
The url will be provided in your command prompt. Type the url into your web browser to access and open the project.

Generally, the url provided is  **http://127.0.0.1:8000/**

## Login

The login page is common for students, faculty and admin.  

Example username and password for student:  
username - 'lakshman'  
password - 'lakshman123'  

Example username and password for faculty:  
username - 'adrijit'  
password - 'adrijit123'  

The login credentials for the admin of are provided in the report submitted.

You can access the admin page at **http://127.0.0.1:8000/admin** or by clicking on **Login as Admin** on the homepage of the project 

Also a new admin user can be created using

```bash
python manage.py createsuperuser
```

## Users

New students and teachers can be added through the admin page. A new user needs to be created for each. 

The admin page is used to modify all tables such as Students, Faculty, Departments, Courses, enrollments etc.