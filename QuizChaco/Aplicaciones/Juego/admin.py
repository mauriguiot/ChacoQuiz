from django.contrib import admin
from .models import pregunta, respuesta, categoria

# Register your models here.

class AnswerInline(admin.TabularInline):
	model = respuesta

class QuestionAdmin(admin.ModelAdmin):
	inlines = [AnswerInline]

admin.site.register(pregunta, QuestionAdmin)
admin.site.register(respuesta)
admin.site.register(categoria)