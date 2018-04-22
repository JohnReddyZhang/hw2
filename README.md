# Homework 2 
For Applied software Engineering

### Source Code:
I decided to use the box_office I wrote for hw1 and start from there.

### Initial Commit:
The initial commit was marked *red* for committing only initial environment files used by PyCharm  
(I am using every chance to get myself familiarized to IDEs) 
The initial commit of `event_class.py` is different and later than other commits, 
but it is several versions later than its actual creation. I forget to add it to repo when I just created it.

### Test Cases:
First run of test case will success, but second or later run will fail **some** tests 
if not deleted pkl files in "data" folder.

This is due to auto save on each operation, and TestClass LoadFiles is using the same pkl as Report, 
so data will be cumulative.
 