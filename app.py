from flask import *
from sudoku import solve_sudoku

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
@app.route('/sudoku', methods=["GET", "POST"])
def sudoku():
  # A list for indexing
  indices_seq = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

  values = indices_seq
  rows = indices_seq
  columns = indices_seq  
  
  fieldString = ""

  for i in rows:
    fieldString += "<tr>\n"
    for j in columns:
        fieldString += "<td><input type=\"number\" name=\"cell_" + i + j + "\"></td>\n"
    fieldString += "\n</tr>"

  return render_template('sudoku.html', fields=fieldString)

@app.route('/testvals', methods=["GET", "POST"])
def testvals():
  indices_seq = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

  values = indices_seq
  rows = indices_seq
  columns = indices_seq  
  result = ""
  liste = ""

  if request.method == 'POST':
    result = request.form
  for i in rows:
    for j in columns:
      cell = "cell_" + i + j
      liste += result[cell] + " " + "\n"
  erg = solve_sudoku(result)
  print(erg)

  fieldString = ""

  for i in range(9):
    fieldString += "<tr>\n"
    for j in range(9):
        fieldString += "<td><input type=\"number\" value=\"" + erg[i][j] + " \" name=\"cell_" + str(i) + str(j) + "\">" + erg[i][j] + "</td>\n"
    fieldString += "\n</tr>"
    print (fieldString)
  return render_template('sudoku.html', fields=fieldString)

if __name__ == "__main__":
	app.run() 
