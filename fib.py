def is_palindrome(text):
    cleaned=text.lower().replace(' ','')
    reversed_text=cleaned[::-1]
    return cleaned==reversed_text
phrase=input('enter a word of phrase : ')
if is_palindrome(phrase):
    print(f" '{phrase}' is a palindrome")
else:
    print(f" '{phrase}' is not a palindrome")