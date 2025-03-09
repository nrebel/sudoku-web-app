from pulp import *

def solve_sudoku(input_form):

    # A list for indexing
    indices_seq = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    values = indices_seq
    rows = indices_seq
    columns = indices_seq

    squares_list = []
    for i in range(3):
        for j in range(3):
            squares_list += [[(rows[3*i+k],columns[3*j+l]) for k in range(3) for l in range(3)]]

    model = LpProblem("Sudoku Problem",LpMinimize)

    choices = LpVariable.dicts("Choice",(values,rows,columns),0,1,LpInteger)

    # The constraints are created here

    for r in rows:
        for c in columns:
            model += lpSum([choices[v][r][c] for v in values]) == 1, ""

    for v in values:
        for r in rows:
            model += lpSum([choices[v][r][c] for c in columns]) == 1,""

        for c in columns:
            model += lpSum([choices[v][r][c] for r in rows]) == 1,""

        for b in squares_list:
            model += lpSum([choices[v][r][c] for (r,c) in b]) == 1,""

    for i in rows:
        for j in columns:
            cell = "cell_" + i + j
            if input_form[cell] != "":
                val = input_form[cell]
                model += choices[str(val)][i][j] == 1,"" # for flask version str(...) might be removed

    # just for analysis, we write out the model into an .lp-file
    model.writeLP("sudoku_model.lp")

    # we are going to write the result to sudokuout.txt and into a html-string (res) for the web app
    sudokuout = open('sudokuout.txt','w')

    # note: we terminate after the first feasible solution is found!
    while True:
        model.solve()
        res = ""
        res_array = [["" for i in range(9)] for j in range(9)]
        # The status of the solution is printed to the screen
        print("Status:", LpStatus[model.status])
        if LpStatus[model.status] == "Optimal":
            for r in rows:
                if r == "1" or r == "4" or r == "7":
                    sudokuout.write("+-------+-------+-------+\n")
                    res += "<b>+-------+-------+-------+</b><br>"
                for c in columns:
                    for v in values:
                        if value(choices[v][r][c]) == 1:
                            res_array[int(r)-1][int(c)-1] = v
                            if c == "1" or c == "4" or c =="7":
                                sudokuout.write("<b>| </b>")
                                res += "<b>| </b>"
                            sudokuout.write(v + " ")
                            res += v + " "
                            if c == "9":
                                sudokuout.write("|\n")
                                res += "<b>|</b><br>"
            sudokuout.write("+-------+-------+-------+\n\n")
            res += "<b>+-------+-------+-------+</b><br><br>"
            # The constraint is added that the same solution cannot be returned again
            model += lpSum([choices[v][r][c] for v in values
                                            for r in rows
                                            for c in columns
                                            if value(choices[v][r][c])==1]) <= 80

            break
        else:
            break
    sudokuout.close()
    print(res)
    return res_array
