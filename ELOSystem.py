import random

# Initialize the movies with their initial ELO ratings
movies_elo = {
    "Episode I: The Phantom Menace": 1500,
    "Episode II: Attack of the Clones": 1500,
    "Episode III: Revenge of the Sith": 1500,
    "Episode IV: A New Hope": 1500,
    "Episode V: The Empire Strikes Back": 1500,
    "Episode VI: Return of the Jedi": 1500,
    "Episode VII: The Force Awakens": 1500,
    "Episode VIII: The Last Jedi": 1500,
    "Episode IX: The Rise of Skywalker": 1500,
    "Rogue One: A Star Wars Story": 1500
}


def update_elo(rating_winner, rating_loser, k=32):
    expected_winner = 1 / (1 + 10 ** ((rating_loser - rating_winner) / 400))
    expected_loser = 1 - expected_winner

    new_rating_winner = rating_winner + k * (1 - expected_winner)
    new_rating_loser = rating_loser - k * expected_loser

    return new_rating_winner, new_rating_loser


def print_rankings(movies_elo):
    ranked_movies = sorted(movies_elo.items(), key=lambda x: x[1], reverse=True)
    for rank, (movie, rating) in enumerate(ranked_movies, start=1):
        print(f"{rank}. {movie}: {round(rating, 2)}")


def main():
    try:
        while True:
            # Randomly select two movies for comparison
            movie1, movie2 = random.sample(list(movies_elo.keys()), 2)
            print(f"Which movie do you prefer? \n1. {movie1}\n2. {movie2}\nType 1 or 2: ")

            # User makes a choice
            choice = input()
            if choice == '1':
                winner, loser = movie1, movie2
            elif choice == '2':
                winner, loser = movie2, movie1
            else:
                print("Invalid selection, please type 1 or 2.")
                continue

            # Update ratings based on the choice
            movies_elo[winner], movies_elo[loser] = update_elo(movies_elo[winner],
                                                               movies_elo[loser])

            # Display the updated rankings
            print("\nUpdated Rankings:")
            print_rankings(movies_elo)
            print("\nNext matchup, or type 'exit' to finish.")
            if input().lower() == 'exit':
                break
    except KeyboardInterrupt:
        print("\nSimulation ended.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
