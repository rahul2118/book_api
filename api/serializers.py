from rest_framework import serializers
from .models import Book, Author, Language, Genre, Publisher


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name']


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ['name']


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['name']


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ['name', 'address']


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    language = LanguageSerializer()
    genre = GenreSerializer()
    publisher = PublisherSerializer()

    class Meta:
        model = Book
        fields = ['title', 'author', 'language', 'genre',
                  'publisher', 'min_age', 'price', 'stock', 'description']

    def create(self, validated_data):
        author_data = validated_data.pop('author')
        language_data = validated_data.pop('language')
        genre_data = validated_data.pop('genre')
        publisher_data = validated_data.pop('publisher')

        author = Author.objects.create(**author_data)
        language = Language.objects.create(**language_data)
        genre = Genre.objects.create(**genre_data)
        publisher = Publisher.objects.create(**publisher_data)

        book = Book.objects.create(
            author=author,
            language=language,
            genre=genre,
            publisher=publisher,
            **validated_data
        )
        return book

    def update(self, instance, validated_data):
        author_data = validated_data.pop('author')
        author, created = Author.objects.get_or_create(**author_data)
        instance.author = author

        language_data = validated_data.pop('language')
        language, created = Language.objects.get_or_create(**language_data)
        instance.language = language

        genre_data = validated_data.pop('genre')
        genre, created = Genre.objects.get_or_create(**genre_data)
        instance.genre = genre

        publisher_data = validated_data.pop('publisher')
        publisher, created = Publisher.objects.get_or_create(**publisher_data)
        instance.publisher = publisher

        instance.title = validated_data.get('title', instance.title)
        instance.min_age = validated_data.get('min_age', instance.min_age)
        instance.price = validated_data.get('price', instance.price)
        instance.stock = validated_data.get('stock', instance.stock)
        instance.description = validated_data.get(
            'description', instance.description)

        instance.save()
        return instance
