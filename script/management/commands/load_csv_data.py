from django.core.management.base import BaseCommand
from script.models import Product
import csv

class Command(BaseCommand):
    help = 'Load data from a CSV file into the database'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    def handle(self, *args, **kwargs):
        csv_file_path = kwargs['csv_file']
        self.load_data_from_csv(csv_file_path)

    def load_data_from_csv(self, csv_file_path):
        with open(csv_file_path, newline='', encoding='latin-1') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                Product.objects.create(
                    name=row['Titre du produit'],
                    description=row['Description du produit'],
                    #category=1,  # Replace with actual category_id or logic to fetch category_id
                    url=row.get('URL du produit', None)
                    # Add other fields as needed
                )
        self.stdout.write(self.style.SUCCESS('Data inserted successfully.'))
