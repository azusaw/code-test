'use strict';
/* azusaw */

const fs = require('fs');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', function(inputStdin) {
    inputString += inputStdin;
});

process.stdin.on('end', function() {
    inputString = inputString.split('\n');

    main();
});

function readLine() {
    return inputString[currentLine++];
}

/*
 * Complete the 'nonDivisibleSubset' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER k
 *  2. INTEGER_ARRAY s
 */

function nonDivisibleSubset(k, s) {
    s = s.map((n) => {
        let cnt = 0
        for (let i = 0; i < s.length; i++) {
            if (n != s[i] && (n + s[i]) % k == 0) {
                cnt += 1
            }
        }
        return [n, cnt]    
    })
    s.sort((a, b) => {
        if (a[1] > b[1]) return 1
        if (a[1] < b[1]) return -1
        return 0
    })
    let sf = []
    for (let n1 of s) {
        let f = 0
        for (let n2 of sf) {
            console.log(n1, n2)
            if ((n1[0] + n2) % k == 0) {
                f = 1
                break
            }
        }
        f == 0 && sf.push(n1[0])
    }
    return sf.length
}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const firstMultipleInput = readLine().replace(/\s+$/g, '').split(' ');

    const n = parseInt(firstMultipleInput[0], 10);

    const k = parseInt(firstMultipleInput[1], 10);

    const s = readLine().replace(/\s+$/g, '').split(' ').map(sTemp => parseInt(sTemp, 10));

    const result = nonDivisibleSubset(k, s);

    ws.write(result + '\n');

    ws.end();
}
