from rest_framework.serializers import ModelSerializer
from base.views import Room


class Roomserializers(ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'