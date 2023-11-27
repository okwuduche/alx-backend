import { createClient, print } from 'redis';
import { promisify } from 'util';

const client = createClient();

client.on('connect', function () {
  console.log('Redis client connected to the server');
});

client.on('error', function (err) {
  console.log(`Redis client not connected to the server: ${err}`);
});

function setNewSchool (schoolName, value) {
  client.set(schoolName, value, print);
}

async function displaySchoolValue (schoolName) {
  const getAsync = promisify(client.get).bind(client);
  try {
    const result = await getAsync(schoolName);
    console.log(result);
  } catch (error) {
    console.log(error);
    throw error;
  }
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
