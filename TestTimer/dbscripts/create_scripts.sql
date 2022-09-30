BEGIN;
--
-- Create model exam
--
CREATE TABLE "timer_exam" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(100) NOT NULL, "description" varchar(100) NOT NULL);
--
-- Create model section
--
CREATE TABLE "timer_section" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "section" varchar(100) NOT NULL, "time" integer NOT NULL, "order" integer NOT NULL, "questions" integer NULL, "test_id" bigint NOT NULL REFERENCES "timer_exam" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "timer_section_test_id_88c739cf" ON "timer_section" ("test_id");
COMMIT;