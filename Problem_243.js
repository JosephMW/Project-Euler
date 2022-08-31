const findFactors = (num) => {
  let factors = [];
  for (let i = 2; i <= Math.sqrt(num); i++) {
    if (num % i == 0) {
      factors.push(i);
    }
  }
  if (num != 1) {
    factors.push(num);
  }
  return factors;
};

const checkResilient = (top, bot) => {
  // get the factors of each and see if they share any.

  topFactors = findFactors(top);
  botFactors = findFactors(bot);

  for (let i = 0; i < topFactors.length; i++) {
    for (let j = 0; j < botFactors.length; j++) {
      if (topFactors[i] == botFactors[j]) {
        return false;
      }
    }
  }
  return true;
};

const resilience = (denom, lim) => {
  let count = 1;

  for (let i = 2; i < denom; i++) {
    if (checkResilient(i, denom)) {
      count++;
      if (count / (denom - 1) > lim) {
        return count / (denom - 1);
      }
    }
  }
  // return ratio of resilient to all proper fractions
  return count / (denom - 1);
};

const smallestDenomResUnder = (lim) => {
  res = 1;
  denom = 259000;
  while (res > lim) {
    denom++;
    res = resilience(denom, lim);
    if (denom % 1 == 0) {
      console.log(denom);
      console.log(res);
    }
  }
  return denom;
};

// approach is correct but WAY TOO SLOW
console.log(smallestDenomResUnder(0.2));
