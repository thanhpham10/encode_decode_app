# Encode Decode Software

Run app using command :
```
git clone https://github.com/thanhpham10/encode_decode_app.git
```
```
cd encode_decode_app
```
```
python main.py
```

### __do not run software with python 2.x__

## ENCODE FUNCTION
```def encode(text="", *,key=0):
    en_text = ""
    for char in text :
        en_text += chr(ord(char) + int(key))

    return en_text
```
## DECODE FUNCTION
```def decode(text="", *,key=0):
    de_text = ""
    for char in text :
        de_text += chr(ord(char) - int(key))

    return de_text
```
