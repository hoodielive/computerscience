/** 
 * Suppose we want to write a function that calculated the sum of all numbers
 * from 1 up to and including some number (n)
*/ 

function addUpTo(n) { 
  let total = 0 
  for (let i = 0; i <= n; i++) {
    total += i; 
  }
  return total; 
}
addUpTo(2)

// n + ( n - 1 ) + ( n - 2 ) + ... ( n - 1 ) + n 
function addUp(n) {
  return n * (n + 1) / 2; 
}

// let time1 = performance.now(); 
addUp(100000000);

// let time2 = performance.now(); 
// console.log(`Time Elapsed: ${(time2 - time1) / 1000} seconds.`)
