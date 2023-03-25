from django.urls import path

from todoapp.views import TodoCreateView, TodoDeleteView, TodoListView, TodoUpdateView, set_done, unset_done


urlpatterns = [
    path('', TodoListView.as_view(), name='list'),
    path('todo/<int:pk>', TodoUpdateView.as_view(), name='update'),
    path('add', TodoCreateView.as_view(), name='create'),
    path('delete/<int:pk>', TodoDeleteView.as_view(), name='delete'),
    path('set-done/<int:pk>', set_done, name='set-done'),
    path('unset-done/<int:pk>', unset_done, name='unset-done'),
]
