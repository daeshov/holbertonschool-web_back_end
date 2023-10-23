const http = require('http');
const url = require('url');
const countStudents = require('./3-read_file_async'); // Import the countStudents function

const app = http.createServer((req, res) => {
  const parsedUrl = url.parse(req.url, true);
  const path = parsedUrl.pathname;

  res.writeHead(200, { 'Content-Type': 'text/plain' });

  if (path === '/') {
    res.end('Hello Holberton School!\n');
  } else if (path === '/students') {
    const databasePath = 'database.csv'; // Adjust the path as needed
    countStudents(databasePath)
      .then((data) => {
        res.end(`This is the list of our students\n${data}`);
      })
      .catch((error) => {
        res.end(`This is the list of our students\n${error.message}`);
      });
  } else {
    res.end('Not Found\n');
  }
});

app.listen(1245);

module.exports = app;
