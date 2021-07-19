# coding: utf-8
import random
import time

from rest_framework import serializers
from .models import AnalysisLog


def analyze_with_ai(image_path):
    # AI分析する想定

    # イメージパスが指定されていない場合
    if not image_path:
        return AnalysisLog(
            success=False,
            message='Error:E50012'
        )

    request_time = time.time()
    time.sleep(1)

    analysis_log = AnalysisLog(
        image_path=image_path,
        success=True,
        message='success',
        field_class=random.randrange(1, 9),
        confidence=random.random(),
        request_timestamp=request_time,
        response_timestamp=time.time()
    )

    return analysis_log


class AnalysisLogSerializer(serializers.ModelSerializer):

    class Meta:
        model = AnalysisLog
        fields = '__all__'

    def create(self, request):
        image_path = request['image_path']

        # APIに接続
        analysis_log = analyze_with_ai(image_path)

        # 成功している場合
        if analysis_log.success:
            analysis_log.save()

        return analysis_log
