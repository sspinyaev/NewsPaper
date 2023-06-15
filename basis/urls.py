from django.urls import path
# Импортируем созданное нами представление
from .views import PostList, PostDetail, PostSearch, NewsCreate, NewsEdit, NewsDelete, ArticleDelete,ArticleEdit,ArticleCreate, CategoryListView, subscriptions


urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>', PostDetail.as_view()),
    path('search', PostSearch.as_view()),
    path('create/', NewsCreate.as_view(), name = 'post_create'),
    path('<int:pk>/update/', NewsEdit.as_view(), name='post_update'),
    path('<int:pk>/delete/', NewsDelete.as_view(), name='post_delete'),
    path('create/', ArticleCreate.as_view(), name = 'post_create'),
    path('<int:pk>/update/', ArticleCreate.as_view(), name='post_update'),
    path('<int:pk>/delete/', ArticleDelete.as_view(), name='article_delete'),
    path('categories/<int:pk>', CategoryListView.as_view(), name = 'category_list'),
    path('subscriptions/', subscriptions, name='subscriptions'),

]