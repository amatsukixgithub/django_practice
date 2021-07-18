# coding: utf-8

from rest_framework import routers
from .views import AnalysisLogViewSet


router = routers.DefaultRouter()
router.register('', AnalysisLogViewSet)
