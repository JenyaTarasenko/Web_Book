from django.db import models
from django.urls import reverse


# Жанр книги
class Genre(models.Model):
    name = models.CharField(max_length=200, help_text='Введите жанр книги', verbose_name='Жанр книги')

   # возврат название жанра
    def __str__(self):
        return self.name



# язык книг
class Language(models.Model):
    name = models.CharField(max_length=20, help_text="Введите язык книги", verbose_name="Язык книги")

    # вщзврат название языка
    def __str__(self):
        return self.name


# автор книг
class Autor(models.Model):
    first_name = models.CharField(max_length=100,
                                  help_text="Введите имя автора",
                                  verbose_name="Имя автора")
    last_name = models.CharField(max_length=100, help_text="Введите фамилию автора",
                                 verbose_name="Фамилия автора")
    date_of_birth = models.DateField(help_text="Введите дату рождения",
                                     verbose_name="Дата рождения",
                                     null=True, blank=True)
    date_of_death = models.DateField(help_text="Введите дату смерти",
                                     verbose_name="Дата смерти",
                                     null=True, blank=True)

    # возврат Фамилии автора
    def __str__(self):
        return self.last_name



class Book(models.Model):
    title = models.CharField(max_length=200, help_text="Введите название книги",
                             verbose_name="Название книги")
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE,
                              help_text="Выберити жанр книги",
                              verbose_name="Жанр книги", null=True)
    language = models.ForeignKey('Language', on_delete=models.CASCADE, help_text="Выберите язык книги",
                                 verbose_name="Язык книги", null=True)
    autor = models.ManyToManyField('Autor', help_text="Выберите автора книги",
                                   verbose_name='Автор книги')
    summary = models.TextField(max_length=1000, help_text="Введите краткое описание книги",
                               verbose_name="Аннотация книги")
    isbn = models.CharField(max_length=13, help_text="Должно содержать 13 символов",
                            verbose_name="ISBN книги")


    # возвращает название книги
    def __str__(self):
        return self.title


    # возвращает URL-адрес для доступа к определенному экземпляру книги
    def get_absolute_url(self):
        return revers('book-detail', arg=[str(self.id)])


    # вытягиваем авторов для админки
    def display_autor(self):
        return ', '.join([autor.last_name for autor in self.autor.all()])
    display_autor.short_description = "Авторы"


# статус книги
class Status(models.Model):
    name = models.CharField(max_length=20, help_text="Введите статус экземпляра книги",
                            verbose_name="Статус экземпляра книги")

   # возврат значения статуса
    def __str__(self):
        return self.name


class BookIntance(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE, null=True)
    inv_nom = models.CharField(max_length=20, null=True,
                               help_text="Введите инвентарный номер экземпляра",
                               verbose_name="Инвентарный номер")
    imprint = models.CharField(max_length=200,
                              help_text="Ведите издательство и год выпуска",
                              verbose_name="Издательство")
    status = models.ForeignKey('Status', on_delete=models.CASCADE,
                               null=True, help_text="Изменить состояния экземпляра",
                               verbose_name="Статус экземпляра книги")
    due_back = models.DateField(null=True, blank=True, help_text="Введите конец срока статуса",
                                verbose_name="Дата окончания статуса")

    def __str__(self):
        return '%s %s %s' % (self.inv_nom, self.book, self.status)

