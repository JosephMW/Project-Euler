let countSundaysOnFirstMonth = 0;
let day = 367; // 1 is monday; 2 tues; ... ; 7 sunday
for (let i = 1901; i <= 2000; i++) {
  let isLeapYear = i % 4 == 0;

  // First of jan:
  if (day % 7 == 0) {
    countSundaysOnFirstMonth++;
  }
  day += 31;
  //first of feb:
  if (day % 7 == 0) {
    countSundaysOnFirstMonth++;
  }
  day += isLeapYear ? 29 : 28;
  // first day of march:
  if (day % 7 == 0) {
    countSundaysOnFirstMonth++;
  }
  day += 31;
  // first day april:
  if (day % 7 == 0) {
    countSundaysOnFirstMonth++;
  }
  day += 30;
  // first day may:
  if (day % 7 == 0) {
    countSundaysOnFirstMonth++;
  }
  day += 31;
  // first day june:
  if (day % 7 == 0) {
    countSundaysOnFirstMonth++;
  }
  day += 30;
  // first day july:
  if (day % 7 == 0) {
    // TODAY IS A SUNDAY
    countSundaysOnFirstMonth++;
  }
  day += 31;
  // first day august:
  if (day % 7 == 0) {
    // TODAY IS A SUNDAY
    countSundaysOnFirstMonth++;
  }
  day += 31;
  //first day september:
  if (day % 7 == 0) {
    // TODAY IS A SUNDAY
    countSundaysOnFirstMonth++;
  }
  day += 30;
  // first day october:
  if (day % 7 == 0) {
    // TODAY IS A SUNDAY
    countSundaysOnFirstMonth++;
  }
  day += 31;
  // first day november:
  if (day % 7 == 0) {
    // TODAY IS A SUNDAY
    countSundaysOnFirstMonth++;
  }
  day += 30;
  // first day december:
  if (day % 7 == 0) {
    // TODAY IS A SUNDAY
    countSundaysOnFirstMonth++;
  }
  day += 31;
}

console.log(countSundaysOnFirstMonth);
