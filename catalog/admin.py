from django.contrib import admin
from catalog.models import Author, Genre, Book, BookInstance

#admin.site.register(Book)
#admin.site.register(Author)
admin.site.register(Genre)
#admin.site.register(BookInstance)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    

admin.site.register(Author, AuthorAdmin)

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
      
    def display_genre(self):
        """Create a string for the Genre. This is required to display genre in Admin."""
        return ','.join(genre.name for genre in self.genre.all()[:3])

    display_genre.short_description = 'Genre'   
    
    list_display = ('title', 'author', display_genre)
    list_filter = ('title', 'author')
    inlines = [BooksInstanceInline]

# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
      list_filter = ('status', 'due_back')
      
      list_display =('book','due_back','imprint','id',)
         
      fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Disponibilidade', {
            'fields': ('status', 'due_back')
        }),
    )


