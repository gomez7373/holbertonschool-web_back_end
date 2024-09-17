const fs = require('fs');

function countStudents(path) {
    try {
        // Read the file synchronously
        const data = fs.readFileSync(path, 'utf8');

        // Split the data by newlines to get each line
        const lines = data.split('\n').filter(line => line.trim() !== '');

        // Ignore the header row
        const students = lines.slice(1);

        // Initialize the student count and a map to store counts by field
        const numberOfStudents = students.length;
        const fields = {};

        // Process each student's data
        students.forEach((student) => {
            const [firstname, lastname, age, field] = student.split(',');
            if (!fields[field]) {
                fields[field] = [];
            }
            fields[field].push(firstname);
        });

        // Output the total number of students
        console.log(`Number of students: ${numberOfStudents}`);

        // Output the number of students in each field and their names
        for (const [field, students] of Object.entries(fields)) {
            console.log(`Number of students in ${field}: ${students.length}. List: ${students.join(', ')}`);
        }
    } catch (error) {
        throw new Error('Cannot load the database');
    }
}

module.exports = countStudents;

