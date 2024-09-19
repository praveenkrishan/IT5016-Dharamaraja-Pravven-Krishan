def count_of_vowels(text):
    vowels = "aeiou"
    count = 0

    for char in text:
        if char in vowels:
         count+=1
        return count
    
def main():
   text = input("enter the text:")
   vowel_count = count_of_vowels(text)
   print(f"number of vowels in {text}: {vowel_count}")

main()   
       

    