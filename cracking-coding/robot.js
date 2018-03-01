/*
Robot in a Grid:
Imagine a robot sitting on the upper left corner of grid with r rows and c columns.

The robot can only move in two directions, right and down, but certain cells are "off limits" such that the robot cannot step on them.

Design an algorithm to find a path for the robot from the top left to the bottom right.
*/

// NOT x,y
// [ROW, COL] [0, 1]
// rows = vertical length
// cols = horizontal length

function createGrid(rows, cols, blocked = []){
    let grid = Array(rows).fill().map(() => Array(cols).fill(true));
    grid[rows-1][cols-1] = "END";

    // mark blocked cells
    if (blocked.length != 0){
        for (let block of blocked){
            if (block[0] >= rows || block[1] >= cols){
                console.log("Block out of grid range:", block);
                continue;
            }
            grid[block[0]][block[1]] = undefined;
        }
    }
    return grid;
}

function findPath(grid, startCell = [0,0]){
    var row = startCell[0];
    var col = startCell[1];
    var start = grid[row][col];
    var directions = [[row+1, col], [row, col+1]]; // down and right

    console.log(row, col);

    for (let i = 0; i < directions.length; i++){
        if (nextCell(grid, directions[i]) == 'END'){
            console.log("Path");
            return console.log(grid);
        }

        if (nextCell(grid, directions[i]) == start){
            findPath(grid, directions[i]);
        }
    }

    // console.log("Lose", row, col);

    return grid;
}

function nextCell(grid, cell){
    let row = cell[0];
    let col = cell[1];
    if (grid[row] != undefined && grid[row][col] != undefined){
        return grid[row][col];
    }
    return false;
}

let blocked = [
    [1,1], [2,3]
    // [0,1], [2,0]
];
let grid = createGrid(3, 5, blocked);
let startCell = [0,0];
findPath(grid, startCell);