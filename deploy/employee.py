from dotenv import load_dotenv
import requests
from openpyxl import Workbook
from reportlab.pdfgen import canvas
from pprint import pprint
from io import BytesIO

load_dotenv()

API_URL = "https://reqres.in/api/users"

def get_employee():

    employee_data = requests.get(API_URL)
    users = employee_data.json().get('data', [])

    if not all(isinstance(entry, dict) and all(key in entry for key in ["id", "first_name", "last_name", "email", "avatar"]) for entry in users):
       return redirect(url_for('incorrect_format'))

    return users

def export_to_excel(data):
    excel_buffer = BytesIO()
    wb = Workbook()
    ws = wb.active
    ws.append(['ID', 'First Name', 'Last Name', 'Email', 'Avatar'])

    for user in data:
        if isinstance(user, dict):
           ws.append([user.get('id', ''), user.get('first_name', ''), user.get('last_name', ''),
                     user.get('email', ''), user.get('avatar', '')])
        else:
           print(f"Invalid user data: {user}")

    wb.save(excel_buffer)
    excel_buffer.seek(0)
    return excel_buffer


def export_to_pdf(data):

    pdf_buffer = BytesIO()
    c = canvas.Canvas(pdf_buffer)
    c.drawString(100, 800, "User List")

    for i, user in enumerate(data, start=1):
        c.drawString(100, 800 - i * 20, f"{i}. {user.get('first_name', '')}, {user.get('last_name', '')}, {user.get('email', '')}")

    c.showPage()
    c.save()

    pdf_buffer.seek(0)
    return pdf_buffer


if __name__ == "__main__":
    print('\n*** Get Employee Data ***\n')

    employee_data = get_employee()

    print("\n")
    pprint(employee_data)
