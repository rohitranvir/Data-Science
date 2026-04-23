from rest_framework import serializers
from .models import Subscription
class SubscripitonSerializer(serializers.ModelSerializer):
    class Meta:
        model=Subscription
        fields=['id','status','amount','start_date','end_date']