CREATE TABLE Status (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL UNIQUE
);

CREATE TABLE Employees (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Tasks (
    id SERIAL PRIMARY KEY,
    displayname TEXT NOT NULL,
    description TEXT,
    status INTEGER DEFAULT 0,
    created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(status) REFERENCES Status(id)
);

CREATE TABLE TaskTimes (
    id SERIAL PRIMARY KEY,
    employeeid INTEGER,
    taskid INTEGER,
    dateworked DATE DEFAULT CURRENT_DATE,
    hours FLOAT NOT NULL DEFAULT 0.0,
    created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(employeeid) REFERENCES Employees(id),
    FOREIGN KEY(taskid) REFERENCES Tasks(id)
);

CREATE TABLE Comments (
    id SERIAL PRIMARY KEY,
    authorid INTEGER,
    taskid INTEGER,
    content TEXT NOT NULL,
    created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(authorid) REFERENCES Employees(id),
    FOREIGN KEY(taskid) REFERENCES Tasks(id)
);

CREATE OR REPLACE FUNCTION update_modified_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.modified = now();
    RETURN NEW;
END;
$$ language 'plpgsql';

CREATE TRIGGER update_employees_modified AFTER UPDATE ON Employees FOR EACH ROW EXECUTE PROCEDURE update_modified_column();
CREATE TRIGGER update_tasks_modified AFTER UPDATE ON Tasks FOR EACH ROW EXECUTE PROCEDURE update_modified_column();
CREATE TRIGGER update_tasktimes_modified AFTER UPDATE ON TaskTimes FOR EACH ROW EXECUTE PROCEDURE update_modified_column();
CREATE TRIGGER update_comments_modified AFTER UPDATE ON Comments FOR EACH ROW EXECUTE PROCEDURE update_modified_column();

INSERT INTO Status (id, name) VALUES (0, 'TODO');
INSERT INTO Status (id, name) VALUES (1, 'In Progress');
INSERT INTO Status (id, name) VALUES (2, 'Paused');
INSERT INTO Status (id, name) VALUES (3, 'Finished');
INSERT INTO Status (id, name) VALUES (4, 'Canceled');

INSERT INTO Employees (name) VALUES ('Josh');
INSERT INTO Employees (name) VALUES ('Michael');
INSERT INTO Employees (name) VALUES ('William');
INSERT INTO Employees (name) VALUES ('Peter');

INSERT INTO Tasks (displayname, description, status) VALUES ('Do stuff', 'Foo Baz', 1);
INSERT INTO Tasks (displayname, description, status) VALUES ('Verify results', 'We expect a 30% increase in user-satisfaction', 0);
INSERT INTO Tasks (displayname, description, status) VALUES ('Ignore customer complaints', 'We are busy, come again later', 0);
INSERT INTO Tasks (displayname, description, status) VALUES ('Eat lunch', 'Yum Yum', 3);
INSERT INTO Tasks (displayname, description, status) VALUES ('Brainstorm', 'Binky and the brain...', 2);
INSERT INTO Tasks (displayname, description, status) VALUES ('Write Fizzbuzz', 'You know, Fizzbuzz. Divisible by 3,5,15 and that jazz', 4);

