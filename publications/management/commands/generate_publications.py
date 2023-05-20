from django.core.management.base import BaseCommand
from faker import Faker

from publications.models import Publication


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("publications_count", nargs="?", type=int, default=10)

    def handle(self, *args, publications_count, **options):
        faker = Faker()
        publications = [
            Publication(
                title=faker.sentence().replace(".", ""),
                content=faker.text(1000),
            )
            for _ in range(publications_count)
        ]

        Publication.objects.bulk_create(publications)

        self.stdout.write(
            self.style.SUCCESS("Successfully created %s publications" % publications_count)
        )
