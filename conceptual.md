### Conceptual Exercise

Answer the following questions below:

- What is PostgreSQL?

PostgreSQL is a free and open-source relational database management system emphasizing extensibility and SQL compliance.

- What is the difference between SQL and PostgreSQL?

SQL is structured query language, whereas PostgreSQL is an open source object-relational database management system

- In `psql`, how do you connect to a database?

\c DATABASE_NAME

- What is the difference between `HAVING` and `WHERE`?

Having filters data based on conditions that certain groups of rows would have, whereas Where is used to filter data based on conditions that individual rows would have.

- What is the difference between an `INNER` and `OUTER` join?
Inner is used to return rows that have matching values in both tables; outer returns only non-matching rows.

- What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?

left outer returns all rows from the left table and matching rows from the right.
Right outer returns all rows from the right table and matching rows from the left.

- What is an ORM? What do they do?

Object relational mapping; a technique that lets you query and manipulate data from a database using an object-oriented paradigm.

- What are some differences between making HTTP requests using AJAX 
  and from the server side using a library like `requests`?

  AJAX requests are faster, but less secure.
  Server side requests may take longer, but are more secure from tampering or interception.

- What is CSRF? What is the purpose of the CSRF token?

Cross site request forgery. CSRF tokens are secret tokens to validate requests sent between servers and clients.

- What is the purpose of `form.hidden_tag()`?

These are used to generate a hidden form field that contains the CSRF token.