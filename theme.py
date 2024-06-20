from nicegui import ui, app

import views
    


def GlobalMenu(page_name):
    with ui.header().classes(replace='row items-center').style('height:60px').classes('bg-black') as header:
        ui.button(on_click=lambda: left_drawer.toggle(), icon='menu').props('flat color=white')        
        ui.space()
        with ui.button(icon='notifications',color='black').style('height:25px; padding-right:5px; padding-left:5px;margin-right:20px'):
              badge = ui.badge('0', color='green').props('floating')
        with ui.avatar(size = '50px').classes('bg-white').style('margin-right:10px'):
              ui.image('/static/profile_pic.png')
              with ui.menu() as menu:
                 ui.menu_item('Profile')
                 ui.menu_item('Logout', lambda: (app.storage.user.clear(), ui.navigate.to('/login')))

    ui.query('body').classes('bg-grey-2')


    with ui.left_drawer().classes('bg-white') as left_drawer:
        ui.image('/static/logo.webp').classes('w-1/2 self-center')
        
        with ui.button(on_click=lambda:ui.navigate.to('/')).classes('w-full bg-white text-green') as dash_button:
            ui.icon('home').style('margin-right:20px')
            ui.label('Dashboard')
            ui.space()
        with ui.button(on_click=lambda:ui.navigate.to('/patients')).classes('w-full bg-white text-green') as patient_button:
            ui.icon('personal_injury').style('margin-right:20px')
            ui.label('Patients')
            ui.space()
        with ui.button(on_click=lambda:ui.navigate.to('/staff')).classes('w-full bg-white text-green') as staff_button:
            ui.icon('supervisor_account').style('margin-right:20px')
            ui.label('Staff')
            ui.space()
        with ui.button(on_click=lambda:ui.navigate.to('/doctors')).classes('w-full bg-white text-green') as doctors_button:
            ui.icon('supervisor_account').style('margin-right:20px')
            ui.label('Doctors')
            ui.space()
        with ui.button(on_click=lambda:ui.navigate.to('/appointments')).classes('w-full bg-white text-green') as appointments_button:
            ui.icon('auto_stories').style('margin-right:20px')
            ui.label('Appointments')
            ui.space()
        with ui.button(on_click=lambda:ui.navigate.to('/payments')).classes('w-full bg-white text-green') as payments_button:
            ui.icon('payments').style('margin-right:20px')
            ui.label('Paiements')
            ui.space()
        with ui.button(on_click=lambda:ui.navigate.to('/invoices')).classes('w-full bg-white text-green') as invoices_button:
            ui.icon('receipt_long').style('margin-right:20px')
            ui.label('Invoices')
            ui.space()
        with ui.button(on_click=lambda:ui.navigate.to('/services')).classes('w-full bg-white text-green') as services_button:
            ui.icon('medical_services').style('margin-right:20px')
            ui.label('Services')
            ui.space()
        with ui.button(on_click=lambda:ui.navigate.to('/medicine')).classes('w-full bg-white text-green') as medicine_button:
            ui.icon('medication').style('margin-right:20px')
            ui.label('Medecine')
            ui.space()
        if page_name == 'dashboard':
            dash_button.classes(replace='w-full bg-green text-white')
        elif page_name == 'patients':
            patient_button.classes(replace='w-full bg-green text-white')
        elif page_name == 'staff':
            staff_button.classes(replace='w-full bg-green text-white')
        elif page_name == 'doctors':
            doctors_button.classes(replace='w-full bg-green text-white')
        elif page_name == 'appointments':
            appointments_button.classes(replace='w-full bg-green text-white')
        elif page_name == 'payments':
            payments_button.classes(replace='w-full bg-green text-white')
        elif page_name == 'invoices':
            invoices_button.classes(replace='w-full bg-green text-white')
        elif page_name == 'services':
            services_button.classes(replace='w-full bg-green text-white')
        elif page_name == 'medicine':
            medicine_button.classes(replace='w-full bg-green text-white')
            

