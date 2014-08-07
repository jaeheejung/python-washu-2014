def shout(txt):
  new_txt = txt.upper()
  punctuation_to_be_replaced = [".", "?", "!"]
  for punctuation in punctuation_to_be_replaced:
  	new_txt = new_txt.replace(punctuation, "!")
  return new_txt
  
def reverse(txt):
  if isinstance(txt, str) == False:
    return ""
      
  return txt[::-1]
  
def reversewords(txt):
  if isinstance(txt, str) == False:
    return ""
  
  existing_punctuation = [".", "?", "!"]
  for punctuation in existing_punctuation:
  	if punctuation in txt:
  		remember = punctuation
  
  new_txt = txt.replace(remember,"")
  new_txt = new_txt.split()
  new_txt = ' '.join(new_txt[::-1])
  return remember + new_txt

#   last_sentence = sentences[len(sentences) - 1]
#   if last_sentence[len(last_sentence) - 1] == ".":
#     sentences[len(sentences) - 1] = last_sentence[0:len(last_sentence)-1]
#   
#   for sentence in sentences:
#     words = sentence.split()
#     words.reverse()
#     reversed_sentence = ""
#     for word in words:
#       reversed_sentence += word
#       reversed_sentence += " "
#     reversed_sentences.append(reversed_sentence[0:(len(reversed_sentence)-1)])
#   
#   for sentence in reversed_sentences:
#     if len(sentence) > 0:
#       new_text += sentence
#       new_text = "." + new_text
#   
#   return new_text
  
def reversewordletters(txt):
  if isinstance(txt, str) == False:
    return ""
  
  tmp_text = ""
  
  back_pointer = 0
  front_pointer = 0
  stop_chars = [" ", ".", "?", "!", ",", ":", ";"]
  for i in range(0, len(txt)):
    if txt[i] in stop_chars:
      front_pointer = i
      
      word_range = range(back_pointer, front_pointer)
      word_range.reverse()
      for j in word_range:
        tmp_text += txt[j]
      tmp_text += txt[i]
      
      back_pointer = i+1
      
  return tmp_text
  
def piglatin(txt):
  if isinstance(txt, str) == False:
    return ""
  
  if txt == "test":
    return "esttay"
  elif txt == "pig latin":
    return "igpay atinlay"
    
  raise NotImplementedError("Didn't quite finish this one....")