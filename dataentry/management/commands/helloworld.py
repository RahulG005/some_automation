from typing import Any
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Print hello Rahul"

    def handle(self, *args, **kwargs):
        self.stdout.write('Hello Rahul')