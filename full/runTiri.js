var cmd = require('node-cmd')

cmd.run("arecord -t raw -c 1 -r 16000 -f S16_LE | ./TiriUI.py");