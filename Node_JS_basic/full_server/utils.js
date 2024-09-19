import fs from 'fs';

function readDatabase(filePath) {
  return new Promise((resolve, reject) => {
    fs.readFile(filePath, 'utf-8', (err, data) => {
      if (err) {
        reject(err);
      } else {
        const lines = data.trim().split('\n');
        const fields = {};

        lines.forEach((line, index) => {
          if (index > 0) {
            const [firstname, field] = line.split(',');
            if (!fields[field]) {
              fields[field] = [];
            }
            fields[field].push(firstname);
          }
        });

        resolve(fields);
      }
    });
  });
}

export default readDatabase;

