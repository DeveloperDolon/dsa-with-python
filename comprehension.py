
users = [ #list comprehension
    "Dolon",
    "Durjoy",
    "Soumik",
    "Sowrav",
    "Rakhi",
    "Dolon",
    "Durjoy"
];

usersWithD = [user for user in users if user.startswith('D')];

# print(usersWithD);

recipes = { #set comprehension
    "Masala Chai": ["ginger", "cardamom", "clove"],
    "Elaichi Chai": ["cardamom", "milk"],
    "Spicy Chai": ["ginger", "black paper", "clove"]
}


unique_spicies = {spice for ingredients in recipes.values() for spice in ingredients}
# print(unique_spicies)


#dictionary comprehension
tea_prices_tk = {
    "Masala Chai" : 40,
    "Green Tea" : 50,
    "Lemon Tea" : 200
}

tea_price_in_usd = {tea:price / 100 for tea, price in tea_prices_tk.items()};
# print(tea_price_in_usd);


#generator comprehension
