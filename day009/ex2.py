travel_log = [
    {
        "country": "France", 
        "cities": ["Paris", "Lille", "Dijon"],
        "visits": 12,
    },
    {
        "country": "Germany",
        "cities": ["Berlin", "Hamburg", "Stuttgart"],
        "visits": 5,
    },
]

def add_new_country(country, cities, visits):
    new_country = {
        "country": country,
        "cities": cities,
        "visits": visits,
    }
    travel_log.append(new_country)

add_new_country(country = "Russia", visits = 2, cities = ["Moscow", "Saint Petersburg"])

print(travel_log)