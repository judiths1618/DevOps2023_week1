# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.student import Student  # noqa: E501
from swagger_server.test import BaseTestCase
import names


class TestStudentController(BaseTestCase):
    """StudentController integration test stubs"""

    def test_add_student(self):
        """Test case for add_student

        Add a new student
        """
        body = Student()
        # body.student_id = 2
        body.first_name = names.get_first_name()
        body.last_name = names.get_last_name()
        body.grades = {'The_Mathematics_of_Quantum_Neutrino_Fields': 0, '20th_Century_History': 0}
        response = self.client.open(
            '/service-api/student',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))
        self.assertTrue(response.is_json)
        # self.assertIsInstance(response.json, int)   # 返回学生id
        self.assertIsInstance(response.json, dict)           


    def test_get_student_by_id(self):
        """Test case for get_student_by_id

        Find student by ID
        """
        body = Student()
        # body.student_id = 1
        body.first_name = names.get_first_name()
        body.last_name = names.get_last_name()
        body.grades = {'math': 8, 'history': 9}
        response = self.client.open(
            '/service-api/student',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        student_id = (response.json)['student_id']
        # student_id = (response.json)
        query_string = [('subject','math')]
        # query_string = 'math'
        response = self.client.open(
            '/service-api/student/{student_id}'.format(student_id=student_id),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))
        self.assertTrue(response.is_json)
        self.assertIsInstance(response.json, dict)


    def test_delete_student(self):
        """Test case for delete_student

        Delete student by ID
        """
        body = Student()
        # body.student_id = 1
        body.first_name = names.get_first_name()
        body.last_name = names.get_last_name()
        body.grades = {'math': 8, 'history': 9}
        response = self.client.open(
            '/service-api/student',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        print('lllll', response.json)
        student_id = (response.json)['student_id']    # 学生id
        # student_id = (response.json)
        print('test_student_controller delete id: ', student_id, response.json)
        response = self.client.open(
            '/service-api/student/{student_id}'.format(student_id=student_id),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))
        

    def test_get_student_by_last_name(self):
        """Test case for get_student_by_last_name

        Find student by last name
        """
        body = Student()
        # body.student_id = 1
        body.first_name = names.get_first_name()
        body.last_name = names.get_last_name()
        body.grades = {'Chinese': 8, 'history': 9}
        response = self.client.open(
            '/service-api/student',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        
        query_string = [('last_name', (response.json)['last_name'])] # 学生的last_name
        response = self.client.open(
            '/service-api/student/',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))
        self.assertTrue(response.is_json)
        self.assertIsInstance(response.json, dict)


if __name__ == '__main__':
    import unittest
    unittest.main()
