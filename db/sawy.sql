DROP TABLE transactions;
DROP TABLE merchants;
DROP TABLE labels;

CREATE TABLE labels (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE merchants (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    label_id INT REFERENCES labels(id) ON DELETE CASCADE,
    merchant_id INT REFERENCES merchants(id) ON DELETE CASCADE,
    amount INTEGER
);