// consts and variables
var express = require('express');
var router = express.Router();
 
const libiotdb = require('../iotdb');
const bodyParser = require('body-parser');
const cors = require('cors');

//Parsing handler 
router.use(bodyParser.json());
router.use(cors());

//get requests whoami
router.get('/whoami', (request, response) => {
   const content = request.baseUrl;
 
   console.log(content);
   response.send(content);
});

//get request, retireve all accounts on the server
router.get('/', (request, response) => {

//2. All accounts
   const queryString = 'SELECT * FROM Accounts';

//3. Response if statements for either error in syntax, results greater than 0, or nothing 
   libiotdb.pool.query(queryString, (error, result, fields) => {
       if (error) {
           console.log("ERROR: " + error);
           response.status(500).json(JSON.stringify(error));
       }
  
       if (result.length > 0) {
           console.log(JSON.stringify(result));
           response.status(200).json(result);
          
       } else {
           console.log('Query returned zero results.');
           response.status(204).end();
       }
   }); 
 
});

router.post('/add', (request, response) => {
   const content = request.body;
   const queryString = `INSERT INTO Accounts (Name, Address, City, Zip, State) VALUES (?,?,?,?,?)`;
 
   libiotdb.pool.query(queryString, [content.Name, content.Address, content.City, content.Zip, content.State], (error, result, fields) => {
       if (error) {
           console.log("ERROR: " + error);
           response.status(500).json(JSON.stringify(error));
       } else {
           response.status(200).json({"Id": result.insertId});
           console.log({"Id": result.insertId});
           response.status(200).end();
       }
   }); 
});


//delete an account
router.delete('/delete/:id', (request, response) => {
   const content = request.body;
   const queryString = 'DELETE FROM Accounts WHERE Id = ?'
 
   libiotdb.pool.query(queryString, [content.Id], (error, result, fields) => {
       if (error) {
           console.log("ERROR: " + error);
           response.status(500).json(JSON.stringify(error));
       } else {
           console.log('Success!');
           response.status(200).end();
       }
   }); 
});


//getting account by specific id 
router.get('/:id', (request, response) => {
 
   const content = request.params;
   const queryString = 'SELECT Id, Name FROM Accounts WHERE Id = ?';
 
   libiotdb.pool.query(queryString, [content.id], (error, result, fields) => {
       if (error) {
           console.log("ERROR: " + error);
           response.status(500).json(JSON.stringify(error));
       }
  
       if (result.length > 0) {
           console.log(JSON.stringify(result));
           response.status(200).json(result);
          
       } else {
           console.log('Query returned zero results.');
           response.status(204).end();
       }
   });
}); 

//Updating a specific account
router.post('/update', (request, response) => {
   const content = request.body;
   console.log(content.Id.toString());
   const queryString = `UPDATE Accounts SET Name = ?, Address = ?, City = ?, State = ?, Zip = ? WHERE Id = ?`;
 
   libiotdb.pool.query(queryString, [content.Name, content.Address, content.City, content.State, content.Zip, content.Id], (error, result, fields) => {
       if (error) {
           console.log("ERROR: " + error);
           response.status(500).json(JSON.stringify(error));
       } else {
           response.status(200).json({"Id": result.insertId});
           console.log({"Id": result.insertId});
           response.status(200).end();
       }
   }); 
});










 
module.exports = router;

