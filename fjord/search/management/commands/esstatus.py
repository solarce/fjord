import logging

from django.core.management.base import BaseCommand

from fjord.search.utils import es_status_cmd


class Command(BaseCommand):
    help = 'Shows elastic search index status.'

    def handle(self, *args, **options):
        logging.basicConfig(level=logging.INFO)
        es_status_cmd()
