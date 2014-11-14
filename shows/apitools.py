"""
Contains tools for dealing with various API's.
Uses HTTP and the 'Requests' third party package, since
google-api-python-client does not not support Python 3+.
Written in Python 3.4.
"""

from __future__ import unicode_literals

import requests
from django.conf import settings

GOOGLE_API_KEY = settings.GOOGLE_API_KEY

MIDROLL_API_KEY = settings.MIDROLL_API_KEY

ITUNES_BASE = 'https://itunes.apple.com/'

YOUTUBE_BASE = 'https://www.googleapis.com/youtube/v3'

FREEBASE_BASE = 'https://www.googleapis.com/freebase/v1/topic'


def itunes_search(q, media='podcast', limit=5, **kwargs):
    """
    Searches the iTunes API. For objects other than podcasts,
    set media="[object type]". Returns a request object.
    """

    params = {'term': q, 'media': media, 'limit': limit}
    params.update(kwargs)
    r = requests.get(ITUNES_BASE + 'search', params=params)
    return r


def itunes_lookup(itunes_id, **kwargs):
    """
    Gets an itunes object from the trackID. Returns a request object.
    """

    params = {'id': itunes_id}
    params.update(kwargs)
    r = requests.get(ITUNES_BASE + 'lookup', params=params)
    return r


def youtube_search(q, part='id,snippet', _type='channel', **kwargs):
    """
    Returns a YouTube API search as a request object. Default filters 'type'
    to Channels.
    """

    params = {'q': q, 'key': GOOGLE_API_KEY, 'part': part, 'type': _type}
    params.update(kwargs)
    r = requests.get(YOUTUBE_BASE + '/search', params=params)
    return r


def youtube_channel(channel_id, part='id,snippet', **kwargs):
    """
    Gets a YouTube channel  as a request object given a channel ID. To grab
    more info, add appropriate 'parts' (may increase quota usage).
    """

    params = {'id': channel_id, 'key': GOOGLE_API_KEY, 'part': part}
    params.update(kwargs)
    r = requests.get(YOUTUBE_BASE + '/channels', params=params)
    return r


def get_freebase(topic_id_list):
    """
    Returns Freebase tag names for a list of topic ID's.
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