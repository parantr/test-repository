import java.util.Random;

public class RandomQuote {
    private static final String[] QUOTES = {
        "Be the change you wish to see in the world. - Mahatma Gandhi",
        "I have a dream. - Martin Luther King Jr.",
        "The only way to do great work is to love what you do. - Steve Jobs",
        "Success is not final, failure is not fatal: it is the courage to continue that counts. - Winston Churchill",
        "Life is what happens when you're busy making other plans. - John Lennon",
        "In three words I can sum up everything I've learned about life: it goes on. - Robert Frost",
        "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
        "The best way to predict the future is to create it. - Peter Drucker",
        "Everything you've ever wanted is on the other side of fear. - George Addair",
        "The purpose of our lives is to be happy. - Dalai Lama"
    };
    
    public static String getRandomQuote() {
        Random random = new Random();
        return QUOTES[random.nextInt(QUOTES.length)];
    }
    
    public static void main(String[] args) {
        System.out.println("Your random quote for today:");
        System.out.println(getRandomQuote());
    }
}