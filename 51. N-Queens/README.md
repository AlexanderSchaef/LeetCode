# 51. N-Queens
## Language: Python

## First thoughts:
### About the board
- Board is dynamic of size n x n, and so will need to be initialized.
- Board is stored in an array of strings
- "Q" is a queen, "." is an empty space
- There are no other pieces on the board that are not queens, the board will always be initialized empty.
### About the function
- Returns an array of all possible **Unique** queen placement boards

## First idea:
Place a queen in a start position, replace other characters with x's, and place a queen in the next available position.
