const express = require('express');
const path = require('path');
const app = express();
const bodyParser = require('body-parser');
const routeStates = require('./routes/states.js');
const routeAccounts = require('./routes/accounts.js');
const cors = require('cors');

const NAME = require(__dirname + '/package.json').name;
const libiotdb = require('./iotdb');
const PORT = 3000;

app.use('/states', routeStates);
app.use('/accounts',routeAccounts);
app.use(cors());

app.listen(PORT, () => console.log('IoT REST API running on port 3000'));

/*
 * Example route testing that app is running.
 */

app.get('/whoami', (request, response) => {
    var url = path.join(request.baseUrl, request.url);
    console.log(url);
    response.send('<div><h1>Hello, HTML</h1></div>');
});

