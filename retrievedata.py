menu = {'starter': 'pakora', 'main': 'murghi masala', 'dessert': 'ice cream'}
print(menu.get('starter'))

menu['dessert'] = 'floater coffee'
print(menu.get('dessert'))

menu.update ({'drink' : 'dr pepper'}) 
print(menu)
