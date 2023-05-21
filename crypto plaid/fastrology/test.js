const { randomInt, createHash } = require('node:crypto');
expected = 'QSHSWdad'
console.log(createHash('md5').update(expected, 'utf8').digest('hex'));
