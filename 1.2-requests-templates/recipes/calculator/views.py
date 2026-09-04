from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    'salad': {
        'огурец, шт': 2,
        'помидор, шт': 2,
        'лук, шт': 1,
        'масло, ст.л.': 2,
    },
}


def recipe_view(request, recipe_name):
    # Получаем рецепт
    recipe = DATA.get(recipe_name)

    # Если рецепта нет
    if recipe is None:
        return render(request, 'calculator/index.html', {'recipe': {}})

    # Проверяем параметр servings
    servings = request.GET.get('servings')

    # Если servings передан и это число > 0
    if servings is not None:
        try:
            servings = int(servings)
            if servings > 0:
                # Умножаем все ингредиенты
                multiplied_recipe = {}
                for ingredient, amount in recipe.items():
                    multiplied_recipe[ingredient] = round(amount * servings, 2)
                recipe = multiplied_recipe
        except ValueError:
            # Если не число — игнорируем
            pass

    return render(request, 'calculator/index.html', {'recipe': recipe})