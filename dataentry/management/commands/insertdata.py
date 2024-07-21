
from django.core.management.base import BaseCommand
from dataentry.models import Student

class Command(BaseCommand):
    help = "It will enter data to database"

    def handle(self, *args, **kwargs):

        dataset = [
            {'roll_no': 1002, 'name': 'Sachin', 'age':21},
            {'roll_no': 1006, 'name': 'Michel', 'age':22},
            {'roll_no': 1004, 'name': 'Mike', 'age':23},
            {'roll_no': 1005, 'name': 'Joseph', 'age':25},
        ]

        for data in dataset:
            roll_no = data['roll_no']
            existing_record = Student.objects.filter(roll_no = roll_no).exists()

            if not existing_record:
                Student.objects.create(roll_no=data['roll_no'],Name = data['name'], age = data['age'])
            else:
                self.stdout.write(self.style.ERROR(f'Student with {roll_no} already exists in database'))
        self.stdout.write(self.style.SUCCESS('Data entered successfully!'))

