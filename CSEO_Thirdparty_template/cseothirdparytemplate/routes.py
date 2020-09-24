from flask import render_template, url_for, redirect, flash, send_from_directory, request, send_file
import os
from cseothirdparytemplate import app
from cseothirdparytemplate.forms import UploadFile, DownloadFile
import pandas as pd
from cseothirdparytemplate.modal import thirdpartyexcelauto


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    form = UploadFile()
    if form.validate_on_submit():
        data = pd.read_excel(form.file.data)
        path = os.path.join(app.root_path, 'static', 'MAS_Actual_links.xlsx')
        data_mas = pd.read_excel(path)
        thirdpartyexcelauto(data, data_mas)
        app_name = form.app_name.data
        flash(f'File Uploaded Successfully for {form.app_name.data}!', 'success')
        return redirect(url_for('download', app_name=app_name))
    return render_template("home.html", title="Home", form=form)


@app.route('/download/<string:app_name>', methods=['GET', 'POST'])
def download(app_name):
    form = DownloadFile()
    app_name = app_name
    if request.method == 'POST':
        path = os.path.join(app.root_path, 'static/data', 'Data_Updated.xlsx')
        file_name = app_name
        app_path = file_name + "_Updated.xlsx"
        return send_file(path, as_attachment=True, attachment_filename=app_path)
    return render_template("download.html", title="Download", form=form, app_name=app_name)


@app.route('/instructions')
def instructions():
    return render_template("instructions.html", title="Instructions")
