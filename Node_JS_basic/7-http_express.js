const express = require('express');
const app = express();
const countStudents = require('./3-read_file_async'); // Import the countStudents function

app.use(express.json());

app.get('/', (req, res) => {
  res.status(200).send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  const databasePath = 'database.csv'; // Adjust the path as needed
  countStudents(databasePath)
    .then((data) => {
      const response = `This is the list of our students\n${data}`;
      res.status(200).send(response);
    })
    .catch((error) => {
      res.status(500).send(`This is the list of our students\n${error.message}`);
    });
});

app.listen(1245, () => {
  console.log('Server is running on port 1245');
});

module.exports = app;
