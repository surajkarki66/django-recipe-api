from rest_framework import serializers

from recipe.models import Ingredient, Recipe, Tag


class TagSerializer(serializers.ModelSerializer):
    """ Serializes tag objects """

    class Meta:
        model = Tag
        fields = ('id','name')
        read_only_fields = ('id',)


class IngredientSerializer(serializers.ModelSerializer):
    """ Serializes ingredient object """

    class Meta:
        model = Ingredient
        fields = ('id','name')
        read_only_fields = ('id',)



class RecipeSerializer(serializers.ModelSerializer):
    """ Serialize a recipe """
    ingredients = serializers.PrimaryKeyRelatedField(
       many=True, 
       queryset = Ingredient.objects.all()
    )

    tags = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset = Tag.objects.all()
    )


    class Meta:
        model = Recipe
        fields = (
            'id', 'title', 'ingredients', 'tags', 'time_minutes',
            'price', 'link'
        )
        read_only_fields = ('id',)




