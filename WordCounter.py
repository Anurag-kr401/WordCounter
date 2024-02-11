def word_counter(text):
    # Split the text by spaces to get individual words
    words = text.split()
    
    # Return the number of words
    return len(words)

def main():
    # Prompt the user to enter a sentence or paragraph
    text = input("Please enter a sentence or paragraph: ")
    
    # Check if the input is not empty
    if text:
        # Call the word_counter function and store its return value
        word_count = word_counter(text)
        
        # Print the word count to the console
        print(f"The text you entered contains {word_count} words.")
    else:
        print("You entered an empty text. Please try again.")

# Call the main function to start the program
if __name__ == "__main__":
    main()
