const assert = require('assert');
const calculateNumber = require('./1-calcul');

describe('calculateNumber', function () {
  // Test cases for type: SUM
  describe('Type: SUM', function () {
    it('should add two positive numbers and round the result', function () {
      assert.strictEqual(calculateNumber('SUM', 1.5, 3.4), 5);
    });

    it('should add two negative numbers and round the result', function () {
      assert.strictEqual(calculateNumber('SUM', -1.5, -3.4), -5);
    });

    it('should add a positive and a negative number and round the result', function () {
      assert.strictEqual(calculateNumber('SUM', 1.5, -3.4), -2);
    });
  });

  // Test cases for type: SUBTRACT
  describe('Type: SUBTRACT', function () {
    it('should subtract two positive numbers and round the result', function () {
      assert.strictEqual(calculateNumber('SUBTRACT', 5.5, 3.4), 2);
    });

    it('should subtract two negative numbers and round the result', function () {
      assert.strictEqual(calculateNumber('SUBTRACT', -5.5, -3.4), -2);
    });

    it('should subtract a positive and a negative number and round the result', function () {
      assert.strictEqual(calculateNumber('SUBTRACT', 5.5, -3.4), 9);
    });
  });

  // Test cases for type: DIVIDE
  describe('Type: DIVIDE', function () {
    it('should divide two positive numbers and round the result', function () {
      assert.strictEqual(calculateNumber('DIVIDE', 10, 2.5), 4);
    });

    it('should handle division by zero and return "Error"', function () {
      assert.strictEqual(calculateNumber('DIVIDE', 5.5, 0), 'Error');
    });

    it('should divide a negative number by a positive number and round the result', function () {
      assert.strictEqual(calculateNumber('DIVIDE', -8, 3.4), -2);
    });
  });
});
