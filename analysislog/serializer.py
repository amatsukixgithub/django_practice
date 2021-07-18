# coding: utf-8
import random
import time

from rest_framework import serializers
from .models import AnalysisLog


class AnalysisLogSerializer(serializers.ModelSerializer):

    class Meta:
        model = AnalysisLog
        fields = '__all__'

    def create(self, request):
        image_path = request['image_path']

        # イメージパスが指定されていない場合
        if not image_path:
            return AnalysisLog(
                success=False,
                message='Error:E50012'
            )

        analysis_log = AnalysisLog(
            image_path=image_path,
            success=True,
            message='success',
            field_class=random.randrange(1, 9),
            confidence=random.random(),
            request_timestamp=time.time(),
            response_timestamp=time.time()
        )
        analysis_log.save()
        return analysis_log
