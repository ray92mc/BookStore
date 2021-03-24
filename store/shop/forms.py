from django.forms import ModelForm
from .models import Book, Category,Review


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['subject', 'comment']