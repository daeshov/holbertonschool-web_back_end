const Utils = {
    calculateNumber(type, a, b) {
      // Round 'a' and 'b'.
      const roundA = Math.round(a);
      const roundB = Math.round(b);
  
      // Perform calculations based on the 'type' argument.
      if (type === "SUM") {
        return roundA + roundB;
      } else if (type === "SUBTRACT") {
        return roundA - roundB;
      } else if (type === "DIVIDE") {
        if (roundB === 0) {
          return "Error"; // Division by zero is not allowed.
        }
        return roundA / roundB;
      } else {
        // Handle unsupported 'type' values.
        return "Unsupported operation";
      }
    },
  };
  
  module.exports = Utils;
  