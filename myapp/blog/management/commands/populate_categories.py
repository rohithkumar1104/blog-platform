from typing import Any
from blog.models import Category
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "This command inserts category data"

    def handle(self, *args, **options):
        #Deleting existing
        Category.objects.all().delete()
        
        categories = ['sports', 'Tecnology', 'Science', 'Art', 'Food']

        for category_name in categories:
            Category.objects.create(name = category_name)
        self.stdout.write(self.style.SUCCESS("Completed inserting Data!"))