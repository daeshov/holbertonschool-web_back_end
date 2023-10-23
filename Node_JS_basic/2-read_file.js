const fs = require('fs');
const csv = require('csv-parser');

function countStudents(path) {
  try {
    if (!fs.existsSync(path)) {
      throw new Error('Cannot load the database');
    }

    const students = { };

    fs.createReadStream(path)
      .pipe(csv())
      .on('data', (data) => {
        if (data.field && data.firstName) {
          if (!students[data.field]) {
            students[data.field] = {
              count: 0,
              list: [],
            };
          }

          students[data.field].count++;
          students[data.field].list.push(data.firstName);
        }
      })
      .on('end', () => {
        const totalStudents = Object.keys(students).reduce((total, field) => {
          console.log(`Number of students in ${field}: ${students[field].count}. List: ${students[field].list.join(', ')}`);
          return total + students[field].count;
        }, 0);
        console.log(`Number of students: ${totalStudents}`);
      });
  } catch (error) {
    console.error(error.message);
  }
}

// Usage
module.exports = countStudents;
