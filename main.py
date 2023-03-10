# exercise-01 Vowel or Consonant

# Write the code that:
# 1. Prompts the user to enter a letter in the alphabet:
#      Please enter a letter from the alphabet (a-z or A-Z):

# 2. Write the code that determines whether the letter entered is a vowel
# 3. Print one of following messages (substituting the letter for x):
#      - The letter x is a vowel
#      - The letter x is a consonant
# Hints:  Use the in operator to check if a character is in another string
#         For example, if some_char in 'abc':
# letter = input('Enter a letter from the alphabet: ').lower()
# vowels = 'aeiou'
# consonants = 'bcdfghjklmnpqrstvwxyz'

# if letter in vowels:
#     print(f'The letter {letter} is a vowel')
# elif letter in consonants:
#     print(f'The letter {letter} is a vowel')
# else:
#     print('quit')

# exercise-02 Length of Phrase

# Write the code that:
# 1. Prompts the user to enter a phrase:
#      Please enter a word or phrase:
# 2. Print the following message:
#      - What you entered is xx characters long
# 3. Return to step 1, unless the word 'quit' was entered.

# phrase = ''
# while phrase != 'quit':
#     phrase = input('Please enter a word or phrase: ').lower()
#     print(f'What you entered is {len{phrase}} characters long')

# exercise-03 Calculate Dog Years

# Write the code that:
# 1. Prompts the user to enter a dog's age in human years like this:
#      Input a dog's age in human years:
# 2. Calculates the equivalent dog years, where:
#      - The first two years count as 10 years each
#      - Any remaining years count as 7 years each
# 3. Prints the answer in the following format:
#      The dog's age in dog years is xx
# Hint:  Use the int() function to convert the string returned from input() into an integer

# human_age = int(input("Input a dog's age in human years: "))

# if human_age <= 2:
#     dog_age = human_age * 10
# else:
#     dog_age = (2 * 10 ) + ( human_age - 2) * 7
# print(f"The dog's age in dog years is {dog_age}")


# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a:
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equalateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle
# A = input('Triangle side a: ')
# B = input('Triangle side b: ')
# C = input('Triangle side c: ')

# if A == B == C:
#     print(f'A triangle with sides of {A}, {B} & {C} is a equalateral triangle')
# elif A == B or B == C or C == A:
#     print(f'A triangle with sides of {A}, {B} & {C} is a isosceles triangle')
# else:
#     print(f'A triangle with sides of {A}, {B} & {C} is a scalene triangle')

# exercise-05 Fibonacci sequence for first 50 terms

# Write the code that:
# 1. Calculates and prints the first 50 terms of the fibonacci sequence.
# 2. Print each term and number as follows:
#      term: 0 / number: 0
#      term: 1 / number: 1
#      term: 2 / number: 1
#      term: 3 / number: 2
#      term: 4 / number: 3
#      term: 5 / number: 5
#      etc.
# Hint: The next number is found by adding the two numbers before it
# a = 0
# b = 1
# num = 0 
# for i in range(50):
#     print(i, num)
#     a = b
#     b = num
#     num = a + b

# exercise-06 What's the  Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the season (Jan - Dec):
# 2. Then promptshtt the user to enter the day of the month:
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season>

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
# if input_month in ('Jan', 'Feb', 'Mar'):
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.

month = input('Enter the month of the season (Jan - Dec): ').lower()
day = int(input('Enter the day of the month: '))

if month in ('January', 'February', 'March'):
     season = 'Winter'
elif month in ('April', 'May', 'June'):
    season = 'Spring'
elif month in ('July', 'August', 'September'):
    season = 'Summer'
else:
    season = 'Fall'

if (month == 'March') and (day > 19):
    season = 'Spring'
elif (month == 'June') and (day >20):
    season = 'Summer'
elif (month == 'September') and (day > 21):
    season = 'Fall'
elif (month == 'December') and (day > 20):
    season = 'Winter'
    print(f'{month} {day} is in {season}')