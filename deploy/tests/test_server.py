import unittest
from unittest.mock import patch, MagicMock
from io import BytesIO

from server import app

class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    @patch('server.get_employee')
    def test_index_route(self, mock_get_employee):
        # Mock the get_employee function to return sample data
        mock_get_employee.return_value = [
            {"id": 1, "first_name": "John", "last_name": "Doe", "email": "john@example.com", "avatar": "avatar_url"}
        ]

        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        # Add more assertions based on your template structure and data
        self.assertIn(b'John Doe', response.data)

    @patch('server.get_employee')
    @patch('server.export_to_excel')
    def test_export_excel_route(self, mock_export_to_excel, mock_get_employee):
        mock_get_employee.return_value = [
            {"id": 1, "first_name": "John", "last_name": "Doe", "email": "john@example.com", "avatar": "avatar_url"}
        ]
        mock_export_to_excel.return_value = BytesIO(b'Test Excel Data')

        response = self.app.get('/export?format=excel')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        # Add more assertions based on your actual export function behavior

    @patch('server.get_employee')
    @patch('server.export_to_pdf')
    def test_export_pdf_route(self, mock_export_to_pdf, mock_get_employee):
        mock_get_employee.return_value = [
            {"id": 1, "first_name": "John", "last_name": "Doe", "email": "john@example.com", "avatar": "avatar_url"}
        ]
        mock_export_to_pdf.return_value = BytesIO(b'Test PDF Data')

        response = self.app.get('/export?format=pdf')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/pdf')
        # Add more assertions based on your actual export function behavior

    def test_invalid_format_route(self):
        response = self.app.get('/export?format=invalid_format')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Invalid format')

if __name__ == '__main__':
    unittest.main()

