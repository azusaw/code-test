// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(N) {
    if (N < 3) {
        return 0
    }
    const regexp = /10+1/g
    let tmp = 2
    /* Odd should add '1' at last */
    let i =  N % 2 === 0 ? 1 : 0
    while (tmp < N) {
        tmp = tmp * 2
        i++
    }
    const binaryGapList =
        makeBinaryStrRecursion(N - tmp / 2, i - 1,'1').match(regexp)
    if (binaryGapList == null) {
        return 0
    } else if (typeof binaryGapList === 'string') {
        return binaryGapList.length - 2
    }
    return binaryGapList.sort((a, b) => a < b ? 1 : -1)[0].length - 2
}

function makeBinaryStrRecursion(num, nextDigit, binaryStr) {
    if (num === 1) {
        return binaryStr + '0'.repeat(nextDigit) + '1'
    } else if (num === 0) {
        return binaryStr + '0'.repeat(nextDigit)
    }
    let tmp = Math.pow(2, nextDigit)
    if (num >= tmp) {
        nextDigit -= 1
    } else {
        while (tmp > num) {
            tmp = tmp / 2
            binaryStr += '0'
            nextDigit -= 1
        }
    }
    return makeBinaryStrRecursion(num - tmp, nextDigit, binaryStr + '1')
}
