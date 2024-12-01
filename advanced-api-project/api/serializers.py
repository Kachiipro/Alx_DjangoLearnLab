from .models import Book, Author

from rest_framework import serializers

class BookSerializer(serializers.ModelSerializer):
   
    class meta:
       model =  Book
       field = '__all__'

    def validate(self, data): # validate method checks if publication year is in the future
        if (data['publication_year']) < 2024:
            raise serializers.ValidationError("publication should not be in the future")
        return data

class AuthorSerializer(serializers.ModelSerealizer): #This allows the API to return the authors data along with its related Books.
    comments = BookSerializers(many=True, read_only=True)
    class meta:
        model = Author
        field = ['name']