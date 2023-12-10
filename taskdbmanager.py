import datetime
import os

from dotenv import dotenv_values
import psycopg

from domainobjs import *

class ForumDBManager:
    def __init__(self):
        # Connect to database using the environment variables
        config = {
            **dotenv_values(".env"),  # load shared development variables
            **os.environ  # override loaded values with environment variables
        }

        self.conn = psycopg.connect(autocommit=True,
                        dbname=config.get("POSTGRES_DB"),
                        host=config.get("POSTGRES_HOST"),
                        user=config.get("POSTGRES_USER"),
                        password=config.get("POSTGRES_PASSWORD"),
                        port=config.get("POSTGRES_PORT"))
        
        del config
        
    def insert_employee(self, name):
        """Create and return a new employee in the database"""
        cur = self.conn.cursor()
        cur.execute("INSERT INTO Employees (name) VALUES (%s) RETURNING id, name, created, modified;", (name,))
        return Employee(*cur.fetchone())
    
    def insert_task(self, displayname, description, status):
        """Create and return a new task in the database"""
        cur = self.conn.cursor()
        cur.execute("INSERT INTO Tasks (displayname, description, status) VALUES (%s, %s, (SELECT id FROM STATUS WHERE name=%s)) RETURNING id, displayname, description, status, created, modified;", (displayname, description, status))
        return Task(*cur.fetchone())
    
    def insert_tasktime(self, employee, task, dateworked, hours):
        """Create and return a new tasktime in the database"""
        employeeid = employee._id if isinstance(employee, Employee) else employee
        taskid = task._id if isinstance(task, Task) else task
        if isinstance(dateworked, (tuple,list)) and len(dateworked)==3:
            dateworked = datetime.date(*dateworked)
        elif isinstance(dateworked, str):
            dateworked = datetime.date.fromisoformat(dateworked)
        hours = float(hours)

        cur = self.conn.cursor()
        cur.execute("INSERT INTO TaskTimes (employeeid, taskid, dateworked, hours) VALUES (%s, %s, %s, %s) RETURNING id, employeeid, taskid, dateworked, hours, created, modified;", (employeeid, taskid, dateworked, hours))
        return TaskTime(*cur.fetchone())
    
    def insert_comment(self, author, task, content):
        """Create and return a new comment in the database"""
        authorid = author._id if isinstance(author, Employee) else author
        taskid = task._id if isinstance(task, Task) else task

        cur = self.conn.cursor()
        cur.execute("INSERT INTO Comments (authorid, taskid, content) VALUES (%s, %s, %s) RETURNING id, authorid, taskid, content, created, modified;", (authorid, taskid, content))
        return Comment(*cur.fetchone())
        
    def insert_status(self, name):
        """Create a new status type in the database
        Note: Status records do not have a domain object.
        Returns tuple of (id, name)"""
        cur = self.conn.cursor()
        cur.execute("INSERT INTO Status (name) VALUES (%s) RETURNING id, name;", (name,))
        return cur.fetchone()
    
    def get_employees(self):
        """Return list of all employees"""
        cur = self.conn.cursor()
        cur.execute("SELECT id, name, created, modified FROM Employees;")
        return [Employee(*e) for e in cur.fetchall()]
    
    def get_employee_by_id(self, _id):
        """Return employee specified by _id"""
        cur = self.conn.cursor()
        cur.execute("SELECT id, name, created, modified FROM Employees WHERE id=%s;", (_id,))
        return Employee(*cur.fetchone())
    
    def get_tasks(self):
        """Return list of all tasks"""
        cur = self.conn.cursor()
        cur.execute("SELECT Tasks.id, displayname, description, Status.name, created, modified FROM Tasks JOIN Status ON Tasks.status=Status.id;")
        return [Task(*t) for t in cur.fetchall()]
    
    def get_task_by_id(self, _id):
        """Return task specified by _id"""
        cur = self.conn.cursor()
        cur.execute("SELECT Tasks.id, displayname, description, Status.name, created, modified FROM Tasks JOIN Status ON Tasks.status=Status.id WHERE id=%s;", (_id,))
        return Task(*cur.fetchone())
    
    def search_tasks_by_displayname(self, displayname):
        """Return tasks that with a similar displayname"""
        cur = self.conn.cursor()
        cur.execute("SELECT Tasks.id, displayname, description, Status.name, created, modified FROM Tasks JOIN Status ON Tasks.status=Status.id WHERE displayname LIKE %s;", (f"%{displayname}%",))
        return [Task(*t) for t in cur.fetchall()]
    
    def get_tasks_by_status(self, statusname):
        """Return list of tasks of a certain status"""
        cur = self.conn.cursor()
        cur.execute("SELECT Tasks.id, displayname, description, Status.name, created, modified FROM Tasks JOIN Status ON Tasks.status=Status.id WHERE Status.name=%s;", (statusname,))
        return [Task(*t) for t in cur.fetchall()]
    
    def get_tasktime_by_id(self, _id):
        """Return tasktime specified by _id"""
        cur = self.conn.cursor()
        cur.execute("SELECT id, employeeid, taskid, dateworked, hours, created, modified FROM TaskTimes WHERE id=%s;", (_id,))
        return TaskTime(*cur.fetchone())
    
    def get_tasktimes_by_employee(self, employee):
        """Return list of tasktimes linked to employee"""
        employeeid = employee._id if isinstance(employee, Employee) else employee
        
        cur = self.conn.cursor()
        cur.execute("SELECT id, employeeid, taskid, dateworked, hours, created, modified FROM TaskTimes WHERE employeeid=%s;", (employeeid,))
        return [TaskTime(*tt) for tt in cur.fetchall()]
    
    def get_tasktimes_by_task(self, task):
        """Return list of tasktimes linked to task"""
        taskid = task._id if isinstance(task, Task) else task
        
        cur = self.conn.cursor()
        cur.execute("SELECT id, employeeid, taskid, dateworked, hours, created, modified FROM TaskTimes WHERE taskid=%s;", (taskid,))
        return [TaskTime(*tt) for tt in cur.fetchall()]
    
    def get_tasktimes_by_dateworked(self, dateworked):
        """Return list of tasktimes on dateworked"""
        if isinstance(dateworked, (tuple,list)) and len(dateworked)==3:
            dateworked = datetime.date(*dateworked)
        elif isinstance(dateworked, str):
            dateworked = datetime.date.fromisoformat(dateworked)
        
        cur = self.conn.cursor()
        cur.execute("SELECT id, employeeid, taskid, dateworked, hours, created, modified FROM TaskTimes WHERE dateworked=%s;", (dateworked,))
        return [TaskTime(*tt) for tt in cur.fetchall()]
    
    def get_comment_by_id(self, _id):
        """Return comment specified by _id"""
        cur = self.conn.cursor()
        cur.execute("SELECT id, authorid, taskid, content, created, modified FROM Comments WHERE id=%s;", (_id,))
        return Comment(*cur.fetchone())

    def get_comments_by_author(self, author):
        """Return list of comments written by author"""
        authorid = author._id if isinstance(author, Employee) else author

        cur = self.conn.cursor()
        cur.execute("SELECT id, authorid, taskid, content, created, modified FROM Comments WHERE authorid=%s ORDER BY created;", (authorid,))
        return [Comment(*c) for c in cur.fetchall()]
    
    def get_comments_by_task(self, task):
        """Return list of comments on task"""
        taskid = task._id if isinstance(task, Task) else task

        cur = self.conn.cursor()
        cur.execute("SELECT id, authorid, taskid, content, created, modified FROM Comments WHERE taskid=%s ORDER BY created;", (taskid,))
        return [Comment(*c) for c in cur.fetchall()]
    
    #def get_timetasks_worked_between(self, employee, date1, date2):
    
    def update_employee(self, employee):
        """Update the database with the employee object"""
        cur = self.conn.cursor()
        cur.execute("UPDATE Employees SET name=%s WHERE id=%s RETURNING modified;", (employee.name, employee._id))
        employee.modified = cur.fetchone()[0]
    
    def update_task(self, task):
        """Update the database with the task object"""
        cur = self.conn.cursor()
        cur.execute("UPDATE Tasks SET displayname=%s, description=%s, status=(SELECT id FROM Status WHERE name=%s) WHERE id=%s RETURNING modified;", (task.displayname, task.description, task.status, task._id))
        task.modified = cur.fetchone()[0]
    
    def update_tasktime(self, tasktime):
        """Update the database with the tasktime object"""
        cur = self.conn.cursor()
        cur.execute("UPDATE TaskTimes SET employeeid=%s, taskid=%s, dateworked=%s, hours=%s WHERE id=%s RETURNING modified;", (tasktime.employeeid, tasktime.taskid, tasktime.dateworked, tasktime.hours, tasktime._id))
        tasktime.modified = cur.fetchone()[0]
    
    def update_comment(self, comment):
        """Update the database with the comment object"""
        cur = self.conn.cursor()
        cur.execute("UPDATE Comments SET authorid=%s, taskid=%s, content=%s WHERE id=%s RETURNING modified;", (comment.authorid, comment.taskid, comment.content, comment._id))
        comment.modified = cur.fetchone()[0]
    
    def clear_database(self):
        """Empty the tables. For testing use."""
        cur = self.conn.cursor()
        cur.execute("DELETE FROM Comments")
        cur.execute("DELETE FROM TaskTimes")
        cur.execute("DELETE FROM Tasks")
        cur.execute("DELETE FROM Employees")
        
    def __del__(self):
        self.conn.commit()
        self.conn.close()

