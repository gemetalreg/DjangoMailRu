from django.conf.urls import url

from views import test, fail404

urlpatterns = [
    url(r'^$', test, name='test'),
    url(r'^login/', test),
    url(r'^signup/', test),
    url(r'^question/\d+/', test),
    url(r'^ask/', test),
    url(r'^popular/', test),
    url(r'^new/', test),
]
