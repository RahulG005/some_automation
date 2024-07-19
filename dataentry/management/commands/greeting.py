from django.core.management.base import BaseCommand, CommandParser

class Command(BaseCommand):
    help = "Print hello Rahul"

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help = "Specifies user name")

    def handle(self, *args, **kwargs):
        name = kwargs['name']
        greeting = f"Hi {name}, Good morning"
        self.stdout.write(self.style.NOTICE(greeting))