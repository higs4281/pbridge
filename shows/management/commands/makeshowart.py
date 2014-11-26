from __future__ import unicode_literals

from django.core.management.base import NoArgsCommand
from shows.models import Show
from shows.utils import get_art_file


class Command(NoArgsCommand):
    help = ('For each show in the database with an external splash art URL '
            'defined, but no file saved for it yet, tries to download and '
            'save the art file from the URL.')

    def handle_noargs(self, **options):
        shows = Show.objects.get(art_file='')
        for show in shows:
            url = show.art_external
            if url:
                ext = url.split('.')[-1]
                fn = 'show-' + str(show.id) + '-splash-art.' + ext
                file = get_art_file(url)
                show.art_file.save(fn, file)
                msg = 'Show art saved: {}'.format(show.name)
                self.stdout.write(msg)