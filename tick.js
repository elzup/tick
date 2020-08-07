const sleep = (msec) => new Promise((resolve) => setTimeout(resolve, msec));
const min = 60 * 1000;

function tick() {
  console.log(new Date());
  sleep(min).then(tick);
}

tick();
