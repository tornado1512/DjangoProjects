from django.urls import path
from  . import views
urlpatterns = [
    path('',views.ArticleListView.as_view(),name='home'),
    path('article/<int:pk>',views.ArticleDetailView.as_view(),name='article_page'),
    path('article/new/',views.ArticleCreateView.as_view(),name='new_article'),
    path('article/new/edit/<int:pk>',views.ArticleUpdateView.as_view(),name='article_edit'),
    path('article/new/delete/<int:pk>',views.ArticleDeleteView.as_view(),name='article_delete'),

]