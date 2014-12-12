from __future__ import absolute_import

from rest_framework import serializers

from . import models


class ShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Show
        fields = [
            'name',
            'host',
            'api_id',
            'platform',
            'art_external',
            'description',
            'link',
            'feed',
            'episodes_per_month',
            'downloads_per_episode',
            'default_vendor',
            'active',
            'notes',
        ]