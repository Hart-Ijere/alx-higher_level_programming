-- Task: Convert hbtn_0c_0 database, first_table, and field name in first_table to UTF8 (utf8mb4, collate utf8mb4_unicode_ci)

-- This scriptConverts the database hbtn_0c_0 to UTF8
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Convert the table first_table to UTF8
ALTER TABLE hbtn_0c_0.first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Convert the field name in first_table to UTF8
ALTER TABLE hbtn_0c_0.first_table CHANGE name name VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
