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