from __future__ import unicode_literals

import csv
import re
import os.path

from django.core.management.base import BaseCommand
from shows.models import Show

SHOW_CSV_HEADERS = ['platform', 'showname', 'api_id']


class Command(BaseCommand):
    help = ('Tries to create new shows from a CSV list. By default, '
            'looks for makeshows.csv in projectroot/, but will take '
            'another file path as an argument. If no file is found, '
            'creates a sample template.')

    def make_show(self, csv_dict_row):
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
        if os.path.isfile(fn):
            # If the file exists, make the shows
            with open(fn, newline='') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    self.make_show(row)
        else:
            # If the file doesn't exist, make a template and do nothing
            with open(fn, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(SHOW_CSV_HEADERS)
                msg = 'No file found. See template created at {}'.format(fn)
                self.stdout.write(msg)
