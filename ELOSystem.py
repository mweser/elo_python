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


# Elo Rating Adjustment Function
def update_elo(rating_winner, rating_loser, k=32):
    """
    Calculate the new ELO ratings for the winner and loser of a matchup.
    The function takes the current ratings of the winner and loser, and a K-factor which determines the maximum rating change.
    Returns the new ratings for both the winner and loser.
    """
    expected_winner = 1 / (1 + 10 ** ((rating_loser - rating_winner) / 400))
    expected_loser = 1 - expected_winner

    new_rating_winner = rating_winner + k * (1 - expected_winner)
    new_rating_loser = rating_loser + k * (0 - expected_loser)

    return new_rating_winner, new_rating_loser


# Example of updating the ratings based on a matchup outcome
winner = "Episode V: The Empire Strikes Back"
loser = "Rogue One: A Star Wars Story"

# Update the ratings
movies_elo[winner], movies_elo[loser] = update_elo(movies_elo[winner], movies_elo[loser])

# Print updated ratings
for movie, rating in movies_elo.items():
    print(f"{movie}: {rating}")
