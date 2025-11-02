CREATE DATABASE everest_project;

use everest_project;

--Table for users 
CREATE TABLE users
(
  user_id INT NOT NULL AUTO_INCREMENT,
  username VARCHAR(240) NOT NULL,
  firstName VARCHAR(240) NOT NULL, 
  lastName VARCHAR(240) NOT NULL,
  email VARCHAR(240) NOT NULL,
  password VARCHAR(240) NOT NUll,
  PRIMARY KEY(user_id)
);

:key="$route.fullPath"