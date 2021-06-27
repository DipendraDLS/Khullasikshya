## To run this project
```python
1. Create Mysql database with name "khullasikshya"
2. create config.json file and give the following:
    Note: you need to change USER, PASS, NAME, HOST_USER, HOST_PASSWORD according to your's settings.
    {
      "DEFAULT":
      {
        "DATABASE_USER": "db_username",
        "DATABASE_PASS": "db_password",
        "DATABASE_NAME": "khullasikshya",
        "EMAIL_HOST_USER": "your_valid_gmail",
        "EMAIL_HOST_PASSWORD": "your_gmail_password",
        "EMAIL_HOST": "smtp.gmail.com",
        "EMAIL_PORT": "587"
      }
    }


3. python manage.py -r requirements.txt in your virtual env.
4. python manage.py setup => this will do all migrations and even loads the data also don't need to create super user.


*************** NOTE : Not needed step no. 5 as i have maintained fixtures and setup.py *************
5. you need to configure the site_id as well for facebook, gmail login for that follow these steps:
    i) create superuser using command as: python manage.py createsuperuser
    ii) goto localhost:8000/admin/
    ii) goto Sites tab
    iii) Add sites as:
            Domain name: localhost:8000
            Display name: localhost
    iv)  goto social application in admin panel
    v)   add there  facebook and gmail application with client id, secrete key and in Sites you need to choose localhost:8000
    NOTE: if you don't know how to create your own gmail facebook social app and get client id and secrete key follow this link:
                          Youtube Link: https://www.youtube.com/watch?v=-TUEM2NCuVE&t=633s&ab_channel=CODEV
```
