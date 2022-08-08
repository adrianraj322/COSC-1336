#Adrian Raj, Status-Complete
#Ask how many servings of spaghetti sauce you want to make and how much of the ingredients do you need
tomato_sauce = 2
tomato_paste = 0.333
cloves_garlic = 2
oregano = 1
serving = tomato_sauce + tomato_paste + cloves_garlic + oregano

#Spaghetti sauce requires 4 times that of a normal serving
spaghetti_sauce_serving = serving * 4
actual_amount_of_servings = float(input('How many servings do you want to make?: '))

#Total servings of the ingredients require one serving multiplied by the ingredient divided by 4
tomato_sauce_serving = actual_amount_of_servings * (tomato_sauce / 4)
tomato_paste_serving = actual_amount_of_servings * (tomato_paste / 4)
cloves_garlic_serving = actual_amount_of_servings * (cloves_garlic / 4)
oregano_serving = actual_amount_of_servings * (oregano / 4)

#Enter ending statements
print('If you want', actual_amount_of_servings, 'servings,', 'then you will need:')
print(format(tomato_sauce_serving, ',.2f'), 'servings of tomato sauce')
print(format(tomato_paste_serving, ',.2f'), 'servings of tomato paste,')
print(format(cloves_garlic_serving, '.2f'), 'servings of garlic cloves,')
print(format(oregano_serving, ',.2f'), 'servings of oregano')
