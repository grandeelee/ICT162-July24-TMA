# Instructions
1. Please keep the folder structure as it is.
```
myWork
├── data.csv
├── q1.py
├── q2.py
├── q3.py
├── q4.py
└── main.py
```
2. Please do not use any external libraries for this task.
3. Please include comments to explain your code.
4. Within each file, there are some test cases for you to test your code. 

## Clone the folder in Vocareum
1. navigate to TMASubmission folder in the terminal
```bash
labsuser@vscode:~$ cd TMASubmission
```
2. Run the following command to clone the folder in Vocareum
```bash
labsuser@vscode:~/TMASubmission$ git clone 
```
### For Question 1
- Not required to validate the passport number, such as how many characters it should have, or what characters it should contain.
```python
"E2000444N", "EC4744643"
```
- A valid passport number will be provided as input.
- **However, you may consider to handle the case where the passport number is not provided.**
- Seperate the different values using a tab in the string representation. 
```python
"Passport: K4096807E\tName: Wong Yong Heng\tAge: 33\tContact: 88120023"
"Tour Code: KMBK08\tName: Mukbang Korea (8D/6N)\tBase Cost: $1,699.36"
```
- It is not mission critical to keep this format but certainly makes it easier to evaluate programmaically.
- It is more important to keep the output format of the cost as a float with 2 decimal places, and comma separated for thousands.
```python
cost = 1699
print(f"${cost:.2f}")
print(f"${cost:,}")
```
- output
```bash
$1699.00
$1,699
```
- for more information on f-strings, please refer to the [official documentation](https://docs.python.org/3/tutorial/inputoutput.html) or [this tutorial](https://www.w3schools.com/python/ref_string_format.asp)

### For Question 2
- To find the difference in days between two datetime objects, you can use
```python
from datetime import datetime
x = datetime(2018, 6, 1)
y = datetime(2018, 5, 1)
print((x - y).days)
```
- This is a very good reference for the [datetime module](https://www.w3schools.com/python/python_datetime.asp)
- Please note that the date is in the format of "3-Apr-2024 10:05"
- Test cases for Question 2 are updated

### For Question 3
- contains `Booking, IndividualBooking, GroupBooking, BookingException`
### For Question 4
- contains `TourAgency`
### For main.py
- contains the main function to display the menu
- please include an `init` function to read the data from the csv file and initialize the TourAgency object
```python
def main():
    ta = TourAgency()    
    init(ta) # read the data from the csv file and initialize the TourAgency object
    while True:
        print("<<<< Main Menu >>>>")
    ...
```
- there is no test case for main.py
- I will run the `main.py` manually to test the code
## Unittest Cases
- Uploaded test cases for q1 and q2
- Only works in the folder structure and naming convention as specified in the instructions
- Tested on Vocareum and Ubuntu
- To run the test cases, navigate to the folder containing the test cases and run the following command
```bash
labsuser@vscode:~/TMASubmission$ chmod +x q1_test
labsuser@vscode:~/TMASubmission$ ./q1_test
```
- The first line of the command is to make the file executable
- The second line of the command is to run the file
- The output will be displayed in the terminal
- Change the file name to q2_test to run the test cases for q2
### Updates for unittest cases
- Updated the test cases for and q2 (previously q2_test has a bug in print `__str__` method)
- Updated the test cases for q3 (deleted one ambiguous test case) 
- Updated the test cases for q4 (separation of listed objects with either single newline or double newlines is accepted)

