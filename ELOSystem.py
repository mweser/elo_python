import random

nolan_movies_elo = {
    "Memento": 1500,
    "Batman Begins": 1500,
    "The Prestige": 1500,
    "The Dark Knight": 1500,
    "Inception": 1500,
    "The Dark Knight Rises": 1500,
    "Interstellar": 1500,
    "Dunkirk": 1500,
    "Tenet": 1500,
    "Oppenheimer": 1500
}

villeneuve_movies_elo = {
    "Prisoners": 1500,
    "Enemy": 1500,
    "Sicario": 1500,
    "Arrival": 1500,
    "Blade Runner 2049": 1500,
    "Dune (Parts 1&2)": 1500,
}

movies_favorites_elo = {
    "Amelie": 1500,
    "1917": 1500,
    "EEAAO": 1500,
    "Gladiator": 1500,
    "Whiplash": 1500,
    "The Social Network": 1500,
    "The Matrix": 1500,
    "The Godfather Part I": 1500,
    "The Godfather Part II": 1500,
    "Citizen Kane": 1500,
    "Pulp Fiction": 1500,
    "Fight Club": 1500,
    "Inglourious Basterds": 1500,
    "Kill Bill Vol. 1": 1500,
    "Kill Bill Vol. 2": 1500,
    "Django Unchained": 1500,
    "Ex Machina": 1500,
    "Scott Pilgrim vs. The World": 1500,
    "The Martian": 1500,
    "The Grand Budapest Hotel": 1500,
    "O Brother, Where Art Thou?": 1500,
    "Fargo": 1500,
    "No Country for Old Men": 1500,
    "Inside Llewyn Davis": 1500,
    "Hail, Caesar!": 1500,
    "The Ballad of Buster Scruggs": 1500,
    "The French Dispatch": 1500,
    "Saving Private Ryan": 1500,
    "The Pianist": 1500,
    "Apocalypse Now": 1500,
    "Doctor Strangelove": 1500,
    "Death of Stalin": 1500,
    "Indiana Jones: Raiders of the Lost Ark": 1500,
    "Indiana Jones: The Last Crusade": 1500,
    "Nightcrawler": 1500,
    "Lawrence of Arabia": 1500,
    "Duck Soup": 1500,
    "A Night at the Opera": 1500,
    "The Lord of the Rings": 1500,
}

star_wars_movies_best_elo = {
    "Episode III: Revenge of the Sith": 1500,
    "Episode IV: A New Hope": 1500,
    "Episode V: The Empire Strikes Back": 1500,
    "Rogue One: A Star Wars Story": 1500
}

star_wars_movies_elo = {
    "Episode I: The Phantom Menace": 1500,
    "Episode II: Attack of the Clones": 1500,
    "Episode III: Revenge of the Sith": 1500,
    "Episode IV: A New Hope": 1500,
    "Episode V: The Empire Strikes Back": 1500,
    "Episode VI: Return of the Jedi": 1500,
    "Episode VII: The Force Awakens": 1500,
    "Episode VIII: The Last Jedi": 1500,
    "Episode IX: The Rise of Skywalker": 1500,
    "Solo: A Star Wars Story": 1500,
    "Rogue One: A Star Wars Story": 1500
}


# Initialize the movies with their initial ELO ratings
movies_elo = {
    **nolan_movies_elo,
    **villeneuve_movies_elo,
    **star_wars_movies_best_elo,
    **movies_favorites_elo,
}

# To avoid repeating matchups too frequently
previous_matchups = set()


def update_elo(rating_winner, rating_loser, k=32):
    expected_winner = 1 / (1 + 10 ** ((rating_loser - rating_winner) / 400))
    expected_loser = 1 - expected_winner

    new_rating_winner = rating_winner + k * (1 - expected_winner)
    new_rating_loser = rating_loser - k * expected_loser

    return new_rating_winner, new_rating_loser


def print_rankings(movies_elo):
    ranked_movies = sorted(movies_elo.items(), key=lambda x: x[1], reverse=True)
    print("\nCurrent Rankings:")
    for rank, (movie, rating) in enumerate(ranked_movies, start=1):
        print(f"{rank}. {movie}: {round(rating, 2)}")


def get_random_matchup(movies_elo):
    while True:
        movie1, movie2 = random.sample(list(movies_elo.keys()), 2)
        matchup = frozenset([movie1, movie2])
        if matchup not in previous_matchups:
            previous_matchups.add(matchup)
            return movie1, movie2


def main():
    count = 0
    try:
        while True:
            count += 1
            movie1, movie2 = get_random_matchup(movies_elo)
            print(
                f"\n{count}. Which movie do you prefer? \n1. {movie1}\n2. {movie2}\nType 1 or 2, or 'exit' to finish: ")

            choice = input()
            if choice == 'exit':
                break
            elif choice == '1':
                winner, loser = movie1, movie2
            elif choice == '2':
                winner, loser = movie2, movie1
            else:
                print("Invalid selection, please type 1 or 2.")
                continue

            movies_elo[winner], movies_elo[loser] = update_elo(movies_elo[winner],
                                                               movies_elo[loser])
            print_rankings(movies_elo)

    except KeyboardInterrupt:
        print("\nSimulation ended.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