def PatientMenu(patientid,choice):
            
            with ui.button(on_click=lambda:views.medRecords(patientid)).classes('w-full bg-white text-blue') as medRecords_button:
                ui.icon('home').style('margin-right:20px')
                ui.label('Medical Records')
                ui.space()
            with ui.button(on_click=lambda:views.patientAppointment(patientid)).classes('w-full bg-white text-blue') as patientAppointment_button:
                ui.icon('auto_stories').style('margin-right:20px')
                ui.label('Appointments')
                ui.space()
            with ui.button(on_click=lambda:views.patientInvoice(patientid)).classes('w-full bg-white text-blue') as patientInvoice_button:
                ui.icon('personal_injury').style('margin-right:20px')
                ui.label('Invoices')
                ui.space()
            with ui.button(on_click=lambda:views.patientPayment(patientid)).classes('w-full bg-white text-blue') as patientPayment_button:
                ui.icon('supervisor_account').style('margin-right:20px')
                ui.label('Paiements')
                ui.space()            
            with ui.button(on_click=lambda:views.patientImages(patientid)).classes('w-full bg-white text-blue') as patientImages_button:
                ui.icon('images').style('margin-right:20px;margin-left:10px')
                ui.label('Images')
                ui.space()
            with ui.button(on_click=lambda:views.patientInfo(patientid)).classes('w-full bg-white text-blue') as patientInfo_button:
                ui.icon('account_box').style('margin-right:20px')
                ui.label('Patient Information')
                ui.space()
            with ui.button(on_click=lambda:views.patientHealth(patientid)).classes('w-full bg-white text-blue') as patientHealth_button:
                ui.icon('medical_information').style('margin-right:20px')
                ui.label('Health Information')
                ui.space()
            buttonsdict = {"patientHealth_button":patientHealth_button,"patientInfo_button":patientInfo_button,"medRecords_button":medRecords_button,"patientAppointment_button":patientAppointment_button,"patientInvoice_button":patientInvoice_button,"patientPayment_button":patientPayment_button,"patientImages_button":patientImages_button}
            for i, j in buttonsdict.items():           
                if i == choice:
                   j.classes(replace='w-full bg-blue text-white')
                else:
                    j.classes(replace='w-full bg-white text-blue')

def DoctorMenu(doctorName,choice):
            
            with ui.button(on_click=lambda:views.doctor_personal_info(doctorName)).classes('w-full bg-white text-blue') as doctor_info_button:
                ui.icon('home').style('margin-right:20px')
                ui.label('Personal Information')
                ui.space()
            with ui.button(on_click=lambda:views.doctor_appointments(doctorName)).classes('w-full bg-white text-blue') as patientAppointment_button:
                ui.icon('auto_stories').style('margin-right:20px')
                ui.label('Appointments')
                ui.space()
            with ui.button(on_click=lambda:views.doctor_patients(doctorName)).classes('w-full bg-white text-blue') as patients_button:
                ui.icon('personal_injury').style('margin-right:20px')
                ui.label('Patients')
                ui.space()           
            with ui.button(on_click=lambda:views.doctor_access(doctorName)).classes('w-full bg-white text-blue') as access_button:
                ui.icon('account_box').style('margin-right:20px')
                ui.label('Access Control')
                ui.space()
            with ui.button(on_click=lambda:views.doctor_changePass(doctorName)).classes('w-full bg-white text-blue') as changePass_button:
                ui.icon('medical_information').style('margin-right:20px')
                ui.label('Change Password')
                ui.space()
            buttonsdict = {"doctor_info_button":doctor_info_button,"patientAppointment_button":patientAppointment_button,"patients_button":patients_button,"access_button":access_button,"changePass_button":changePass_button}
            for i, j in buttonsdict.items():           
                if i == choice:
                   j.classes(replace='w-full bg-blue text-white')
                else:
                    j.classes(replace='w-full bg-white text-blue')
