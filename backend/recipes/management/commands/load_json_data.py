# flake8: noqa
import json

from django.core.management.base import BaseCommand

from foodgram_backend.local_settings import (
    FILE_PATH,
    FILE_PATH_TAGS,
    FILE_PATH_USERS,
    FILE_PATH_RECIPES
)
from recipes.models import Ingredient, Tag, Recipe, IngredientRecipe
from users.models import User


class Command(BaseCommand):
    help = 'Загрузка данных из JSON файлов'

    def handle(self, *args, **options):
        with open(FILE_PATH, encoding="utf8") as f:
            data = json.load(f)
            for item in data:
                try:
                    Ingredient.objects.create(**item)
                except:
                    pass
        with open(FILE_PATH_TAGS, encoding="utf8") as f:
            data = json.load(f)
            for item in data:
                try:
                    Tag.objects.create(**item)
                except:
                    pass
        with open(FILE_PATH_USERS, encoding="utf8") as f:
            data = json.load(f)
            for item in data:
                try:
                    user = User.objects.create(**item)
                    user.set_password(item['password'])
                    user.save()
                except:
                    pass

        with open(FILE_PATH_RECIPES, encoding="utf8") as f:
            data = json.load(f)
            for el in data:
                author = el.pop('author')
                tags = el.pop('tags')
                ingredients = el.pop('ingredients')
                author_name = User.objects.get(username=author['username'])
                el['author'] = author_name
                recipe = Recipe.objects.create(**el)
                for ing in ingredients:
                    IngredientRecipe.objects.create(
                        recipe=recipe,
                        ingredients=Ingredient.objects.get(name=ing['name']),
                        amount=ing['amount'])
                t_list = []
                for t in tags:
                    tag = Tag.objects.get(name=t['name'])
                    t_list.append(tag.id)
                    # print(type(tag))
                recipe.tags.set(t_list)
                recipe.save()


        self.stdout.write(
            self.style.SUCCESS('Загрузка данных прошла успешно.'))
