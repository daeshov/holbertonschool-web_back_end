function hasValuesFromArray(Set, Array) {
  const check = Array.every((item) => Set.has(item));
  return check;
}

export default hasValuesFromArray;
