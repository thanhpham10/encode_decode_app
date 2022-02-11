from os import system


def encode(text="", *,key=0):
    en_text = ""
    for char in text :
        en_text += chr(ord(char) + int(key))

    return en_text

def decode(text="", *,key=0):
    de_text = ""
    for char in text :
        de_text += chr(ord(char) - int(key))

    return de_text

def main():
    print("decode and encode by thanh")
    system("cls")
    print("""Choose mode :
+ encode 
+ decode """)
    mode = input("choose mode : ").lower()

    if mode == "encode":
        text = input("text to (encode / decode) => ")
        space = input("enter space text (key) (1 -> 10000) => ")        
        print(f"your text is {encode(text, key=space)}")

    elif mode == "decode":
        text = input("text to (encode / decode) => ")
        space = input("enter space text (key) (1 -> 10000) => ")
        print(f"your text is {decode(text, key=space)}")

    else:
        print("there was wrong")
        print("")
        print("="*100)
        print(" please choose encode or decode ".center(100,"="))        
        print("="*100)
    
    input("...")

if __name__ == "__main__":
    main()

