from django.contrib import admin

from parser.models import Spell, CharacterClass


@admin.register(Spell)
class SpellAdmin(admin.ModelAdmin):
    pass
