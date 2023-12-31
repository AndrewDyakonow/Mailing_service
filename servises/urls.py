from django.urls import path
from django.views.decorators.cache import cache_page

from servises.views import start_page, main_page, ClientsListView, ClientsDetailView, ClientsCreateView, \
    ClientsUpdateView, ClientsDeleteView, SettingsListView, SettingsCreateView, SettingsDetailView, SettingsUpdateView, \
    SettingsDeleteView, MessageListView, MessageCreateView, MessageDetailView, MessageUpdateView, MessageDeleteView, \
    start_mailing, LogListView, end_mailing, testes

app_name = 'servises'

urlpatterns = [
    path('', start_page, name='start_page'),
    path('start/', cache_page(60)(main_page), name='main_page'),
    path('clients/', ClientsListView.as_view(), name='clients'),
    path('clients/<int:pk>/', ClientsDetailView.as_view(), name='client'),
    path('clients/new/', ClientsCreateView.as_view(), name='client_create'),
    path('clients/update/<int:pk>/', ClientsUpdateView.as_view(), name='client_update'),
    path('clients/delete/<int:pk>/', ClientsDeleteView.as_view(), name='client_delete'),

    path('settings/', SettingsListView.as_view(), name='setting_list'),
    path('settings/new/', SettingsCreateView.as_view(), name='setting_create'),
    path('settings/<int:pk>/', SettingsDetailView.as_view(), name='setting_detail'),
    path('settings/update/<int:pk>/', SettingsUpdateView.as_view(), name='setting_update'),
    path('settings/delete/<int:pk>/', SettingsDeleteView.as_view(), name='setting_delete'),

    path('message/', MessageListView.as_view(), name='message_list'),
    path('message/new/', MessageCreateView.as_view(), name='message_create'),
    path('message/<int:pk>/', MessageDetailView.as_view(), name='message_detail'),
    path('message/update/<int:pk>/', MessageUpdateView.as_view(), name='message_update'),
    path('message/delete/<int:pk>/', MessageDeleteView.as_view(), name='message_delete'),

    path('settings/startmailing/<int:pk>/', start_mailing, name='start_mailing'),
    path('settings/endmailing/<int:pk>/', end_mailing, name='end_mailing'),
    path('settings/logs/', LogListView.as_view(), name='log'),

    path('test/', testes, name='test')
]
