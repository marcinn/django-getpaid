from django.urls import path, include
from getpaid.views import NewPaymentView, FallbackView
from getpaid.utils import import_backend_modules

includes_list = []
for backend_name, urls in list(import_backend_modules('urls').items()):
    includes_list.append(path(r'^%s/' % backend_name, include(urls)))

urlpatterns = [
    path(r'^new/payment/(?P<currency>[A-Z]{3})/$', NewPaymentView.as_view(), name='getpaid-new-payment'),
    path(r'^payment/success/(?P<pk>\d+)/$', FallbackView.as_view(success=True), name='getpaid-success-fallback'),
    path(r'^payment/failure/(?P<pk>\d+)$', FallbackView.as_view(success=False), name='getpaid-failure-fallback'),
]

urlpatterns += includes_list
