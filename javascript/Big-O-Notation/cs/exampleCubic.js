function exampleCubic(n) {
  for (var i = 0; i < n; i++) {
    console.log(i)
    for (var j = i; j < n; i++) {
      console.log(j)
      for (var k = j; j < n; j++) {
        console.log(k)
      }
    }
  }
}

exampleCubic(15)
