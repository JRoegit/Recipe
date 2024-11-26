DROP TABLE REVIEWS;

CREATE TABLE IF NOT EXISTS USERS(
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR NOT NULL,
    password VARCHAR NOT NULL
);

CREATE TABLE IF NOT EXISTS RECIPES(
    recipe_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR,
    story VARCHAR,  
    category VARCHAR,
    photo BLOB,
    date_added DATE,
    servings INTEGER,
    prep_time INTEGER,
    cook_time INTEGER,
    user_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES USERS(user_id) ON DELETE CASCADE
);

-- Optional images?
CREATE TABLE IF NOT EXISTS DIRECTIONS(
    direction_id INTEGER PRIMARY KEY AUTOINCREMENT,
    step_num INTEGER,
    step_description VARCHAR,
    recipe_id INTEGER,
    FOREIGN KEY (recipe_id) REFERENCES RECIPES(recipe_id) ON DELETE CASCADE
);

-- Seperate amount and name? for multiplicative reasons?
CREATE TABLE IF NOT EXISTS INGREDIENTS(
    ingredient_id INTEGER PRIMARY KEY AUTOINCREMENT,
    ingredient VARCHAR,
    recipe_id INTEGER,
    FOREIGN KEY (recipe_id) REFERENCES RECIPES(recipe_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS REVIEWS(
    review_id INTEGER PRIMARY KEY AUTOINCREMENT,
    rating INT,
    review VARCHAR,
    review_date DATE, 
    user_id INTEGER,
    recipe_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES USERS(user_id) ON DELETE CASCADE
    FOREIGN KEY (recipe_id) REFERENCES RECIPES(recipe_id) ON DELETE CASCADE
);

INSERT INTO USERS (username, password) VALUES ('Jacob', "ruGer123")