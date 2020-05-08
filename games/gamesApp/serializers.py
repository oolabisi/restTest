from rest_framework import serializers
from gamesApp.models import Games

# (or)
# from . import Games


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Games
        fields = ('id', 'name', 'description', 'release_date', 'game_category', 'was_included_in_home')

    #  pk = serializers.IntegerField(read_only=True)
    #  name = serializers.CharField(max_length=100)
    #  description = serializers.CharField(max_length=200)
    #  release_date = serializers.DateTimeField()
    #  game_category = serializers.CharField(max_length=200)
    #  was_included_in_home = serializers.BooleanField(required=False)

    def create(self, validated_data):
        return Games.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.release_date = validated_data.get('release_date', instance.release_date)
        instance.game_category = validated_data.get('game_category', instance.game_category)
        instance.was_included_in_home = validated_data.get('was_included_in_home', instance.was_included_in_home)
        instance.save()
        return instance
