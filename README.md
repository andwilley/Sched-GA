# Military Flight Scheduling EA
## Installation:
1. Ensure Python 3.6 is installed on the system.
2. In the console:
```
python3.6 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Run the Program
From the top project directory, in the console:
```
python run.py
```

## Change the way the program runs:
- To change the schedule used in the program, in `run.py`, change the number in the event file name to another number between 1 and 5.
```diff
-from app.state.events1 import events
+from app.state.events3 import events
```
- To change any of the parameters, just edit the values in `./app/ga/parameters.py`. Values chosen for the GA are in comments beside the values.
- To see the hamming distance at the conclusion of the run, add the following parameter to the call to `main()` in `run.py` (This is time consuming).
```python
print_hamming=True
```
- To view the plotted results, navigate to `./tmp`. Images of the figures will be saved there.

## Directory Structure
- App
    - analysis - *diversity caluclation and plotting*
    - constants - *app-wide constants defined*
    - ga - *fitness calculations, genetic operators, parameters*
    - models - *definition of model classes, incl Constaint, Individual and Population*
    - state - *schedules, pilots and events*
    - test - *unit tests*
    - tmp - *fitness plots saved here*