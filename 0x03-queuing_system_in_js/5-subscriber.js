import { createClient } from 'redis';

const client = createClient();

client.on('connect', function () {
  console.log('Redis client connected to the server');
});

client.on('error', function (error) {
  console.log(`Redis client not connected to the server: ${error}`);
});

client.subscribe('holberton school channel');
client.on('message', (channel, message) => {
  console.log(message);
  if (message === 'KILL_SERVER') {
    client.unsubscribe();
    client.quit();
  }
});
