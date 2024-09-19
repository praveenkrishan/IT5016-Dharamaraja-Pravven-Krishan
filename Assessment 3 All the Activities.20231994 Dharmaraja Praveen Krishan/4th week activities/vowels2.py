def count_vowels(text):
    text = input("Enter the text: ")

text = input("Enter the text: ")


vowel_count = 0


vowels = "aeiou"


for char in text:
    if char in vowels:
        vowel_count += 1


print(f"Number of vowels in '{text}': {vowel_count}")
