import random

quotes = [
    "Life is what happens when you're busy making other plans. - John Lennon",
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Success is not final, failure is not fatal: it is the courage to continue that counts. - Winston Churchill",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "Be yourself; everyone else is already taken. - Oscar Wilde",
    "In the middle of difficulty lies opportunity. - Albert Einstein",
    "The best way to predict the future is to create it. - Peter Drucker",
    "It does not matter how slowly you go as long as you do not stop. - Confucius",
    "Everything you've ever wanted is on the other side of fear. - George Addair",
    "The only impossible journey is the one you never begin. - Tony Robbins"
]

def get_random_quote():
    """Return a random quote from the quotes list."""
    return random.choice(quotes)

def main():
    print("\nRandom Quote Generator")
    print("-" * 20)
    print(f"\n{get_random_quote()}\n")

if __name__ == "__main__":
    main()