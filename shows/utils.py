from __future__ import absolute_import, unicode_literals

from time import mktime
from datetime import datetime
from django.core.files.base import ContentFile
import requests

from django.shortcuts import get_object_or_404

from .models import Platform
from .apitools import youtube_channel, get_freebase, itunes_lookup


def get_art_file(art_url):
    r = requests.get(art_url)
    r.raise_for_status()
    file = ContentFile(r.content)
    return file


def get_art_url(api_id, platform_name):
    """
    Grabs a URL for show art from an api id.
    """
    if platform_name.lower() in ('yt', 'youtube'):
        data = youtube_channel(api_id).json()
        item_list = data.get('items', [{}])
        if not item_list:
            return None

        items = item_list[0]
        snippet = items.get('snippet', {})
        thumbs = snippet.get('thumbnails', {})
        return thumbs.get('high').get('url') or thumbs.get('default').get('url')

    if platform_name.lower() in ('it', 'itunes'):
        data = itunes_lookup(api_id).json()
        items = data.get('results', [])[0]
        if not items:
            return None

        return items.get('artworkUrl600')


def yt_init_data(channel_id):
    """
    Returns a dictionary with pre-filled field values for a Show given
    YouTube API ID. Can be passed to a Django form as initial data.
    YouTube API call should be done with part='id,snippet,topicDetails'.
    Requires Platforms model to be populated with a 'youtube' object.
    """

    data = youtube_channel(channel_id, part='id,snippet,topicDetails').json()

    item_list = data.get('items', [{}])
    if not item_list:
        return None

    items = item_list[0]
    snippet = items.get('snippet', {})
    thumbs = snippet.get('thumbnails', {})
    api_id = items.get('id')
    topic_id_list = items.get('topicDetails', {}).get('topicIds')
    freebase_tag_list = get_freebase(topic_id_list)
    platform = get_object_or_404(Platform, simple_name__iexact='youtube')
    link = platform.show_base_url.format(api_id)
    art_external = thumbs.get('high').get('url') or thumbs.get('default').get('url')

    # Show Fields (initial data)
    initial_data_dict = {
        'name': snippet.get('title'),
        'api_id': api_id,
        'description': snippet.get('description'),
        'link': link,
        'art_external': art_external,
        'platform': platform,
        'feed': 'https://gdata.youtube.com/feeds/api/users/' + api_id,
        'tags': ', '.join(freebase_tag_list),
    }
    return initial_data_dict


def it_init_data(itunes_id):
    """
    Returns a dictionary with pre-filled field values for a Show given
    iTunes API ID. Can be passed to a Django form as initial data.
    Requires the Platforms model to be populated with an 'itunes' object.
    """

    # Get the iTunes JSON data from the iTunes API
    data = itunes_lookup(itunes_id).json() or {}

    items = data.get('results', [])[0]
    if not items:
        return None

    tag_list = items.get('genres', [])
    api_id = items.get('trackId')
    platform = get_object_or_404(Platform, simple_name__iexact='itunes')
    link = platform.show_base_url.format(api_id)
    art_external = items.get('artworkUrl600')

    # Show Fields (initial data)
    initial_data_dict = {
        'name': items.get('trackName'),
        'api_id': api_id,
        'platform': platform,
        'link': link,
        'art_external': art_external,
        'feed': items.get('feedUrl'),
        'tags': ', '.join(tag_list),
    }
    return initial_data_dict


def it_episode_data(rssEntry):
    # Date has to be restructured to a datetime object
    rss_struct_time = rssEntry.published_parsed
    date = datetime.fromtimestamp(mktime(rss_struct_time))
    initial_data_dict = {
        'date': date,
        'link': rssEntry.link,
        'details': rssEntry.description,
    }
    return initial_data_dict