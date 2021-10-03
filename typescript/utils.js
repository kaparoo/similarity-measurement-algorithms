function makeMatrix(numRows, numCols, initialValue = 0) {
    let matrix = new Array(numRows);
    for (let i = 0; i < numRows; ++i) {
        matrix[i] = new Array(numCols)
        for (let j = 0; j < numCols; ++j) {
            matrix[i][j] = initialValue;
        }
    }
    return matrix;
}


function displayMatrix(matrix) {
    matrix.reverse();
    matrix.forEach(row => {
        row.forEach(element => process.stdout.write(`[${element}]`));
        console.log();
    });
    matrix.reverse();
}