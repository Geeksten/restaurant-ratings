def ratings_format(filename):
    """Takes txt file with list of restaurant ratings and prints strings of restaurant name and rating value.
    """

    restaurant_ratings_dict = {}

    ratings_file = open(filename)

    for line in ratings_file:
        name_score = line.rstrip()
        name_score = name_score.split(":")
        restaurant_ratings_dict[name_score[0]] = name_score[1]

    print "Add a new restaurant."
    new_restaurant = raw_input("Restaurant: ")
    new_rating = int(raw_input("Rating: "))
    restaurant_ratings_dict[new_restaurant] = new_rating
    
    sorted_ratings_dict = sorted(restaurant_ratings_dict)

    for restaurant in sorted_ratings_dict:
        print "{} is rated at {}.".format(restaurant, restaurant_ratings_dict[restaurant])

ratings_format("scores.txt")
