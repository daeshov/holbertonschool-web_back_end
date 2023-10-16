-- Check if the table already exists, and if it does, do nothing
    CREATE TABLE IF NOT exists users (
        id serial PRIMARY KEY,
        email VARCHAR(255) NOT NULL UNIQUE,
        name VARCHAR(255)
    );
