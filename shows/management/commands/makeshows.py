from __future__ import unicode_literals

import csv
import os.path

from django.core.management.base import BaseCommand
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from shows.models import Show, Platform

# headers we expect from the csv file
SHOW_CSV_HEADERS = ['platform', 'show_name', 'api_id']


class Command(BaseCommand):
    help = ('Tries to create new shows from a CSV list. By default, '
            'looks for makeshows.csv in project_root/, but will take '
            'another file path as an argument. If no file is found, '
            'creates a sample template. Platform, along with either '
            'show_name or an api_id is required. If not given api_id, '
            "I hope you're feeling lucky.")

    def handle(self, *args, **options):
        if args:
            fn = args[0]
        else:
            fn = 'makeshows.csv'
        if os.path.isfile(fn):
            # If the file exists, make the shows
            with open(fn, newline='') as f:
                reader = csv.DictReader(f)
                for i, row in enumerate(reader):
                    make_show(self, row, i + 2)
        else:
            # If the file doesn't exist, make a template and do nothing
            with open('makeshows_template.csv', 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(SHOW_CSV_HEADERS)
                msg = 'No file found. See template created at {}'.format(fn)
                self.stdout.write(msg)


def make_show(command, csv_dict_row, row_num):
    """
    Creates a new Show object from a dict of show info. Attempts to get
    additional info from an API, if possible.
    :param csv_dict_row: a single row from a DictReader instance.
    """

    platform_name = csv_dict_row['platform']
    api_id = csv_dict_row['api_id']

    # Make sure the show doesn't already exists to avoid duplicates.
    # Hit the database for each show *on purpose*, to ensure we haven't made
    # a duplicate since the command began
    api_id_exists = Show.objects.filter(api_id=api_id)
    if api_id_exists:
        command.stdout.write(
            'Row #{}: Show already exists for {}'.format(row_num, api_id)
        )
        return
    show_data = {}

    # Grab API data if able
    try:
        platform = Platform.objects.get(
            Q(name__icontains=platform_name) |
            Q(simple_name__icontains=platform_name)
        )
    except ObjectDoesNotExist:
        command.stdout.write('Row #{}: Platform not found!'.format(row_num))
        return
    api = platform.get_api_class()(show_api_id=api_id)
    show_data.update(api.get_show_initial())

    # Make the show
    if show_data:
        # Couldn't get this to work with 'tags' in the dict, so pop them
        # and add them after the save.
        tags = show_data.pop('tags').split(', ')
        s = Show(**show_data)
        s.save()
        s.tags.add(*tags)
        command.stdout.write('Show created: {}'.format(s))
    else:
        command.stdout.write('Row #{}: No show found for {}'.format(row_num, api_id))
