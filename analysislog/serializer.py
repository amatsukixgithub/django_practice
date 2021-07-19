# coding: utf-8
import random
import time

from rest_framework import serializers
from .models import AnalysisLog


def analyze_with_ai():
    # AI分析する想定
    time.sleep(1)
    return {'class': random.randrange(1, 9), 'confidence': random.random()}


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

        # APIに接続
        request_time = time.time()
        result = analyze_with_ai()
        response_time = time.time()

        analysis_log = AnalysisLog(
            image_path=image_path,
            success=True,
            message='success',
            field_class=result['class'],
            confidence=result['confidence'],
            request_timestamp=request_time,
            response_timestamp=response_time
        )
        analysis_log.save()
        return analysis_log
