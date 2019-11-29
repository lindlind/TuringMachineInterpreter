# TuringMachineInterpreter

### How to use

1. Constuct a table of rules for Turing machine. You can do it in Microsoft Excel or LibreOffice Calc and save as .csv file.
2. Tune a config file according to the format of saved table.
3. Construct an initial tape for Turing machine and save it in input file. It should be empty if initial tape is empty.
4. Parse Turing machine from table by running `parseMT.py`. Give this program the name of file with table.
5. Run Turing machine by running `runMT.py`. Give this program the name if input file with initial tape.
6. To see each step of turing machine, set showStrip parameper in config file as True.

### Table format

- In first cell of each line except first is a name of the state.
- In first cell of each column except first is a symbol at the pointer. 
- Each cell is a state, characterized by the name of the state, symbol at the pointer and position of a pointer. 
- Each cell contains 3 parameters:
	- First is a symbol that replace current symbol at the pointer.
	- Second is a name of the next state.
	- Third is a direction of movement of the pointer.

### Config parameters

| Parameter | Description | 
| --------- | ----------- |
| cell delimeter | How cells in table are separated |
| inner delimeter | How parameters in cell are separated |
| go left | Designation in table of going pointer to the left |
| go right | Designation in table of going pointer to the right |
| stay here | Designation in table of staying pointer in place |
| start | Name of starting state. If value is 'first', starting state will be the first state in table. |
| accept | Name of accepting state. |
| reject | Name of rejecting state. |
| blank | Which symbol was chosen as a default symbol on the tape. |
| same | Designation in table of not-changing of state and not-changing of symbol on tape. |
| showStrip | Can be 'True' or 'False'. If 'True', print the tape and the pointer on it while running. |

### Warnings

- Values in config file cannot contain a quotation mark ans space symbols.
- Names of states and symbols cannot contain a quotation mark, cell delimeter, inner delimeter and space symbols.
- Tape cannot contain space symbols. All space symbols in input file will be skipped.
- Do not reorder parameters in config file.
