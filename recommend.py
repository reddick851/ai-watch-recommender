# recommend.py
# Tiny "what should I watch?" demo using simple text matching.
movies = {
    "Guardians of the Galaxy": "funny sci-fi adventure with a group of misfits in space",
    "Interstellar": "serious sci-fi drama about space, time, and saving humanity",
    "The Martian": "light-hearted survival story about an astronaut stranded on Mars",
    "The Notebook": "emotional romantic drama about love and memory",
    "Spider-Man: Homecoming": "funny superhero coming-of-age story with action and humor",
}

def recommend(user_feeling):
    user_words = user_feeling.lower().split()
    scores = {}

    for title, desc in movies.items():
        desc_words = desc.lower().split()
        # simple score: how many words overlap
        overlap = len(set(user_words) & set(desc_words))
        scores[title] = overlap

    # sort by score, highest first
    ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    return ranked

if __name__ == "__main__":
    print("What do you feel like watching? (e.g. 'funny sci-fi', 'emotional romance')")
    user_input = input("> ")

    results = recommend(user_input)

    print("\nTop suggestions:")
    for title, score in results:
        if score > 0:
            print(f"- {title} (score: {score})")

    if all(score == 0 for _, score in results):
        print("Hmm, nothing matched well. Try different words like 'funny', 'sci-fi', 'romantic', 'serious'.")
