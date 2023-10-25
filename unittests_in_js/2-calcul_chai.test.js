const { expect } = require('chai');
const calculateNumber = require('./2-calcul_chai');

describe('calculateNumber', () => {
	it('checks output for add', () => {
        expect(calculateNumber('SUM', 1, 7)).to.equal(8);
        expect(calculateNumber('SUM', 1, 6.7)).to.equal(8);
        expect(calculateNumber('SUM', 3.7, 1)).to.equal(5);
        expect(calculateNumber('SUM', 1, 5.3)).to.equal(6);
        expect(calculateNumber('SUM', 1.2, 3.7)).to.equal(5);
	});
});

describe('calculateNumber', () => {
	it('checks output for subtract', () => {
        expect(calculateNumber('SUBTRACT', 2, 3)).to.equal(-1);
        expect(calculateNumber('SUBTRACT', 2.9, 3)).to.equal(0);
        expect(calculateNumber('SUBTRACT', 6.6, 3.2)).to.equal(4);
        expect(calculateNumber('SUBTRACT', 4.2, 3.9)).to.equal(0);

	});
});

describe('calculateNumber', () => {
	it('checks output for divide', () => {
        expect(calculateNumber('DIVIDE', 4.2, 3.9)).to.equal(1);
        expect(calculateNumber('DIVIDE', 4.2, 3)).to.equal(1.3333333333333333);
        expect(calculateNumber('DIVIDE', 2.2, 0)).to.equal ('Error');
        expect(calculateNumber('DIVIDE', 2, 2)).to.equal(1);
	});
});
