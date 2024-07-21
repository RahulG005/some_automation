import csv
from django.core.management.base import BaseCommand, CommandParser, CommandError
#from dataentry.models import Student
from django.apps import apps

#proposed command -- python manage.py importdata file_path

class Command(BaseCommand):
    help = "Import data from csv"

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help= "path to the csv file" )
        parser.add_argument('model_name', type=str, help='Name of the model')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        model_name = kwargs['model_name'].capitalize()

        #search for model across all apps
        model=None
        for app_config in apps.get_app_configs():

            try:
                model = apps.get_model(app_config.label, model_name)
                break
            except LookupError:
                continue
        
        if not model:
            raise CommandError(f'Model {model_name} not found in any app!')

        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                model.objects.create(**row)
        self.stdout.write(self.style.SUCCESS("Imported from csv successfully!"))