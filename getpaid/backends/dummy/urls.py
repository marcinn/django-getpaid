from django.urls import path
from getpaid.backends.dummy.views import DummyAuthorizationView

urlpatterns = [
    path(r'^payment/authorization/(?P<pk>[0-7]+)/$', DummyAuthorizationView.as_view(), name='getpaid-dummy-authorization'),
]
