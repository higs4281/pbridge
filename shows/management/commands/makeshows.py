from __future__ import unicode_literals

import csv
import re

from django.core.management.base import BaseCommand
from shows.models import Show


class Command(BaseCommand):
    help = ('Makes new shows from a CSV list. '
            'Default looks for makeshows.csv in projectroot/.')

    def make_show(self, csvrow):
        """
        Creates a new Show object from a dict of show info.
        """
        pass

    def add_arguments(self, parser):
        """
        Gathers the optional filename arg from the command line.
        """

        parser.add_argument('filename', default='makeshows.csv')

    def handle(self, *args, **options):
        fn = options['filename']
        with open(fn, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                self.make_show(row)
