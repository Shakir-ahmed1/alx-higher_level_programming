#!/usr/bin/node
function addMeMaybe (nb, theFunction) {
  nb++;
  theFunction(nb);
}
module.exports.addMeMaybe = addMeMaybe
