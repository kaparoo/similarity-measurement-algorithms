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


function getCostMatrix(seq1, seq2) {
    let costMatrix = makeMatrix(seq2.length, seq1.length, 0);

    for (const [y, elem2] of seq2.entries()) {
        for (const [x, elem1] of seq1.entries()) {
            let penalty = 0;
            if (x === 0 && y === 0) {
                continue;
            } else if (x === 0) {
                penalty = costMatrix[y - 1][0];
            } else if (y === 0) {
                penalty = costMatrix[0][x - 1];
            } else {
                penalty = Math.min(costMatrix[y - 1][x], costMatrix[y - 1][x - 1], costMatrix[y][x - 1]);
            }
            costMatrix[y][x] = Math.abs(elem1-elem2) + penalty;
        }
    }

    return costMatrix;
}


function getOptimalPath(costMatrix) {
    const optimalPathCoords = [];
    const optimalPathCosts = [];
    let x = costMatrix[0].length - 1;
    let y = costMatrix.length - 1;
    
    while (true) {
        optimalPathCoords.push([x, y])
        optimalPathCosts.push(costMatrix[y][x])
        if (x === 0 && y === 0) {
            break;
        } else if (x === 0) {
            --y;
        } else if (y === 0) {
            --x;
        } else {
            const horizontalCost = costMatrix[y][x - 1];
            const diagonalCost = costMatrix[y - 1][x - 1];
            const verticalCost = costMatrix[y - 1][x];
            if (horizontalCost < diagonalCost) {
                if (horizontalCost < verticalCost) {
                    --x;
                } else {
                    --y;
                }
            } else {
                --y;
                if (diagonalCost <= verticalCost) {
                    --x;
                }
            }
        }
    }

    return [optimalPathCoords.reverse(), optimalPathCosts.reverse()];
}


function run(seq1, seq2) {
    const costMatrix = getCostMatrix(seq1, seq2);
    const [optimalPathCoords, optimalPathCosts] = getOptimalPath(costMatrix);
    return [optimalPathCoords, optimalPathCosts, costMatrix];
}


function main() {
    let seq1 = [1, 7, 3, 4, 1, 10, 5, 4, 7, 4];
    let seq2 = [1, 4, 5, 10, 9, 3, 2, 6, 8, 4];

    const [optimalPathCoords, optimalPathCosts, costMatrix] = run(seq1, seq2);
    displayMatrix(costMatrix);
    console.log("seq1 (x-axis):", seq1);
    console.log("seq2 (y-axis):", seq2);
    console.log("optimalPathCoords:", optimalPathCoords);
    console.log("optimalPathCosts:", optimalPathCosts);
}