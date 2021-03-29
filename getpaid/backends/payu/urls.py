from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from getpaid.backends.payu.views import OnlineView, SuccessView, FailureView

urlpatterns = [
    path(r'^online/$', csrf_exempt(OnlineView.as_view()), name='getpaid-payu-online'),
    path(r'^success/(?P<pk>\d+)/', csrf_exempt(SuccessView.as_view()), name='getpaid-payu-success'),
    path(r'^failure/(?P<pk>\d+)/(?P<error>\d+)/', csrf_exempt(FailureView.as_view()), name='getpaid-payu-failure'),
]
