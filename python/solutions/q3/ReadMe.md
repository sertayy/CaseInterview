# Ideal Clock
## Notes
- This project developed in a macOS 11.6 machine using Python 3.8 and tested in Ubuntu 20.04.4 LTS version.
- All the libraries used in this project are python standard libraries.

###  Execution
``` 
python3 soln.py
```
Sample Outputs:
```
Please enter the time: 7:53
minute-hand is 81.5 degrees clockwise from hour-hand
```
```
Please enter the time: 6:00
hour-hand is 180.0 degrees clockwise from minute-hand
```
```
Please enter the time: 12:00
minute-hand is 0.0 degrees clockwise from hour-hand
```
```
Please enter the time: 4:12
hour-hand is 54.0 degrees clockwise from minute-hand
```
``` 
Please enter the time: 14:00
ERROR:root:The time is not valid. Use 12-hour format!
```
``` 
Please enter the time: 2:61
ERROR:root:The time is not valid. Minute range is not correct!
```
```
Please enter the time: 2.15 
ERROR:root:Invalid time format! Use ":" for the time splitter.
```

## Bonus Part
- You can use create_csv.py script to create a sample input csv file.
- "create_csv.py" scripts creates "time.csv" file in the same directory.
- The input file path should be given as an argument.
- The input csv file should consist of only one column which has the time values.
- The results can be visible in "results.csv" file, after the execution of the "bonus.py" script.
- The output csv file consist of two columns(angle and clockwise). 
- Angle column represents the angle in between the hands. 
- Clockwise true means, minute-hand is X degree clockwise from hour-hand. Counter-clockwise on false.
- If the format of a value in the input file is not correct, this value is skipped and an information log is printed on 
the console as given in the sample output.

###  Execution
``` 
python3 bonus.py <input file path>
```
Ex:
``` 
python3 bonus.py time.csv
```
Sample Output:
```
INFO:root:The clock in the 9. line of the csv file is skipped due to an error.
ERROR:root:Invalid time format! Use ":" for the time splitter.
INFO:root:The clock in the 12. line of the csv file is skipped due to an error.
ERROR:root:The time is not valid. Use 12-hour format!
INFO:root:The clock in the 14. line of the csv file is skipped due to an error.
ERROR:root:The time is not valid. Minute range is not correct!
```
For creating a sample input file called "time.csv":
```
python3 create_csv.py 
```

The sample files:
- This is just a representation. These two below are not correlated to each other.
<table>
<tr><th> Input </th><th> Output </th></tr>
<tr><td>

| time |
|------|
| ...  |
| 1.7  | 
| 1:9  | 
| 0:10 | 
| 1:65 |
| ...  |

</td><td>

| angle | clockwise |
|-------|-----------|
| ...   | ...       |
| 8.0   | False     |
| 2.5   | False     |
| 3.0   | True      |
| 14.0  | True      |
| ...   | ...       |

</td></tr> </table>
