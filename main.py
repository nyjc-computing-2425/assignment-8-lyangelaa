# Built-in imports
def reverse(text):
    """
    Reverses text using a recursibe function
    
    Parameters
    ----------
    text: string
          text to be reversed
    """
    if len(text) == 0:
        return ""
    else:
        first_character = text[0]   
        rest_of_text = text[1:]
        reversed_text = reverse(rest_of_text)
        return reversed_text + first_character
def is_palindrome(text):
    """
    Checks if string is a palindrome using a recusive function
    
    Parameters
    ----------
    text: string
          text to checked
    """
    if len(text) <= 1:
        return True
    elif text[0] != text[-1]:
        return False
    else:
        return is_palindrome(text[1:-1])