from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("results", views.results, name="results"),
    path("search_api", views.search_api, name="search_api"),
    path("entry/<int:entry_id>", views.entry, name="entry"),
    path("entries", views.entries, name="entries"),
    path("scroll_entries_api", views.scroll_entries_api, name="scroll_entries_api"),
    path("word_families", views.word_families, name="word_families"),
]
