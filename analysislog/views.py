# coding: utf-8

from rest_framework import status, mixins
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .models import AnalysisLog
from .serializer import AnalysisLogSerializer


# PUT以外のメソッドを実装
class AnalysisLogViewSet(mixins.CreateModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.DestroyModelMixin,
                         mixins.ListModelMixin,
                         GenericViewSet):

    queryset = AnalysisLog.objects.all()
    serializer_class = AnalysisLogSerializer

    # POSTの場合は特別なレスポンスを返す
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        # 成功している場合は201で返す
        response_status = status.HTTP_201_CREATED if serializer.data['success'] == 'True' \
            else status.HTTP_400_BAD_REQUEST

        return Response({'success': serializer.data['success'],
                         'message': serializer.data['message'],
                         'estimated_data':
                             self.return_estimated_data(serializer.data['field_class'],
                                                        serializer.data['confidence'])
                         }, status=response_status, headers=headers)

    def return_estimated_data(self, field_class, confidence):
        if not field_class or not confidence:
            return {}

        return {'class': field_class, 'confidence': confidence}
