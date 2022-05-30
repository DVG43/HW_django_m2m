from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Scope, Article, Topic

#Однако в этой задаче вам потребуется добавить дополнительную проверку при сохранении объекта.
#Для этого в объекте Inline'а можно переопределить атрибут formset, который должен указывать
#на специальный класс типа BaseInlineFormSet, нужный для обработки списка однотипных форм
#(каждая для своей связи).

class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        for form in self.forms:
            # В form.cleaned_data будет словарь с данными
            # каждой отдельной формы, которые вы можете проверить
            form.cleaned_data
            # вызовом исключения ValidationError можно указать админке о наличие ошибки
            # таким образом объект не будет сохранен,
            # а пользователю выведется соответствующее сообщение об ошибке
            raise ValidationError('Тут всегда ошибка')
        return super().clean()  # вызываем базовый код переопределяемого метода

class ScopeInline(admin.TabularInline):
      model = Scope
      formset = ScopeInlineFormset

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    #list_display = ['id', 'Название', 'Текст', 'Дата публикации', 'Изображение', ]
    inlines = (ScopeInline,)

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    inlines = (ScopeInline,)