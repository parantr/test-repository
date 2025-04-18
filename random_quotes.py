#!/usr/bin/env python3

import random

# List of quotes with their authors
quotes = [
    ("Be the change you wish to see in the world.", "Mahatma Gandhi"),
    ("Life is what happens when you're busy making other plans.", "John Lennon"),
    ("The only way to do great work is to love what you do.", "Steve Jobs"),
    ("I think, therefore I am.", "René Descartes"),
    ("In three words I can sum up everything I've learned about life: it goes on.", "Robert Frost"),
    ("To be yourself in a world that is constantly trying to make you something else is the greatest accomplishment.", "Ralph Waldo Emerson"),
    ("Two things are infinite: the universe and human stupidity; and I'm not sure about the universe.", "Albert Einstein"),
    ("The future belongs to those who believe in the beauty of their dreams.", "Eleanor Roosevelt"),
    ("Success is not final, failure is not fatal: it is the courage to continue that counts.", "Winston Churchill"),
    ("Be yourself; everyone else is already taken.", "Oscar Wilde")
]

def get_random_quote():
    """Return a random quote from the quotes list."""
    quote, author = random.choice(quotes)
    return f'"{quote}" - {author}'

def main():
    """Main function to generate and display a random quote."""
    print("\nRandom Quote Generator")
    print("-" * 20)
    print(get_random_quote())
    print()

if __name__ == "__main__":
    main()