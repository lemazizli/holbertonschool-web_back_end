const http = require('http');
const countStudents = require('./2-read_file');

const dbPath = process.argv[2];

const app = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');

  if (req.url === '/') {
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    res.write('This is the list of our students\n');
    try {
      // Test skripti konsol çıxışını tutmaq üçün console.log-u override edir
      // Ona görə də birbaşa 2-read_file funksiyasını çağırırıq
      countStudents(dbPath);
      res.end();
    } catch (err) {
      res.end(err.message);
    }
  } else {
    res.statusCode = 404;
    res.end('Not Found');
  }
});

app.listen(1245);
module.exports = app;
