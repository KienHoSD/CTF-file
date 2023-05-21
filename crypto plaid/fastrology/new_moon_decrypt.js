const { randomInt, createHash } = require('node:crypto');
expected = 'QSHSWdad'
console.log(createHash('md5').update(expected, 'utf8').digest('hex'));

const prefix_len = 192;
const alphabet = '♈♉♊♋♌♍♎♏♐♑♒♓⛎';
let output = '⛎♑♎♉♋♈⛎♌♉♐♒♈♒♉♉♏♎♒♏♊♐♐♑♉♎♊♐♏♊♏♓♑♐♋♊♒♋♓♉♐♒♉♎⛎♏♒♈♍♈♈♈♑♌♈♌♍♎♊♑♐♏♐⛎♊♒♍♒♎♉♑⛎♓♐♌♉♈♐♈♋⛎⛎♎♍⛎♑♉♏⛎♓♒♒♑♓♓♑♍⛎♒♏⛎♐♑♈♈♉♌♊♑♊♍♒♍♋♉♎♈♌⛎♐♎♑⛎♌♌⛎♏♎♒♑♑♒♏⛎⛎♎♊♎♋♍♓♌♒⛎⛎♈♋♏♎♏♓♑♎♏♉♓♊♏♐♍♍♑♈♐♓♌♋♉♊♎♏♏♓♋♓♐♌♋♊⛎♏♋♎♍♈♓♏♒♉♏♌♏♋';
while (true)

    for (let i = 0; i < 128; i++) {
        output += alphabet[Math.floor(Math.random() * alphabet.length)];
    }
    output = '⛎♑♎♉♋♈⛎♌♉♐♒♈♒♉♉♏♎♒♏♊♐♐♑♉♎♊♐♏♊♏♓♑♐♋♊♒♋♓♉♐♒♉♎⛎♏♒♈♍♈♈♈♑♌♈♌♍♎♊♑♐♏♐⛎♊♒♍♒♎♉♑⛎♓♐♌♉♈♐♈♋⛎⛎♎♍⛎♑♉♏⛎♓♒♒♑♓♓♑♍⛎♒♏⛎♐♑♈♈♉♌♊♑♊♍♒♍♋♉♎♈♌⛎♐♎♑⛎♌♌⛎♏♎♒♑♑♒♏⛎⛎♎♊♎♋♍♓♌♒⛎⛎♈♋♏♎♏♓♑♎♏♉♓♊♏♐♍♍♑♈♐♓♌♋♉♊♎♏♏♓♋♓♐♌♋♊⛎♏♋♎♍♈♓♏♒♉♏♌♏♋';