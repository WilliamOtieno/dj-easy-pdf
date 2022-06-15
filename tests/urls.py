# coding=utf-8

from django.conf.urls import url

from easy_pdf.views import PDFTemplateView
from .views import DemoPDFView, PDFUserDetailView

urlpatterns = [
    url(r'^demo/$', DemoPDFView.as_view()),
    url(r'^simple/$', PDFTemplateView.as_view(template_name='simple.html')),
    url(r'^user/(?P<pk>\d+)/$', PDFUserDetailView.as_view()),
]
