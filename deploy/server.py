from flask import Flask, render_template, request, Response, send_file
from employee import *
from waitress import serve
from dotenv import load_dotenv
import argparse


app = Flask(__name__)

@app.route('/')
def index():
    users = get_employee()
    return render_template('index.html', users=users)


@app.route('/export')
def export_data():
    format_type = request.args.get('format', 'json')
    
    if format_type == 'excel':
        excel_data = get_employee()
        excel_file = export_to_excel(excel_data)
        return send_file(excel_file, as_attachment=True, download_name='users.xlsx')
    elif format_type == 'pdf':
        pdf_data = get_employee()
        pdf_file = export_to_pdf(pdf_data)
        return send_file(pdf_file, as_attachment=True, download_name='users.pdf')
    else:
        return "Invalid format"

@app.route('/incorrect_format')
def incorrect_format():
    return render_template('incorrect_format.html')


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="5000")
