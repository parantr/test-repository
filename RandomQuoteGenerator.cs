using System;
using System.Collections.Generic;

class RandomQuoteGenerator
{
    private static readonly List<string> quotes = new List<string>
    {
        "Believe you can and you're halfway there. -Theodore Roosevelt",
        "The future belongs to those who believe in the beauty of their dreams. -Eleanor Roosevelt",
        "It does not matter how slowly you go as long as you do not stop. -Confucius",
        "Success is not final, failure is not fatal: it is the courage to continue that counts. -Winston Churchill",
        "The only way to do great work is to love what you do. -Steve Jobs",
        "Everything you've ever wanted is sitting on the other side of fear. -George Addair",
        "Don't watch the clock; do what it does. Keep going. -Sam Levenson",
        "The secret of getting ahead is getting started. -Mark Twain",
        "You are never too old to set another goal or to dream a new dream. -C.S. Lewis",
        "Quality is not an act, it is a habit. -Aristotle"
    };

    static void Main(string[] args)
    {
        Random random = new Random();
        while (true)
        {
            Console.WriteLine("\nPress Enter for a random motivational quote (or 'q' to quit):");
            string input = Console.ReadLine();
            
            if (input?.ToLower() == "q")
                break;

            int index = random.Next(quotes.Count);
            Console.WriteLine("\n" + quotes[index]);
        }
    }
}