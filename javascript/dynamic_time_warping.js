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

    for (const [x2, elem2] of seq2.entries()) {
        for (const [x1, elem1] of seq1.entries()) {
            let penalty = 0;
            if (x1 === 0 && x2 === 0) {
                continue;
            } else if (x1 === 0) {
                penalty = costMatrix[x2 - 1][0];
            } else if (x2 === 0) {
                penalty = costMatrix[0][x1 - 1];
            } else {
                penalty = Math.min(costMatrix[x2 - 1][x1], costMatrix[x2 - 1][x1 - 1], costMatrix[x2][x1 - 1]);
            }
            costMatrix[x2][x1] = Math.abs(elem1-elem2) + penalty;
        }
    }

    return costMatrix;
}


function getOptimalPath(costMatrix) {
    const optimalPathCoords = [];
    const optimalPathCosts = [];
    let y1 = costMatrix[0].length - 1;
    let y2 = costMatrix.length - 1;
    
    while (true) {
        optimalPathCoords.push([y1, y2])
        optimalPathCosts.push(costMatrix[y2][y1])
        if (y1 === 0 && y2 === 0) {
            break;
        } else if (y1 === 0) {
            --y2;
        } else if (y2 === 0) {
            --y1;
        } else {
            const horizontalCost = costMatrix[y2][y1 - 1];
            const diagonalCost = costMatrix[y2 - 1][y1 - 1];
            const verticalCost = costMatrix[y2 - 1][y1];
            if (horizontalCost < diagonalCost) {
                if (horizontalCost < verticalCost) {
                    --y1;
                } else {
                    --y2;
                }
            } else {
                --y2;
                if (diagonalCost <= verticalCost) {
                    --y1;
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