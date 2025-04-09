"""A hello world program with intentionally bad indentation."""

def main():
   # Only keeping one print statement
   print("Hello World!")
   message = "Using three spaces"

def another_function():
  # Removed print statement as per feedback
  message = "Using two spaces"
  return message

def third_function():
        # Removed print statement as per feedback
        message = "Using eight spaces"
        return message

if __name__ == "__main__":
 main()  # Single space indentation