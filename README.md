It is a college management system built using Django framework. It is designed for interactions between students and teachers. Features include courses, grades, etc.

The project is hosted live at **http://lakshmankattunga.pythonanywhere.com/**

The procedure to run the project on local machine is as follows: 

Its recommended to use Mozilla Browser to view the project either through the hosted link given above or using local server.

## Installation

Python and Django need to be installed

```bash
pip install django
```

## Usage
- create a folder where you want to save this project in your computer.  
- open command prompt and change the directory to this folder using the
command prompt by ' cd ./(the path file of your folder) '. Make sure that
your folder is saved in the original directory of your command prompt.

  ```bash
   python manage.py runserver
   ```

-  Make sure that the above command is run with the folder where manage.py file is present as working directory.
 
- The url will be provided in your command prompt. Type the url into your web browser to access and open the project.

- Generally, the url provided is  **http://127.0.0.1:8000/**

## Login

The login page is common for students, faculty and admin.  

Example username and password for student:  
username - 'lakshman'  
password - 'lakshman123'  

Example username and password for faculty:  
username - 'adrijit'  
password - 'adrijit123'  

You can access the admin page at **http://127.0.0.1:8000/admin** or by clicking on **Login as Admin** on the homepage of the project 

The login credentials for the admin are provided in the report submitted.

Also a new admin user can be created using

```bash
python manage.py createsuperuser
```

## Users

New students and teachers can be added through the admin page. A new user needs to be created for each. 

The admin page is used to modify all tables such as Students, Faculty, Departments, Courses, enrollments etc.