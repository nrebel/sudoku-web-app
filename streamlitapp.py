import streamlit as st
import numpy as np
from sudoku import solve_sudoku

def main():
    st.title("Sudoku Solver with Streamlit")
    st.write("Enter the Sudoku puzzle below and click Solve.")
    
    # Initialize a 9x9 grid for user input
    grid = np.zeros((9, 9), dtype=int)
    
    # Use a grid layout for easier input
    for i in range(9):
        cols = st.columns(9)
        for j in range(9):
            value = cols[j].text_input(f"  ", value="0", key=f"cell_{i}{j}")
            if value.isdigit() and int(value) >= 0 and int(value) <= 9:
                grid[i, j] = int(value)
            else:
                grid[i, j] = 0
    
    if st.button("Solve Sudoku"):
        # Convert grid to the format required by solve_sudoku
        input_form = {f"cell_{i+1}{j+1}": int(grid[i, j]) for i in range(9) for j in range(9)}
        
        solution = solve_sudoku(input_form)
        
        if solution and solution[0][0] != '':
            st.success("Solved Sudoku:")
            solved_grid = [[solution[i][j] for j in range(9)] for i in range(9)]
            st.table(solved_grid)
        else:
            st.error("No solution found!")

if __name__ == "__main__":
    main()
