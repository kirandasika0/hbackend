from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^create_event/', views.createEvent),
    url(r'event_feed/', views.event_feed),
    url(r'chat_notification/', views.chat_notification),
    url(r'is_attendee/', views.is_attendee),
    url(r'attend/', views.attend),
    url(r'cancel_attendee/', views.cancel_attendee),
    url(r'edit_chat_notifications/', views.edit_chat_notifications),
    url(r'new_checklist_item/', views.new_checklist_item),
    url(r'get_items/', views.get_items),
    url(r'checklist_item_state/', views.change_checklist_item_state),
    url(r'delete_item/', views.deleteItem),
    url(r'my_events/', views.my_events),
    url(r'list_attendees/', views.list_attendees),
    url(r'update_event', views.update_event),
    url(r'delete_event', views.delete_event),
    url(r'list_invitees/', views.list_invitees),
    url(r'invite_connections/', views.invite_connection),
]
