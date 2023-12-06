CREATE TABLE Status (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    UNIQUE(name)
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
    status INTEGER,
    created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(status) REFERENCES Status(id)
);

CREATE TABLE TaskTimes (
    id SERIAL PRIMARY KEY,
    employeeid INTEGER,
    taskid INTEGER,
    hours FLOAT NOT NULL DEFAULT 0.0,
    dateworked DATE DEFAULT CURRENT_DATE,
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


