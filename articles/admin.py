from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Scope, Article, Tag

#Однако в этой задаче вам потребуется добавить дополнительную проверку при сохранении объекта.
#Для этого в объекте Inline'а можно переопределить атрибут formset, который должен указывать
#на специальный класс типа BaseInlineFormSet, нужный для обработки списка однотипных форм
#(каждая для своей связи).

class TagInlineFormset(BaseInlineFormSet):
    def clean(self):
        index = 0
        for form in self.forms:
            # В form.cleaned_data будет словарь с данными каждой отдельной формы, которые вы можете проверить
            if form.cleaned_data['is_main']:
                index += 1
                if index > 1:
                    raise ValidationError('Тут всегда ошибка')
            # вызовом исключения ValidationError можно указать админке о наличие ошибки
            # таким образом объект не будет сохранен,
            # а пользователю выведется соответствующее сообщение об ошибке
        if index == 0:
            ValidationError('Тут всегда ошибка')
        return super().clean()  # вызываем базовый код переопределяемого метода

class TagInline(admin.TabularInline):
      model = Tag
      formset = TagInlineFormset

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    #list_display = ['id', 'Название', 'Текст', 'Дата публикации', 'Изображение', ]
    inlines = (TagInline,)

@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    inlines = (TagInline,)