function makeMatrix(numRaws, numCols, initialValue = 0) {
    let matrix = new Array(numRaws);
    for (let i = 0; i < numRaws; ++i) {
        matrix[i] = new Array(numCols)
        for (let j = 0; j < numCols; ++j) {
            matrix[i][j] = initialValue;
        }
    }
    return matrix;
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
    const optimalPathCosts = [];
    const optimalPathPairs = [];
    let x = costMatrix[0].length - 1;
    let y = costMatrix.length - 1;
    
    while (true) {
        optimalPathPairs.push([x, y])
        optimalPathCosts.push(costMatrix[y][x])
        if (x === 0 && y === 0) {
            break;
        } else if (x === 0) {
            --y;
        } else if (y === 0) {
            --x;
        } else {
            const leftsideCost = costMatrix[y][x - 1];
            const diagonalCost = costMatrix[y - 1][x - 1];
            const bottomCost = costMatrix[y - 1][x];
            if (leftsideCost < diagonalCost) {
                if (leftsideCost < bottomCost) {
                    --x;
                } else {
                    --y;
                }
            } else {
                --y;
                if (diagonalCost <= bottomCost) {
                    --x;
                }
            }
        }
    }

    return [optimalPathPairs.reverse(), optimalPathCosts.reverse()];
}


function run(seq1, seq2) {
    const costMatrix = getCostMatrix(seq1, seq2);
    const [optimalPathPairs, optimalPathCosts] = getOptimalPath(costMatrix);
    return [optimalPathPairs, optimalPathCosts, costMatrix];
}

function displayMatrix(matrix) {
    matrix.reverse();
    matrix.forEach(raw => {
        raw.forEach(element => process.stdout.write(`[${element}]`));
        console.log();
    });
    matrix.reverse();
}


function main() {
    let seq1 = [1, 7, 3, 4, 1, 10, 5, 4, 7, 4];
    let seq2 = [1, 4, 5, 10, 9, 3, 2, 6, 8, 4];

    const [optimalPathPairs, optimalPathCosts, costMatrix] = run(seq1, seq2);
    // let costMatrix = getCostMatrix(seq1, seq2);
    displayMatrix(costMatrix);
    console.log("seq1 (x-axis):", seq1);
    console.log("seq2 (y-axis):", seq2);
    
    // let [optimalPathPairs, optimalPathCosts] = getOptimalPath(costMatrix);
    
    console.log("optimalPathPairs [(x, y)]:", optimalPathPairs);
    console.log("optimalPathCosts:", optimalPathCosts);
}