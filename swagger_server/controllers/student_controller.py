import connexion
import six

from swagger_server.models.student import Student  # noqa: E501
from swagger_server import util

from swagger_server.service import student_service


def add_student(body):  # noqa: E501
    """Add a new student

     # noqa: E501

    :param body: Student object that needs to be added
    :type body: dict | bytes

    :rtype: int
    """
    if connexion.request.is_json:
        body = Student.from_dict(connexion.request.get_json())  # noqa: E501
        # print('default controller body', body)
        if (not body.first_name) or (not body.last_name):
            return "Not content", 405
    # return 'do some magic!'
    return student_service.add_student(body)


def delete_student(student_id):  # noqa: E501
    """Delete student by ID

    Delete a single student # noqa: E501

    :param student_id: ID of student to use
    :type student_id: int

    :rtype: Student
    """
    # return 'do some magic!'
    res = student_service.delete_student(student_id)
    if res:
        return res
    return 'Not Found', 404


def get_student_by_id(student_id, subject=None):  # noqa: E501
    """Find student by ID

    Returns a single student # noqa: E501

    :param student_id: ID of student to return
    :type student_id: int
    :param subject: The subject name
    :type subject: str

    :rtype: Student
    """
    # return 'do some magic!'
    print('id&subject query', student_id, subject, connexion.request, connexion.request.query_string)
    query_string = connexion.request.query_string.decode()
    
    print("id&subject", student_id, subject)
    # res = student_service.get_student_by_id(student_id, subject=subject)
    if subject is None:
        res1 = student_service.get_student_by_id(student_id, subject)
        if res1:
            return res1
    # subject = query_string.split('=')[1]
    # subject = query_string
    res2 = student_service.get_student_by_id_and_subject(student_id, subject)
    if res2:
        return res2
    return 'Not Found', 404

def get_student_by_last_name(last_name=None):  # noqa: E501
    """Find student by last name

    Returns a single student # noqa: E501

    :param last_name: The last name
    :type last_name: str

    :rtype: Student
    """
    # return 'do some magic!'
    print('last name query', last_name, connexion.request, connexion.request.query_string)
    query_string = connexion.request.query_string.decode()
    # last_name = query_string.split('=')[1]
    # last_name = query_string
    print("last name",last_name)
    
    res = student_service.get_student_by_last_name(last_name)
    if res:
        return res
    return 'Not Found', 404
