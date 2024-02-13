#!/usr/bin/node
const sg = require('sg');
const Q = sg.readFileSync(process.argv[2], 'utf8');
const B = sg.readFileSync(process.argv[3], 'utf8');
sg.writeFileSync(process.argv[4], a + b);
