"""
Contains tools for dealing with various API's.
Uses HTTP and the 'Requests' third party package, since
google-api-python-client does not not support Python 3+.
Written in Python 3.4.
"""

from __future__ import unicode_literals
import dateutil.parser
from django.core.exceptions import ImproperlyConfigured

import requests
from django.conf import settings
from shows.utils import RSSFeed

GOOGLE_API_KEY = settings.GOOGLE_API_KEY

MIDROLL_API_KEY = settings.MIDROLL_API_KEY

ITUNES_BASE = 'https://itunes.apple.com/'

YOUTUBE_BASE = 'https://www.googleapis.com/youtube/v3'

FREEBASE_BASE = 'https://www.googleapis.com/freebase/v1/topic'


def get_freebase(topic_id_list):
    """
    Returns Freebase tag names given a list of topic ID's.
    """

    if not topic_id_list:
        return []
    tags = []
    params = {
        'key': GOOGLE_API_KEY,
        'filter': '/type/object/name'
    }
    for topic_id in topic_id_list:
        r = requests.get(FREEBASE_BASE + topic_id, params=params)
        topic = r.json()
        name = topic.get(
            'property', {}
        ).get(
            '/type/object/name', {}
        ).get(
            'values', [{}]
        )[0].get(
            'text', ''
        )
        if name:
            tags.append(name)
    return tags


class BasePlatformAPI(object):
    """
    Base class for platform-specific API classes.
    Endpoint must be set.
    """
    show_api_id = None
    episode_api_id = None
    show_object = None
    episode_object = None
    endpoint = None

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def get_show_api_id(self):
        if self.show_api_id is None:
            raise ImproperlyConfigured(
                "{} is missing a show_api_id."
                " Set show_api_id first.".format(self.__class__.__name__)
            )
        return self.show_api_id

    def search(self, q):
        return NotImplemented

    def get_show_initial(self):
        return NotImplemented

    def get_episode_initial(self):
        return NotImplemented

    def get_show_object(self, **kwargs):
        return NotImplemented

    def get_episode_object(self):
        return NotImplemented

    def get_art_url(self):
        return NotImplemented

    def get_episode_list(self):
        return NotImplemented


class YouTubeAPI(BasePlatformAPI):
    """
    A class for the YouTube API
    """
    endpoint = 'https://www.googleapis.com/youtube/v3'
    api_key = settings.GOOGLE_API_KEY

    def search(self, q, **kwargs):
        """
        Returns a YouTube API search as a request object. Default filters 'type'
        to Channels.
        See params variable for default search parameters.
        """
        params = {'q': q, 'key': GOOGLE_API_KEY, 'part': 'id,snippet'}
        params.update(kwargs)
        r = requests.get(YOUTUBE_BASE + '/search', params=params)
        return r.json()

    def get_show_object(self, **kwargs):
        """
        Gets a YouTube channel  as json, given a channel ID. To grab
        more info, add appropriate 'parts' (may increase quota usage).
        """
        if not self.show_object:
            params = {
                'id': self.get_show_api_id(),
                'key': GOOGLE_API_KEY,
                'part': 'id,snippet'
            }
            params.update(kwargs)
            r = requests.get(YOUTUBE_BASE + '/channels', params=params)
            self.show_object = r.json()
        return self.show_object

    def get_art_url(self):
        data = self.get_show_object()
        item_list = data.get('items', [{}])
        if item_list:
            items = item_list[0]
            thumbs = items.get('snippet', {}).get('thumbnails', {})
            return thumbs.get('high').get('url') or thumbs.get('default').get('url')
        return None

    def get_episode_list(self):
        data = self.search(None, channelId=self.get_show_api_id())
        episode_list = data.get('items', [])
        # special handling for structured date
        for episode in episode_list:
            published_at = episode.get('snippet', {}).get('publishedAt')
            date = dateutil.parser.parse(published_at)
            episode['date'] = date
        return episode_list

    def get_show_initial(self):
        """
        Returns a dictionary with pre-filled field values for a Show given
        YouTube API ID. Can be passed to a Django form as initial data.
        Platform itself will need to be added to the initial data separately
        (can't import here).
        """
        data = self.get_show_object()
        item_list = data.get('items', [{}])
        if item_list:
            items = item_list[0]
            snippet = items.get('snippet', {})
            thumbs = snippet.get('thumbnails', {})
            api_id = items.get('id')
            topic_id_list = items.get('topicDetails', {}).get('topicIds')
            freebase_tag_list = get_freebase(topic_id_list)
            link = 'https://www.youtube.com/channel/{}/'.format(api_id)
            art_external = thumbs.get('high').get('url') or thumbs.get('default').get('url')
            initial_data_dict = {
                'name': snippet.get('title'),
                'api_id': api_id,
                'description': snippet.get('description'),
                'link': link,
                'art_external': art_external,
                'platform_id': 1,
                'feed': 'https://gdata.youtube.com/feeds/api/users/' + api_id,
                'tags': ', '.join(freebase_tag_list),
            }
            return initial_data_dict
        return {}


class ItunesAPI(BasePlatformAPI):
    """
    A class for the iTunes API
    """
    endpoint = 'https://itunes.apple.com/'
    rss_feed_url = None

    def search(self, q, **kwargs):
        """
        Searches the iTunes API. For objects other than podcasts,
        set media="[object type]". Returns a request object.
        See params variable for default search parameters.
        """
        params = {'term': q, 'media': 'podcast', 'limit': 5}
        params.update(kwargs)
        r = requests.get(ITUNES_BASE + 'search', params=params)
        return r.json()

    def get_show_object(self, **kwargs):
        if not self.show_object:
            params = {'id': self.get_show_api_id()}
            params.update(kwargs)
            r = requests.get(ITUNES_BASE + 'lookup', params=params)
            self.show_object = r.json()
        return self.show_object

    def get_art_url(self):
        data = self.get_show_object()
        items = data.get('results', [])[0]
        if items:
            return items.get('artworkUrl600')
        return None

    def get_episode_list(self):
        rss = RSSFeed(self.rss_feed_url)
        entries = rss.get_entries_with_initial()
        try:
            return entries[:5]
        except KeyError:
            return entries

    def get_show_initial(self, **kwargs):
        """
        Returns a dictionary with pre-filled field values for a Show given
        iTunes API ID. Can be passed to a Django form as initial data.
        Requires the Platforms model to be populated with an 'itunes' object.
        """
        # Get the iTunes JSON data from the iTunes API
        data = self.get_show_object()
        items = data.get('results', [])[0]
        if items:
            tag_list = items.get('genres', [])
            api_id = items.get('trackId')
            link = 'https://itunes.apple.com/us/podcast?id={}'.format(api_id)
            art_external = items.get('artworkUrl600')

            # Show Fields (initial data)
            initial_data_dict = {
                'name': items.get('trackName'),
                'api_id': api_id,
                'platform_id': 2,
                'link': link,
                'art_external': art_external,
                'feed': items.get('feedUrl'),
                'tags': ', '.join(tag_list),
            }
            return initial_data_dict
        return {}