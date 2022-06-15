# coding=utf-8

from django.urls import path

from easy_pdf.views import PDFTemplateView
from .views import DemoPDFView, PDFUserDetailView

urlpatterns = [
    path('demo/', DemoPDFView.as_view()),
    path('simple/', PDFTemplateView.as_view(template_name='simple.html')),
    path('user/<pk>/', PDFUserDetailView.as_view()),
]
