function getStudentsByLocation(location, city) {
  if (!Array.isArray(location)) {
    return [];
  }

  const result = location.filter((item) => item.location === city);

  return result;
}

export default getStudentsByLocation;
