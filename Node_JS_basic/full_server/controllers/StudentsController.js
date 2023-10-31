// full_server/controllers/StudentsController.js
import { readDatabase } from '../utils';

class StudentsController {
  static async getAllStudents(req, res) {
    try {
      const database = await readDatabase('./database.csv');
      const response = ['This is the list of our students'];
      const fields = Object.keys(database).sort();

      fields.forEach((field) => {
        const students = database[field];
        response.push(`Number of students in ${field.toUpperCase()}: ${students.length}. List: ${students.join(', ')}`);
      });

      res.status(200).send(response.join('\n'));
    } catch (error) {
      res.status(500).send(`Cannot load the database: ${error}`);
    }
  }

  static async getAllStudentsByMajor(req, res) {
    const { major } = req.params;

    if (major !== 'CS' && major !== 'SWE') {
      res.status(500).send('Major parameter must be CS or SWE');
      return;
    }

    try {
      const database = await readDatabase('./database.csv');
      const students = database[major.toLowerCase()] || [];
      res.status(200).send(`List: ${students.join(', ')}`);
    } catch (error) {
      res.status(500).send(`Cannot load the database: ${error}`);
    }
  }
}

export default StudentsController;
