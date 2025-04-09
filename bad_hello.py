"""A hello world program with intentionally bad indentation."""

def main():
    """Main function that prints hello world."""
    # Only keeping one print statement
    print("Hello World!")
    message = "Using three spaces"

def another_function():
    """Second function with proper docstring."""
    # Removed print statement as per feedback
    message = "Using two spaces"
    return message

def third_function():
    """Third function with proper docstring."""
    # Removed print statement as per feedback
    message = "Using eight spaces"
    return message

if __name__ == "__main__":
    main()  # Using standard 4 spaces