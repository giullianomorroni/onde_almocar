var events = require('events');
var eventEmitter = new events.EventEmitter();

function main() {
  console.log('Starting Application')
  eventEmitter.emit('starApp');
}

function startApplication(){
  console.log('Application started')
}

function startApplicationListen(){
  console.log('Server event listtening')
}

eventEmitter.on('starApp',startApplication);
eventEmitter.on('starApp',startApplicationListen);

main();