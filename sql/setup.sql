---- set using database ---
USE labdb;

---- drop ----
DROP TABLE IF EXISTS contents;

---- create ----
create table IF not exists contents
(
id               INT(20) AUTO_INCREMENT PRIMARY KEY,
course_code             VARCHAR(16) NOT NULL,
course_name             VARCHAR(120) NOT NULL,
duration                SMAILLINT NOT NULL
) DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

---- insert data ----
INSERT INTO contents (id, course_code, course_name, duration)
VALUES
(0, 'NFC0313G', 'クラウドコンピューティング概要', 1),
(0, 'NFC0314G', 'ビジネスパーソンのためのクラウド入門', 1),
(0, 'NFC0267G', 'クラウドアーキテクト・ファーストステップ', 2),
(0, 'NFC0295G', '実践クラウドデザインパターン', 2),
(0, 'NFC0477G', 'さわってわかるクラウド入門', 1);