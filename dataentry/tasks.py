from awd_main.celery import app
import time
from django.core.management import call_command
from django.contrib import messages
from django.conf import settings
from .utils import send_email_notification
from django.core.mail import send_mail


@app.task
def celery_test_task():
    time.sleep(10)
    return "Task executed successfully"

@app.task
def import_data_task(file_path, model_name):
    try:
        call_command('importdata', file_path, model_name)
    except Exception as e:
        raise e
    
     # notify the user by email
    mail_subject = 'Import Data Completed'
    message = 'Your data import has been successful'
   
    send_email_notification(mail_subject,message,settings.DEFAULT_TO_EMAIL,)
    print("email sent")
    return 'Data imported successfully.'
    
   
