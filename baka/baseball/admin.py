from django.contrib import admin
from .models import Batter, Statline

"""
class BatterModelAdmin(admin.ModelAdmin):
    list_display = ["player", "pos", "rank"]
    list_filter = [["player", "pos", "rank"]]
    list_editable = ["rank"]
    search_fields = ["player", "pos"]
    class Meta:
	    model = Batter

"""



admin.site.register(Batter)
admin.site.register(Statline)


# Register your models here.
