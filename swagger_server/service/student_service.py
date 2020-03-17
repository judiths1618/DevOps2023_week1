import json
import logging
import os
import tempfile

from tinydb import TinyDB, Query, where
from tinydb.middlewares import CachingMiddleware
from functools import reduce
import uuid

from swagger_server.models import Student

db_dir_path = tempfile.gettempdir()
db_file_path = os.path.join(db_dir_path, "students.json")
student_db = TinyDB(db_file_path)


def add_student(student):
    queries = []
    query = Query()
    queries.append(query.first_name == student.first_name)
    queries.append(query.last_name == student.last_name)
    query = reduce(lambda a, b : a & b , queries)
    res = student_db.search(query)
    if res:
        return 'already exists', 409

    doc_id = student_db.insert(student.to_dict())
    student.student_id = doc_id

    student_db.update(student.to_dict(), doc_ids=[doc_id])
    print("Added a new student. ", student)
    # return student.student_id
    return student


def get_student_by_id(student_id, subject):
    student = student_db.get(where('student_id')==student_id)
    # student = student_db.get(doc_id=int(student_id))  
    print('Find by id', student_id, subject, student)
    if not student:
        return student
    student = Student.from_dict(student)
    if not subject:
        return student
    
    
def get_student_by_id_and_subject(student_id, subject):
    Q = Query()
    student = student_db.get((Q.student_id==student_id) & (Q.grades[subject]))
    print('Find by id& subject', student_id, subject, student)
    if not student: 
        return student

    student = Student.from_dict(student)
    return student
    

def delete_student(student_id):
    student = student_db.get(where('student_id')==student_id)
    # student = student_db.get(doc_id=int(student_id))
    if not student:
        return student
    doc_id = student_db.remove(where('student_id')==student_id)
    return doc_id


def get_student_by_last_name(last_name):
    Q = Query()
    student = student_db.get(Q.last_name==last_name)
    print('by last name', last_name, student)
    if not student: 
        return student

    student = Student.from_dict(student)
    return student