import redis from 'redis';

const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error.message}`);
});

// Function to set a new school value in Redis
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

// Function to display the value for a school in Redis
async function displaySchoolValue(schoolName) {
    const asyncGet = promisify(client.get).bind(client);
    const value = await asyncGet(schoolName);
    console.log(value);
}

displaySchoolValue("Holberton").catch((err) =>  console.err(err));
setNewSchool("HolbertonSanFrancisco", "100");
displaySchoolValue("HolbertonSanFrancisco").catch((err) =>  console.err(err));
