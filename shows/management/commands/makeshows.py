from __future__ import unicode_literals

import csv
import re
import os.path

from django.core.management.base import BaseCommand
from shows.models import Show
from shows.utils import it_init_data, yt_init_data

SHOW_CSV_HEADERS = ['platform', 'show_name', 'api_id']


class Command(BaseCommand):
    help = ('Tries to create new shows from a CSV list. By default, '
            'looks for makeshows.csv in project_root/, but will take '
            'another file path as an argument. If no file is found, '
            'creates a sample template. Platform, along with either '
            'show_name or an api_id is required. If not given api_id, '
            "I hope you're feeling lucky.")

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
                    make_show(row)
        else:
            # If the file doesn't exist, make a template and do nothing
            with open(fn, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(SHOW_CSV_HEADERS)
                msg = 'No file found. See template created at {}'.format(fn)
                self.stdout.write(msg)


def make_show(csv_dict_row):
    """
    Creates a new Show object from a dict of show info. Attempts to get
    additional info from an API, if possible.
    :param csv_dict_row: a single row from a DictReader instance.
    """

    platform = csv_dict_row['platform']
    api_id = csv_dict_row['api_id']
    show_data = {}

    # Grab API data if able
    if platform.lower() in ('it', 'itunes'):
        if api_id:
            api_data = it_init_data(api_id)
            show_data.update(api_data)
    if platform.lower() in ('yt', 'youtube'):
        if api_id:
            api_data = yt_init_data(api_id)
            show_data.update(api_data)

    s = Show(show_data)
    s.save()
