#!/usr/bin/env python3
import theme
import views
import auth
from typing import Optional

from fastapi import Request
from fastapi.responses import RedirectResponse
from starlette.middleware.base import BaseHTTPMiddleware

from nicegui import Client, app, ui

app.add_static_files('/static', 'static')

app.add_middleware(auth.AuthMiddleware)

passwords = {'user1': 'pass1', 'user2': 'pass2'}


@ui.page('/')
def index():
    theme.GlobalMenu('dashboard')
    views.adminDash()

@ui.page('/staff')
def staff():
    theme.GlobalMenu('staff')
    views.staffDash()

@ui.page('/doctors')
def doctors():
    theme.GlobalMenu('doctors')
    views.doctorsDash()

@ui.page('/View_doctor/{doctorName}')
def View_doctor(doctorName : str):
    theme.GlobalMenu('doctors')
    views.View_doctorDash(doctorName)

@ui.page('/appointments')
def appointments():
    theme.GlobalMenu('appointments')
    views.appointmentsDash()


@ui.page('/payments')
def appointments():
    theme.GlobalMenu('payments')
    views.paymentsDash()


@ui.page('/View_payment/{paymentId}')
def View_payment(paymentId : int):
    theme.GlobalMenu('payments')
    views.View_payment(paymentId)


@ui.page('/invoices')
def invoices():
    theme.GlobalMenu('invoices')
    views.invoicesDash()

@ui.page('/Create_invoice')
def Create_invoice():
    theme.GlobalMenu('invoices')
    views.Create_invoiceDash()

@ui.page('/View_invoice/{invoiceId}')
def View_invoice(invoiceId : str):
    theme.GlobalMenu('invoices')
    views.View_invoiceDash(invoiceId)

@ui.page('/services')
def services():
    theme.GlobalMenu('services')
    views.servicesDash()

@ui.page('/medicine')
def medicine():
    theme.GlobalMenu('medicine')
    views.medicineDash()

@ui.page('/patients')
def patients():
    theme.GlobalMenu('patients')
    views.patientsDash()

@ui.page('/Create_patient')
def Create_patient():
    theme.GlobalMenu('patients')
    views.Create_patientDash()

@ui.page('/View_patient/{patientid}')
def View_patient(patientid : str):
    theme.GlobalMenu('patients')
    views.View_patientDash(patientid)

@ui.page('/New_MedicalRecord/{patientid}')
def New_MedicalRecord(patientid : str):
    theme.GlobalMenu('patients')
    views.New_MedicalRecord(patientid)

@ui.page('/Edit_MedicalRecord/{patientid}/{recordId}')
def Edit_MedicalRecord(patientid : str,recordId : int):
    theme.GlobalMenu('patients')
    views.Edit_MedicalRecord(patientid,recordId)

@ui.page('/login')
def login() -> Optional[RedirectResponse]:
    def try_login() -> None:  # local function to avoid passing username and password as arguments
        if passwords.get(username.value) == password.value:
            app.storage.user.update({'username': username.value, 'authenticated': True})
            ui.navigate.to(app.storage.user.get('referrer_path', '/'))  # go back to where the user wanted to go
        else:
            ui.notify('Wrong username or password', color='negative')

    if app.storage.user.get('authenticated', False):
        return RedirectResponse('/')
    with ui.card().classes('absolute-center'):
        username = ui.input('Username').on('keydown.enter', try_login)
        password = ui.input('Password', password=True, password_toggle_button=True).on('keydown.enter', try_login)
        ui.button('Log in', on_click=try_login)
    return None


ui.run(storage_secret='THIS_NEEDS_TO_BE_CHANGED')
