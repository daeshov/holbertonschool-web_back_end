function getStudentIdsSum(students) {
  if (!Array.isArray(students)) {
    return [];
  }

  const reducer = (acc, item) => acc + item.id;

  const sumids = students.reduce(reducer, 0);

  return sumids;
}

export default getStudentIdsSum;
