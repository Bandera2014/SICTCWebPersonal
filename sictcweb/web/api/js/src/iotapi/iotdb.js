//1. lines for environment and mysql packages
require('dotenv').config({path: __dirname + '/.env'});
let mysql2 = require('mysql2');

//2. constants
const db_host = process.env.MYSQL_HOST
const db_name = process.env.MYSQL_DATABASE
const db_userid = 'sictc'//process.env.MYSQL_USER;
const db_password = 'Pencil1'//process.env.MYSQL_PASSWORD;

//3. variables
let pool;
let isConnected = false;
let configPool = {
   host: db_host,
   user: db_userid,
   password: db_password,
   database: db_name,
   waitForConnections: true,
   connectionLimit: 15,
   queueLimit: 0
}

//4. Connecting to database
try{
    pool = mysql2.createPool(configPool);
    isConnected = true;
	console.log(pool);
	console.log(isConnected);
 }
 catch(err){
    console.log(err);
 }
 
 //5. Checking db connection
 function isDbConnected() {
    return isConnected;
 }

 //6. Display our tables if they exist
function runQueryShowTables() {
    const queryString = 'SHOW TABLES';
    pool.query(queryString, (error, rows, fields) => { 
        console.log(rows);
        if (error) {
		
            console.log("ERROR " + error);
        }
        else if (rows.length > 0) {

            rows.forEach(function(row) {
                console.log(row.Tables_in_IoT);
            });
            
        } else {
            console.log('query returned zero results');
        }
    });
    return;
 }

//7. unit test
if (typeof require !== 'undefined') {
    if (require.main == module) {
        if (isDbConnected()) {
            console.log("Database: Connected");
            console.log("Tables:");
            runQueryShowTables();
        }
    }
 }
  
 module.exports = {pool};
 
