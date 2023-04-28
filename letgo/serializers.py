# 시리얼 이친구는 딕셔너리 형태를 만들어줘 이런 형태라고 한다. 좀 더 알아보기

#클래스 틀 객체 구현할 대상 인스턴스 구현된 구체적인 실체


from rest_framework import serializers
from letgo.models import Letgo

class LetgoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Letgo
        fields = "__all__"



