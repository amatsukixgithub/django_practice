from django.db import models


class AnalysisLog(models.Model):
    image_path = models.CharField('画像ファイルパス', max_length=255, null=True, blank=True)
    success = models.CharField('成功', max_length=255, null=True, blank=True, default=None)
    message = models.CharField('レスポンスメッセージ', max_length=255, null=True, blank=True)
    field_class = models.IntegerField('クラス', db_column='class', null=True)
    confidence = models.DecimalField('信頼性', null=True, max_digits=5, decimal_places=4)
    request_timestamp = models.PositiveIntegerField('リクエスト時刻', null=True)
    response_timestamp = models.PositiveIntegerField('レスポンス時刻', null=True)

    class Meta:
        db_table = 'ai_analysis_log'
