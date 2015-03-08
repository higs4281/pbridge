from __future__ import absolute_import, unicode_literals

from time import mktime
from datetime import datetime
from django.core.files.base import ContentFile
import feedparser
import requests


def get_art_file(art_url):
    r = requests.get(art_url)
    r.raise_for_status()
    file = ContentFile(r.content)
    return file


class RSSFeed:
    """
    Base class for dealing with podcast RSS feeds, which have more
    info than the iTunes API can provide.
    """

    def __init__(self, rss_feed_url):
        self.parse = feedparser.parse(rss_feed_url)

    def get_feed(self):
        return self.parse.feed

    def get_entries(self):
        return self.parse.entries

    def get_entries_with_initial(self):
        entries = self.get_entries()
        for entry in entries:
            entry['initial'] = self.get_itunes_initial(entry)
        return entries

    @staticmethod
    def get_itunes_initial(entry):
        # Date has to be restructured to a datetime object
        rss_struct_time = entry.published_parsed
        date = datetime.fromtimestamp(mktime(rss_struct_time))
        initial_data = {
            'date': date,
            'link': entry.link,
            'details': entry.description,
        }
        return initial_data