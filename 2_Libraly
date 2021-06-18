"use strict"
function main(lines) {
  // lines: Array<string>
  const AVAILABLE_BOOKS_NUMBER = lines[0]
  let isOpen = false
  const rentalList = new Array(100000000).fill(null)
  const reserveList = new Array(100000000).fill([]) /* bookId: [...userIdList] */
  const keepList = new Array(10000000).fill([]) /* userID: [...bookIdList] */

  lines.forEach((v) => executeCmd(v.split(" ")))

  function executeCmd(cmdline) {
    switch (cmdline[0]) {
      case "open":
        isOpen = true
        console.log("open")
        break
      case "close":
        isOpen = false
        console.log("close")
        break
      case "borrow":
        borrow(cmdline)
      case "return":
        returnExec(cmdline)
      case "reserve":
        reserve(cmdline)
      default:
    }
  }

  function borrow(cmdline) {
    const userId = cmdline[1]
    const bookList = cmdline.slice(2)
    const overBookCnt =
      AVAILABLE_BOOKS_NUMBER -
      (rentalList.filter((v) => v === userId).length + keepList[userId].length + bookList.length)
    if (overBookCnt > 0) {
      console.log(`cannnot ${overBookCnt}`)
    } else {
      keepList[userId].forEach((v) => {
        reserveList[v].shift()
        keepList[userId] = []
      })
      console.log(`can ${keepList[userId].sort().join(" ")}`)
    }
  }

  function returnExec(cmdline) {
    const bookList = cmdline.slice(1)
    for (let i = 0; i < bookList.length; i++) {
      rentalList[bookList[i]] = null
      if (reserveList[bookList[i]].length > 0) {
        keepList[reserveList[bookList[i]][0]].push(bookList[i])
        console.log(reserveList[bookList[i]][0])
      } else {
        console.log("return")
      }
    }
  }

  function reserve(cmdline) {
    const userId = cmdline[1]
    const bookList = cmdline.slice(2)
    const cannotList = []
    for (let i = 0; i < bookList.length; i++) {
      /* TODO予約数で判定する */
      if (
        reserveList.flatMap.filter((v) => v === userId).length < AVAILABLE_BOOKS_NUMBER &&
        rentalList[bookList[i]] != null
      ) {
        reserveList[bookList[i]].push(userId)
      } else {
        cannotList.push(("00000000" + bookList).slice(-8))
      }
      if (bookList.length)
        console.log(cannotList.length === 0 ? "can" : `cannot ${cannotList.join(" ")}`)
    }
  }
}

/* default method */
function runWithStdin() {
  let input = ""
  process.stdin.resume()
  process.stdin.setEncoding("utf8")

  process.stdin.on("data", (v) => {
    input += v
  })
  process.stdin.on("end", () => {
    main(input.split("\n"))
  })
}
runWithStdin()
