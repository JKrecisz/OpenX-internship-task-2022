# Task 2
### What the script does
The script will print out the soonest date in the future when at least desired amount of people are available for given amount of time.
The script works, has been tested with different values.

### How to run

Before everything, check if you have these libraries:
- re
- glob
- datetime
- argparse

If not, just download them like:

```text
pip install regex
    # or
pip3 install regex
```

Then, download the entire repository (If you did it in the first task, skip this step):
```text
git clone https://github.com/JKrecisz/OpenX-internship-task-2022.git
```
Next:
```text
cd OpenX-internship-task-2022
# then
cd task2
```
Now, the syntax is simple, we have to give arguments that are required:

    --duration-in-minutes   # Availability time of people (minutes)
    --minimum-people        # Minimum number of people
    --calendars             # Name of the date folder

Calling the script will look like for example:
```text
python3 find-available-slot.py --calendars /in --duration-in-minutes 30 --minimum-people 2
```