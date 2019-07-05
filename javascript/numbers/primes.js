prime_numbers = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]

5 = (6-1), 7 = ((1*6) + 1), 13 = ((2 * 6) + 1)

function isPrime(n) {
    if (n <= 1) return false; 
    if (n <= 3) return true; 

    if (n % 2 == 0 || n % 3 == 0) return false; 

    for (var i = 5; i * i <= n; i = i + 6) {
        if (n % i == 0 || n % (i + 2) == 0)
            return false; 
    }

    return true;
}