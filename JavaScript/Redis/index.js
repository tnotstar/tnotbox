var redis = require('redis');
var client = redis.createClient();

client.on('connect', function(){
    console.log('Successfully connected')
});

client.del('test')

client.hmset('test', {
  name: 'Joe Doe',
  age: 42
});

client.hgetall('test', function(err, object) {
  console.table(object)
  console.log(`${typeof object}, ${typeof object.name}, ${typeof object.age}`);
});

client.quit()