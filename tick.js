const sleep = (msec) => new Promise((resolve) => setTimeout(resolve, msec));

function tick() {
  console.log(new Date());
  sleep(1000).then(tick);
}

tick();
