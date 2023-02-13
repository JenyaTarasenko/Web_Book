from django.contrib import admin
from .models import *



#регистрация моделей в админке
#admin.site.register(Autor)

#admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Language)
#admin.site.register(BookIntance)

@admin.register(Autor)# регистрация в админке
class AutorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'date_of_death') #расширяем админку
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]#формируем список для авторов по горизонтали
    # exclude для списка кторые будут исключены
    


@admin.register(Book)# регистрация в админке
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'language', 'display_autor')#'display_autor'- прописываем в models.py
    list_filter = ('genre', 'autor')#фильтрация книжек по жанру и автору(фильтр справа)




@admin.register(BookIntance)# регистрация в админке
class BookIntanceAdmin(admin.ModelAdmin):
    list_filter = ('book', 'status')