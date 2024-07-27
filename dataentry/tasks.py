from awd_main.celery import app
import time
from django.core.management import call_command
from django.contrib import messages
from django.conf import settings
from .utils import send_email_notification, generate_csv_file
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
    
    return 'Data imported successfully.'

@app.task
def export_data_task(model_name):
    try:
        call_command('exportdata', model_name)
    except Exception as e:
        raise e
    
    file_path = generate_csv_file(model_name)
    
    # Send email with the attachment
    mail_subject = 'Export Data Successful'
    message = 'Export data successful. Please find the attachment'
    
    send_email_notification(mail_subject, message, settings.DEFAULT_TO_EMAIL, file_path)
    return 'Export Data task executed successfully.'
   
