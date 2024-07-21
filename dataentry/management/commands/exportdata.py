import csv
from django.core.management.base import BaseCommand
import datetime
from django.apps import apps


class Command(BaseCommand):
    help = 'Export data from student model to a csv file'

    def add_arguments(self, parser):
        parser.add_argument('model_name', type=str, help='Model name')

    

    def handle(self, *args, **kwargs):
        model_name = kwargs['model_name'].capitalize()

        # search through all the installed apps for the model
        model = None
        for app_config in apps.get_app_configs():
            try:
                model = apps.get_model(app_config.label, model_name)
                break # stop executing once the model is found
            except LookupError:
                pass
        
        if not model:
            self.stderr.write(f'Model {model_name} cound not found')
            return

        data = model.objects.all()
        
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

        file_path = f'Exported_{model_name}_data_{timestamp}.csv'

        # open the csv file and write the data
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)

            # write the CSV header
            # we want to print the field names of the model that we are trying to export
            writer.writerow([field.name for field in model._meta.fields])

            for dt in data:
                writer.writerow([getattr(dt, field.name) for field in model._meta.fields])
        
        self.stdout.write(self.style.SUCCESS('Data exported successfully!'))