// full_server/utils.js

import fs from 'fs';

function readDatabase(filePath) {
  return new Promise((resolve, reject) => {
    fs.readFile(filePath, 'utf8', (err, data) => {
      if (err) {
        reject('Cannot load the database');
      } else {
        const lines = data.split('\n');
        const database = {};
        lines.forEach((line) => {
          const [field, firstName] = line.split(',');
          if (field && firstName) {
            const normalizedField = field.trim().toLowerCase();
            if (!database[normalizedField]) {
              database[normalizedField] = [];
            }
            database[normalizedField].push(firstName.trim());
          }
        });
        resolve(database);
      }
    });
  });
}

export { readDatabase };
