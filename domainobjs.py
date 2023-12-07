class Employee:
    def __init__(self, _id, name, created, modified):
        self._id = int(_id)
        self.name = name
        self.created = created
        self.modified = modified
    def __repr__(self):
        return f"Employee #{self._id} Name: {self.username}"

class Task:
    def __init__(self, _id, displayname, description, status, created, modified):
        self._id = int(_id)
        self.displayname = displayname
        self.description = description
        self.status = status
        self.created = created
        self.modified = modified
    def __repr__(self):
        return f"Task #{self._id} \"{self.displayname}\" ({self.status}): {self.description}"
        
class TaskTime:
    def __init__(self, _id, employeeid, taskid, dateworked, hours, created, modified):
        self._id = _id
        self.employeeid = employeeid
        self.taskid = taskid
        self.dateworked = dateworked
        self.hours = hours
        self.created = created
        self.modified = modified
    def __repr__(self):
        return f"TaskTime #{self._id}: EID={self.employeeid}, TID={self.taskid}, DATE={self.dateworked}, HOURS={self.hours}"

class Comment:
    def __init__(self, _id, authorid, taskid, content, created, modified):
        self._id = _id
        self.authorid = authorid
        self.taskid = taskid
        self.content = content
        self.created = created
        self.modified = modified
    def __repr__(self):
        return f"Comment #{self._id}: EID={self.employeeid}, TID={self.taskid}"
    