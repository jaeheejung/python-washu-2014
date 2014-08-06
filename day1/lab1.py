def binarify(num): 
  """convert positive integer to base 2"""
  if num<=0: return '0'
  digits = []
  for i in range(0,100):
  	if num/(2**i) > 1:
  		continue
  	else:
  		digits.append('1')
  		num = num - 2**i
  		length = i
  		break
  for j in range((length-1), -1, -1):
  	if num/(2**j) >= 1:
  		digits.append('1')
  		num = num - (2**j)
  	else:
  		digits.append('0')
  return ''.join(digits)

def int_to_base(num, base):
  """convert positive integer to a string in any base"""
  if num==0:  return '0' 
  if base<=0: return '0'
  if base==1: return '1'*num
  digits = []
  negative=False
  if num<0: num*=(-1); negative=True
  while num>0:
    digits.append(num%base)
    num=num/base
  digits=digits[::-1]
  if negative: return '-'+''.join(str(e) for e in digits)
  return ''.join(str(e) for e in digits)

def base_to_int(string, base):
  """take a string-formatted number and its base and return the base-10 integer"""
  if string=="0" or base <= 0 :
  	return 0 	
  elif base == 10 :
  	return int(string)
  else :
  	negative = False
  	if int(string) < 0:
  		string = string[1:]
  		negative = True
  	length = len(string)
  	result = 0
  	for i in string:
  		length -= 1
  		result += (base ** length) * int(i)
  	if negative:
  		result *= (-1)
  return result
  	
def flexibase_add(str1, str2, base1, base2):
  """add two numbers of different bases and return the sum"""
  total = base_to_int(str1, base1) + base_to_int(str2, base2)
  return int_to_base(total, 2)

def flexibase_multiply(str1, str2, base1, base2):
  """multiply two numbers of different bases and return the product"""
  total = base_to_int(str1, base1) * base_to_int(str2, base2)
  return int_to_base(total, 2)

def romanify(num):
  """given an integer, return the Roman numeral version"""
  ones = ['','I','II','III','IV','V','VI','VII','VIII','IX']
  tens = ['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC']
  hundreds = ['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM']
  thousands = ['','M','MM','MMM']
  roman = [ones, tens, hundreds, thousands]
  length = len(str(num))
  result = []
  for i in str(num):
  	length -= 1
  	result.append(roman[int(length)][int(i)])
  return ''.join(result)