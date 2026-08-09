from django.urls import path,re_path #repath means ragex
from . import views
urlpatterns = [
    path('post/<int:post_id>/',views.post_detail,name='Post Details'), 
    path('user/<str:username>/',views.user_profile,name='user_profile'),
    path('article/<int:year>/<int:month>/<int:day>/',views.article_details ,name='artical_by_year_month'),
    re_path(r'^article/(?P<year>[0-9]{4})/$',views.article_by_year,name='article_by_year'),
    re_path(r'^article2/(?P<year>[0-9]{4})/$',views.article_by_second_year,name="dummy year"),
]

