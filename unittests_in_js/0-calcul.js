module.exports = function calculateNumber(a, b){
    // rounds a and b.
    const rounda = Math.round(Number(a));
    const roundb = Math.round(Number(b));

    // returns sum of both.
    const sum = rounda + roundb;
    return sum;
};
