#!/usr/bin/node
function callMeMoby (iter, func) {
  for (let i = 0; i < iter; i++) func();
}
module.exports.callMeMoby = callMeMoby;
