chai_order = dict(type="Masala Chai",size="Large",sugar=2)
print(f"chai order : {chai_order}")
chai_recipe = {}
chai_recipe["base"]="black tea"
chai_recipe["liquid"]="milk"
print(f"Recipie base:{chai_recipe['base']}")
del chai_recipe['liquid']
print(f"chai recipie::{chai_recipe}")
print(f"Order details (keys) : {chai_order.keys()}")
print(f"Order details (values): {chai_order.values()}")
print(f"print chai order items: {chai_order.items()}")
last_item = chai_order.popitem()
print(f"Removed last item : {last_item}")
extra_spices = {"cardamom":"crushed","ginger":"sliced"}
print(f"Updated chai_recipie:{chai_recipe}")
chai_size = chai_order.get("note","No note")
print(f"Chai size is : {chai_size}")