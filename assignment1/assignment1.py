# Write your code here.

#Task1:Hello
# Write a hello function that takes no arguments and returns Hello!

def hello():
    return "Hello!"

print("Hello function: ",hello()) 

# Task 2: Greet with a Formatted String
# Write a greet function.  It takes one argument, a name, and returns Hello, Name!.

def greet(name):
    return f"Hello, {name}!"
    
print("Greet function: ",greet("Fara"))


# Task 3: Calculator
# Write a calc function. It takes three arguments. The default value for the third argument is "multiply".
# The first two arguments are values that are to be combined using the operation requested by the third argument,
# a string that is one of the following add, subtract, multiply, divide, modulo, int_divide (for integer division) 
# and power. The function returns the result.
# Error handling: When the function is called, it could ask you to divide by 0. That will throw an exception: 
# Which one? You can find out by triggering the exception in your program or in the Python Interactive Shell. 
# Wrap the code within the calc function in a try block, and put in an except statement for this exception. If the exception occurs, return the string "You can't divide by 0!".
# More error handling: When the function is called, the parameters that are passed might not work for the operation. 
# For example, you can't multiply two strings. Find out which exception occurs, catch it, and return the string
# "You can't multiply those values!".

def calc(number1, number2, operation="multiply"):
    
    try:
        match operation:
            case "add":
                return number1 + number2
            case "subtract":
                return number1 - number2
            case "multiply":
                return number1 * number2
            case "divide":
                return number1 / number2
            case "modulo":
                return number1 % number2
            case "int_divide":
                return number1 // number2
            case "power":
                return number1 ** number2
                    
    except ZeroDivisionError:
        return "You can't divide by 0!"
        
    except TypeError:
        return f"You can't {operation} those values!"
                    
print("Calculator function :", calc(4,5,"add"))


# Task 4: Data Type Conversion
# Create a function called data_type_conversion. It takes two parameters, the value and the name of the data type requested,
# one of float, str, or int. Return the converted value.
# Error handling: The function might be called with a bad parameter. 
# For example, the caller might try to convert the string "nonsense" to a float. 
# Catch the error that occurs in this case. If this error occurs, return the string You can't convert {value} into a {type}., 
# except you use the value and data type that are passed as parameters -- so again you use a formatted string.

def data_type_conversion(value, data_type):
    
        try:            
            match data_type:
                case "float":
                    return float(value)
                case "str":
                    return str(value)
                case "int":
                    return int(value)
                        
        except ValueError:
            return f"You can't convert {value} into a {data_type}."
                    
print("Data type conversion: ", data_type_conversion(5,"float"))


# Task 5: grade
# Create a grade function. It should collect an arbitrary number of parameters, 
# compute the average, and return the grade. based on the following scale:
# A: 90 and above
# B: 80-89
# C: 70-79
# D: 60-69
# F: Below 60

def grade(*args):
    
    try:
        
        avg = sum(args) / len(args)
        
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >=70:
            return "C"
        elif avg >=60:
            return "D"
        else:
            return"F"
        
    except TypeError:
        return "Invalid data was provided."
                    
print("Grade function: ",grade(100,89,5,100,5,80))
        
                
        
# Task 6
# Task 6: Use a For Loop with a Range
# Create a function called repeat. It takes two parameters, a string and a count, 
# and returns a new string that is the old one repeated count times.
# You can get the test to pass by just returning string * count. 
# That would produce the correct return value. But, for this task, do it using a for loop and a range.


def repeat(string, count):
    string_repeated = string
    for _ in range(1, count):
        string_repeated += string
    return string_repeated

print("repeat : ",repeat("fara,",5))


# Task 7: Student Scores, Using **kwargs
# Create a function called student_scores. It takes one positional parameter and an arbitrary number
# of keyword parameters. The positional parameter is either "best" or "mean". 
# If it is "best", the name of the student with the highest score is returned. 
# If it is "mean", the average score is returned.
# The arbitrary list of keyword arguments uses the names of students as the keywords 
# and their test score as the value for each.

def student_scores(positional,**kwargs):
    if positional =="best":
        highest_score = 0
        for key, value in kwargs.items():
            if value > highest_score:
                highest_score = value
                name = key
        return name
            
    else:
        return sum(kwargs.values()) / len(kwargs.values())
    

print("Student score  ", student_scores("best",Fara=78,Tsiry=79,Anna=80))


# Task 8:Task 8: Titleize, with String and List Operations
# Create a function called titleize. It accepts one parameter, a string. The function returns a new string, 
# where the parameter string is capitalized as if it were a book title.
# The rules for title capitalization are: (1) The first word is always capitalized. (2) 
# The last word is always capitalized. (3) All the other words are capitalized, except little words. For the purposes of this task, the little words are "a", "on", "an", "the", "of", "and", "is", and "in".
# The following string methods may be helpful: split(), join(), and capitalize(). Look 'em up.
# The split() method returns a list. You might store this in the words variable. words[-1] gives the last element in the list.
# The in comparison operator: You have seen in used in loops. But it can also be used for comparisons,
# for example to check to see if a substring occurs in a string, or a value occurs in a list.
# A new trick: As you loop through the words in the words list, it is helpful to have the index of the word for each iteration.
# You can access that index using the enumerate() function:
# for i, word in enumerate(words):

def titleize(title):
    words = title.split()
    words[0] = words[0].capitalize()
    words[-1] = words[-1].capitalize()
    little_word = ["a", "on", "an", "the", "of", "and", "is", "in"]
    for i, word in enumerate(words):
        if word not in little_word:
            words[i] = word.capitalize()
    return " ".join(words)
                
print("Titleize a string : ",titleize("It is good to learn a new programming language"))



# Task 9: Hangman, with more String Operations
# Create a function hangman. It takes two parameters, both strings, the secret and the guess.
# The secret is some word that the caller doesn't know. So the caller guesses various letters,
# which are the ones in the guess string.
# A string is returned. Each letter in the returned string corresponds to a letter in the secret, 
# except any letters that are not in the guess string are replaced with an underscore

def hangman(secret, guess):
    return_string = ""
    for letter in secret:
        if letter in guess:
            return_string += letter
        else:
            return_string += "_"
    return return_string

print("Hangman ", hangman("alphabet","ab"))


# Task 10 Pig Latin, Another String Manipulation Exercise
# Task 10: Create a function called pig_latin. It takes an English string or sentence and converts it to Pig Latin, 
# returning the result. We will assume that there is no punctuation and that everything is lower case.
# Pig Latin is a kid's trick language. Each word is modified according to the following rules. 
# (1) If the string starts with a vowel (aeiou), "ay" is tacked onto the end. 
# (2) If the string starts with one or several consonants, they are moved to the end and "ay" is tacked on after them. 
# (3) "qu" is a special case, as both of them get moved to the end of the word, as if they were one consonant letter.

def pig_latin(sentence):
    sentence = sentence.split()
    new_sentence = []
    vowels = ["a", "e", "i", "o", "u"]

    for word in sentence:

        if word[0] in vowels:
            new_word = word+"ay"
            new_sentence.append(new_word)
            
        else:
            index = 0
            while index < len(word) and word[index] not in vowels:
                if word[index:index+2] == "qu":  
                    index += 2
                    break
                index += 1
            new_word = word[index:] + word[:index] + "ay"
            new_sentence.append(new_word)

    new_sentence = " ".join(new_sentence)
    return new_sentence
     
print("pig_latin: ", pig_latin("it is forbidden to spit on quiet square cats"))
