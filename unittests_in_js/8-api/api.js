const express = require('express');

const app = express();
const connect = 7885;

app.get('/', (req, res) => {
    res.send('Welcome to the payment system');
});

app.listen(connect, () => {
    console.log('API available on localhost port ${connect}');
});

module.exports = app;
