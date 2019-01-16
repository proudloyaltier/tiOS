var cmd = require('node-cmd')

this.startListening = function() {
  cmd.run("arecord -t raw -c 1 -r 16000 -f S16_LE | ./TiriUI.py");
}
