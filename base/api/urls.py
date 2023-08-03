from django.urls import path
from .views import auth, todo, today_tasks, messages, user
from .views.google import google_todos

urlpatterns = [
    # TODO: ____ todos _____
    path('todos', todo.todo_list_create, name='todo_list_create'),
    path('todos/<str:pk>', todo.todo_delete, name='todo_delete'),
    
    # TODO: ____ today notes _____
    path('today-notes', today_tasks.today_notes_list_create, name='today_notes_list_create'),
    path('today-notes/<str:pk>', today_tasks.today_notes_delete, name='today_notes_delete'),

    # TODO: ____ messages _____
    path('messages', messages.messages_list, name='messages_list'),  
    path('update-settings', user.update_settings, name='update_settings'),
    
    path('delete-todo/<str:todo_list>/<str:todo_id>', google_todos.GoogleTodoServiceDelete, name='delete_google_todo'),
    path('сomplete-todo/<str:todo_list>/<str:todo_id>', google_todos.GoogleTodoServiceComplete, name='complete_google_todo'),
    path('patch-title-todo/<str:todo_list>/<str:todo_id>', google_todos.GoogleTodoServicePatchTitle, name='patch_title_google_todo'),
    
    path('rewrite-tokens', user.rewrite_tokens, name='rewrite_tokens'), 
]