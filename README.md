# sudoku-web-app
Small Python web app to solve Sudokus using PuLP and Flask

This is a very basic and simple example for a Python web app, that solves a Sudoku, which is entered by the user.
The principle is as follows: 
with the numbers entered for the sudoku via the web interface a linear program is generated, that gets solved in the background using the
standard LP solver provided by the PuLP module (you can also activate your preferred solver like Gurobi etc. if you hold a license).

To run the web app locally, you need to call

```bash
$ python3 app.py
```

Then you can open your browser and go to http://127.0.0.1:5000/sudoku

**Requirements**:
- PuLP
- Flask

For the html rendering bootstrap is used inside the templates.
