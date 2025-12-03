DROP TABLE IF EXISTS answer;
DROP TABLE IF EXISTS question;

CREATE TABLE question (
    id INT NOT NULL AUTO_INCREMENT,
    title VARCHAR(255) NOT NULL,
    option_1 VARCHAR(255) NOT NULL,
    option_2 VARCHAR(255) NOT NULL,
    option_3 VARCHAR(255) NOT NULL,
    option_4 VARCHAR(255) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE answer (
    id INT NOT NULL AUTO_INCREMENT,
    user_id INT NOT NULL,
    question_id INT NOT NULL,
    selected_option TINYINT NOT NULL CHECK (selected_option BETWEEN 1 AND 4),
    PRIMARY KEY (id),
    UNIQUE KEY uq_user_question (user_id, question_id)
);
