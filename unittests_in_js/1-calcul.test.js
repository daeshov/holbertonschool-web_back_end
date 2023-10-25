const assert = require('assert');
const calculateNumber = require('./1-calcul');

describe('calculateNumber', () => {
	it('checks output for add', () => {
        assert.strictEqual(calculateNumber('SUM', 1, 7), 8);
        assert.strictEqual(calculateNumber('SUM', 1, 6.7), 8);
        assert.strictEqual(calculateNumber('SUM', 3.7, 1), 5);
        assert.strictEqual(calculateNumber('SUM', 1, 5.3), 6);
        assert.strictEqual(calculateNumber('SUM', 1.2, 3.7), 5);
	});
});

describe('calculateNumber', () => {
	it('checks output for subtract', () => {
        assert.strictEqual(calculateNumber('SUBTRACT', 2, 3), -1);
        assert.strictEqual(calculateNumber('SUBTRACT', 2.9, 3), 0);
        assert.strictEqual(calculateNumber('SUBTRACT', 6.6, 3.2), 4);
        assert.strictEqual(calculateNumber('SUBTRACT', 4.2, 3.9), 0);

	});
});

describe('calculateNumber', () => {
	it('checks output for divide', () => {
        assert.strictEqual(calculateNumber('DIVIDE', 4.2, 3.9), 1);
        assert.strictEqual(calculateNumber('DIVIDE', 4.2, 3), 1.3333333333333333);
        assert.strictEqual(calculateNumber('DIVIDE', 2.2, 0), 'Error');
        assert.strictEqual(calculateNumber('DIVIDE', 2, 2), 1);
	});
});
