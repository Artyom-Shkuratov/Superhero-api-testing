# main.py
import requests

def get_tallest_hero_by_gender_and_work(gender, has_job):
    
    url = "https://akabab.github.io/superhero-api/api/all.json"
    response = requests.get(url)
    if response.status_code != 200:
        return None

    heroes = response.json()

    matching = [] 
    for hero in heroes:
        hero_gender = hero.get("appearance", {}).get("gender", "")
        occupation = hero.get("work", {}).get("occupation", "")
        occupation = occupation.strip()  
        hero_has_job = bool(occupation)
        if hero_gender == gender and hero_has_job == has_job:
            matching.append(hero)

    if not matching:
        return None
    
    tallest_hero = None
    max_height = 0.0 

    for hero in matching:
        height_list = hero.get("appearance", {}).get("height", [])
        if len(height_list) < 2:
            continue

        height_str = height_list[1]  
        parts = height_str.split()
        if not parts:
            continue

        try:
            height_value = float(parts[0])
        except ValueError:
            continue

        if height_value > max_height:
            max_height = height_value
            tallest_hero = hero

    if tallest_hero:
        return tallest_hero.get("name")
    else:
        return None


hero = get_tallest_hero_by_gender_and_work("Male", True)
print("Самый высокий мужской герой с работой:", hero)

hero = get_tallest_hero_by_gender_and_work("Female", True)
print("Самый высокий женский герой с работой:", hero)

hero = get_tallest_hero_by_gender_and_work("Male", False)
print("Самый высокий мужской герой без работы:", hero)

hero = get_tallest_hero_by_gender_and_work("Female", False)
print("Самый высокий женский герой без работы:", hero)


 