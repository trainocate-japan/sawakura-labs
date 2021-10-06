---- set using database ---
USE labdb;

---- drop ----
DROP TABLE IF EXISTS contents;

---- create ----
create table IF not exists contents
(
id               INT(20) AUTO_INCREMENT PRIMARY KEY,
course_code             VARCHAR(16) NOT NULL,
course_name             VARCHAR(120) NOT NULL
) DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

---- insert data ----
INSERT INTO contents (id, course_code, course_name)
VALUES
(0, 'NFC0313G', 'クラウドコンピューティング概要'),
(0, 'NFC0267G', 'クラウドアーキテクト・ファーストステップ');
