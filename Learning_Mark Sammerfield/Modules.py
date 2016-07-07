import string

def clear(text, whitespace=string.whitespace, delete=''):
   result = []
   word = ""
   for char in text:
       if char in delete:
            continue
       elif char in whitespace:
            if word:
                result.append(word)
                word = ""
            else:
                word += char
       if word:
                result.append(word)
       
       return " ".join(result)
 

   print(clear('nichosi', delete = 'i'))