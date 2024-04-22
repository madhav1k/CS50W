from django.contrib import admin
from .models import Entry, EntriesRelation, FamilialRelation

# Register your models here.
admin.site.register(Entry)
admin.site.register(EntriesRelation)
admin.site.register(FamilialRelation)