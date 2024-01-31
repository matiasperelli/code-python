import emoji

txt = str(input("Input: "))

e = emoji.emojize(txt, language="alias")
print(f"Output: {e}")

#Harvard CS50
