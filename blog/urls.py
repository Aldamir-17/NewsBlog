from django.urls import path
from .views import newspage, contactpage, news_list, news_detali, categoryPage,singlenewsPage

urlpatterns =[
    path('',newspage, name="news"),
    path("category", categoryPage, name="category_page"),
    path('news',news_list, name="newslist"),

    path('news/<slug:news>',news_detali, name="detali"),

    path('contact',contactpage, name="contact"),
    path('single/',singlenewsPage, name="single"),
]
