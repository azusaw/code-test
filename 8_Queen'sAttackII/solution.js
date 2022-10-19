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
 * Complete the 'queensAttack' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER n
 *  2. INTEGER k
 *  3. INTEGER r_q
 *  4. INTEGER c_q
 *  5. 2D_INTEGER_ARRAY obstacles
 */

function queensAttack(n, k, r_q, c_q, obstacles) {
    let obs_r = obstacles.filter((v) => v[0] == r_q)
    let obs_c = obstacles.filter((v) => v[1] == c_q)
    let obs_d = obstacles.filter((v) => v[0] - v[1] == r_q - c_q || v[0] + v[1] == r_q + c_q)
    let tmp = []
    let cnt = 0

    // row direction
    cnt += n - 1
    if (obs_r.length > 0) {
        tmp = obs_r.filter((v) => v[1] < c_q).sort()
        if (tmp.length > 0) {
            cnt -= tmp[tmp.length - 1][1]
        }
        tmp = obs_r.filter((v) => v[1] > c_q).sort()
        if (tmp.length > 0) {
            cnt -= n - tmp[0][1] + 1
        }
    }
    // col direction
    cnt += n - 1
    if (obs_c.length > 0) {
        tmp = obs_c.filter((v) => v[0] < r_q).sort()
        if (tmp.length > 0) {
            cnt -= tmp[tmp.length - 1][0]
        }
        tmp = obs_c.filter((v) => v[0] > r_q).sort()
        if (tmp.length > 0) {
            cnt -= n - tmp[0][0] + 1
        }
    }
    // diagonal direction
    let m = Math.min(n - Math.max(r_q, c_q), Math.min(r_q, c_q) - 1)
    cnt += n - 1 + m * 2
    if (obs_d.length > 0) {
        tmp = obs_d.filter((v) => v[0] > r_q && v[1] < c_q).sort()
        if (tmp.length > 0) {
            cnt -= Math.min(n - tmp[0][0] + 1, tmp[0][1])
        }
        tmp = obs_d.filter((v) => v[0] > r_q && v[1] > c_q).sort()
        if (tmp.length > 0) {
            cnt -= Math.min(n - tmp[0][0], n - tmp[0][1]) + 1
        }
        tmp = obs_d.filter((v) => v[0] < r_q && v[1] > c_q).sort()
        if (tmp.length > 0) {
            cnt -= Math.min(tmp[tmp.length - 1][0], n - tmp[tmp.length - 1][1] + 1)
        }
        tmp = obs_d.filter((v) => v[0] < r_q && v[1] < c_q).sort()
        if (tmp.length > 0) {
            cnt -= Math.min(tmp[tmp.length - 1][0], tmp[tmp.length - 1][1]) 
        }   
    }
    return cnt
}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const firstMultipleInput = readLine().replace(/\s+$/g, '').split(' ');

    const n = parseInt(firstMultipleInput[0], 10);

    const k = parseInt(firstMultipleInput[1], 10);

    const secondMultipleInput = readLine().replace(/\s+$/g, '').split(' ');

    const r_q = parseInt(secondMultipleInput[0], 10);

    const c_q = parseInt(secondMultipleInput[1], 10);

    let obstacles = Array(k);

    for (let i = 0; i < k; i++) {
        obstacles[i] = readLine().replace(/\s+$/g, '').split(' ').map(obstaclesTemp => parseInt(obstaclesTemp, 10));
    }

    const result = queensAttack(n, k, r_q, c_q, obstacles);

    ws.write(result + '\n');

    ws.end();
}
