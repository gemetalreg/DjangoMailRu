from django.conf.urls import url

from views import test, fail404, one_question, new_questions, popular

urlpatterns = [
    url(r'^$', new_questions),
    url(r'^login/', test),
    url(r'^signup/', test),
    url(r'^question/(?P<qid>\d+)/', one_question),
    url(r'^ask/', test),
    url(r'^popular/', popular),
    url(r'^new/', test),
    url(r"^", fail404)
]
