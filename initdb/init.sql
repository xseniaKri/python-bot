CREATE TABLE Users (
    user_id SERIAL PRIMARY KEY,
    nickname VARCHAR(100) NOT NULL
);

CREATE TABLE Results (
    result_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES Users(user_id),
    total_score INT NOT NULL
);