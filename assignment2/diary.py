# Create a program called diary.py. Add code to do the following:

# Open a file called diary.txt for appending.
# In a loop, prompt the user for a line of input. The first prompt should say,
# "What happened today? ". All subsequent prompts should say "What else? "
# As each line is received, write it to diary.txt, with a newline (\n) at the end.
# When the special line "done for now" is received, write that to diary.txt. 
# Then close the file and exit the program (you just exit the loop).
# Wrap all of this in a try block. If an exception occurs,
# catch the exception and print out "An exception occurred." followed by the name of the exception itself. 
# Now, normally, you catch specific types of exceptions, and handle each according to program logic. 
# In this case, you can catch any non-fatal exceptions via an except for Exception, 
# and then display the information from the exception and exit the program. 
# The traceback module provides a way to include function traceback information in your error message, 
# which will make it easier to find the error. You can use the following code to handle exceptions using the traceback module.
# Open the file using a with statement (inside the try block), and rely on that statement to handle the file close.
# The input statement should be inside the loop inside the with block.
import traceback

def diary():
    
    try:
        
        with open("diary.txt", "a") as file:
            prompt = "What happened today?"
            while True:
                try:
                    entry = input(prompt)
                except EOFError:
                    print("\n EOF detected")
                    break
                if entry.lower() == "done for now":
                    file.write("done for now\n")
                    break
                    
                file.write(entry + "\n")
                prompt = "What else? "
                
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
        
diary()
                      
        
