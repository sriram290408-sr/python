def high_low(temp):
    avg_li = []
    cities = []
    for city, temps in temp.items():
        a = sum(temps) / len(temps)
        avg_li.append(a)
        cities.append(city)
    maximum = max(avg_li)
    minimum = min(avg_li)
    
    max_city = cities[avg_li.index(maximum)]
    min_city = cities[avg_li.index(minimum)]
    
    print("Highest Avg:",max_city)
    print("Lowest Avg:",min_city)

high_low({
    "Chennai": [32, 33, 31, 35],
    "Bangalore": [27, 28, 26, 29],
    "Delhi": [35, 36, 38, 37],
})
