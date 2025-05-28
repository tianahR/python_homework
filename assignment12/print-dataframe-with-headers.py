# Task 5 : Extending a class

import pandas as pd
class DFPlus(pd.DataFrame):
    @property
    def _constructor(self):
        return DFPlus

    @classmethod
    def from_csv(cls, filepath, **kwargs):
        df = pd.read_csv(filepath, **kwargs)
        return cls(df)
    
    # Within the DFPlus class, declare a function called print_with_headers(). 
    # It only takes one argument, self. When you print a big DataFrame, you can't see the column headers because they scroll up.
    # This function will provide a way to print the DataFrame giving column headers every 10 lines. The function will print the whole
    # DataFrame in a loop, printing 10 rows at a time.
    # Well, how to do this? You need to know the length of the DataFrame. 
    # That's easy: len(self). Now, how do you get a given 10 rows?
    # That's easy too. You have access to super().iloc so you can specify the ten line slice you want. 
    # And then you just print what you get back, looping until you get to the bottom.
    
    def print_with_headers(self):
        x = len(self)
        pos=0
        while pos < x:
            print(super().iloc[pos:pos+10])
            pos += 10
            if pos < x:
                input("\nPress Enter to continue...\n")  # Wait for user
            
# Task 5:3 Using the from_csv() class method, create a DFPlus instance from "../csv/products.csv".
dfp = DFPlus.from_csv("../csv/products.csv")

# Task 5:4 Use the print_with_headers() method of your DFPlus instance to print the DataFrame.
dfp.print_with_headers()