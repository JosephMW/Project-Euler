const quadratic = (x, a, b) => {
  return x ** 2 + a * x + b;
};

const isPrime = (num) => {
  for (let i = 2, s = Math.sqrt(num); i <= s; i++)
    if (num % i === 0) return false;
  return num > 1;
};

const numberConsecPrimes = (a, b) => {
  let x = 0;
  let val = quadratic(x, a, b);
  let count = 0;
  while (isPrime(val)) {
    count++;
    x++;
    val = quadratic(x, a, b);
  }
  return count;
};

const findab = (amin, amax, bmin, bmax) => {
  let besta = 0;
  let bestb = 0;
  let bestcount = 0;
  let currentcount = 0;
  for (let a = amin; a <= amax; a++) {
    for (let b = bmin; b <= bmax; b++) {
      currentcount = numberConsecPrimes(a, b);
      if (currentcount > bestcount) {
        besta = a;
        bestb = b;
        bestcount = currentcount;
      }
    }
  }
  return besta * bestb;
};

console.log(findab(-999, 999, -1000, 1000));
