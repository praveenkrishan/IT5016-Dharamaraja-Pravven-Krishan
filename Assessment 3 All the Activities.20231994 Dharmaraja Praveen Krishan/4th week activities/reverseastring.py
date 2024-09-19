def reverse_string(s):
    reversed_str =""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str



def main():
    original_str = input("enter a string")
    praveen = reverse_string(original_str)
    print(f"original:{original_str}")
    print(f"reversed: {praveen}")


main()    