CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    user_id BIGINT NOT NULL,
    nickname VARCHAR(30) NOT NULL,
    result INT NOT NULL,
    hard VARCHAR(30) NOT NULL
);
