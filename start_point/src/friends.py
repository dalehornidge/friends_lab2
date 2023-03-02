def get_name(person):
    return person["name"]

def get_favourite_tv_show(person):
    return person["favourites"]["tv_show"]

def likes_to_eat(person, test_food):
    result = False
    for favourites in person["favourites"]["snacks"]:
        if favourites == test_food:
            result = True
    return result
        
def add_friend(person, new_friend):
    person ["friends"].append(new_friend)

def remove_friend(person, old_friend):
    person["friends"].remove("Fred")

def total_money(people):
    total_sum = 0
    for person in people:
        total_sum += person["monies"]
    return total_sum

def lend_money(lender, borrower, amount):
    lender["monies"] -= amount
    borrower["monies"] += amount

def all_favourite_foods(people):
    all_faves = []
    for person in people:
        for food in person["favourites"]["snacks"]:
            all_faves.append(food)
    return all_faves 

def find_no_friends(people):
    friendless = []
    for person in people:
        if len(person["friends"]) == 0:
            friendless.append(person)
    return friendless

def unique_favourite_tv_shows(people):
    unique_shows = []
    for person in people:    
        fave_show = person["favourites"]["tv_show"]
        if unique_shows.count(fave_show) == 0:
            unique_shows.append(fave_show)    

    return unique_shows