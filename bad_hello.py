"""A hello world program with intentionally bad indentation."""

def main():
    """Main function that prints hello world."""
    # Only keeping one print statement
    print("Hello World!")

def another_function():
  """Second function with proper docstring."""
  # Using 2 spaces for bad indentation
  return "Using two spaces"

def third_function():
        """Third function with proper docstring."""
        # Using 8 spaces for bad indentation
        return "Using eight spaces"

if __name__ == "__main__":
    main()  # Using standard 4 spaces