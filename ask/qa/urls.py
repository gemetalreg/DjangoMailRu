from django.conf.urls import url

from . import views
from views import test, fail404, one_question, new_questions, popular

urlpatterns = [
    url(r'^$', views.new_questions),
    url(r'^login/', views.test),
    url(r'^signup/', views.test),
    url(r'^question/(?P<qid>\d+)/', views.one_question, name='question'),
    url(r'^ask/', views.ask),
    url(r'^answer/', views.answer),
    url(r'^popular/', views.popular),
    url(r'^new/', views.test),
    url(r"^", views.fail404)
]
