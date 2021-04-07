// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(N) {
    if (N < 3) {
        return 0
    }
    const regexp = /10+1/g
    var binaryStr = N.toString(2);
    const binaryGapList = binaryStr.match(regexp)
    if (binaryGapList == null) {
        return 0
    } else if (typeof binaryGapList === 'string') {
        return binaryGapList.length - 2
    }
    return binaryGapList.sort((a, b) => a < b ? 1 : -1)[0].length - 2
}
