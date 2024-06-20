import theme
import models
from datetime import date
from fullcalendar import FullCalendar as fullcalendar
import base64
from nicegui import events, ui


def adminDash():
    with ui.row().classes('w-full'):
        with ui.card().style('width:23%'):
            with ui.row().classes('w-full'):
                ui.icon('personal_injury').classes('text-h5 text-green')
                ui.label('Total Patients :').classes('text-h6 text-black')
                ui.space()
            with ui.row().classes('w-full'):
                ui.label('1345').classes('text-h6 text-black font-bold')
                ui.space()
                ui.label('+12%').classes('text-h6 text-green font-bold')
        with ui.card().style('width:25%'):
            with ui.row().classes('w-full'):
                ui.icon('auto_stories').classes('text-h5 text-green')
                ui.label('Appointments :').classes('text-h6 text-black')
                ui.space()
            with ui.row().classes('w-full'):
                ui.label('375').classes('text-h6 text-black font-bold')
                ui.space()
                ui.label('-32%').classes('text-h6 text-red font-bold')
        with ui.card().style('width:23%'):
            with ui.row().classes('w-full'):
                ui.icon('medication').classes('text-h5 text-green')
                ui.label('Prescriptions :').classes('text-h6 text-black')
                ui.space()
            with ui.row().classes('w-full'):
                ui.label('45').classes('text-h6 text-black font-bold')
                ui.space()
                ui.label('+15%').classes('text-h6 text-green font-bold')
        with ui.card().style('width:23%'):
            with ui.row().classes('w-full'):
                ui.icon('payments').classes('text-h5 text-green')
                ui.label('Total Earnings :').classes('text-h6 text-black')
                ui.space()
            with ui.row().classes('w-full'):
                ui.label('133').classes('text-h6 text-black font-bold')
                ui.space()
                ui.label('-26%').classes('text-h6 text-red font-bold')
    with ui.row().classes('w-full'):
        with ui.column().style('width:74%'):
            with ui.card().classes('w-full'):
                ui.label('Total Earnings :').classes('text-h6 text-black')
                ui.echart({
                    'xAxis': {'type': 'category'},
                    'yAxis': {'axisLabel': {':formatter': 'value => "$" + value'}},
                    'series': [{'type': 'line',
                                'data': [5, 8, 13, 21, 34, 55, 44, 38, 46, 63, 53, 77, 89, 133, 98, 88, 133, 154]}],
                }).classes('w-full').style('height:400px')
        with ui.column().style('width:23%'):
            with ui.card().classes('w-full').style('height:480px'):
                ui.label('Recent Patients :').classes('text-h6 text-black')
                with ui.row().classes('w-full'):
                    with ui.avatar():
                        ui.image('/static/med.jpeg')
                    with ui.column().classes('gap-0'):
                        ui.label('Mohammed Youss').style('padding-bottom:0px').classes('text-h7 text-black')
                        ui.label('+212-681990152').style('padding-top:0px').classes('text-h7 text-grey')
                ui.separator()
                with ui.row().classes('w-full'):
                    with ui.avatar():
                        ui.image('/static/kawtar.jpeg')
                    with ui.column().classes('gap-0'):
                        ui.label('Kaoutar Charifi').style('padding-bottom:0px').classes('text-h7 text-black')
                        ui.label('+212-681990152').style('padding-top:0px').classes('text-h7 text-grey')
                ui.separator()
                with ui.row().classes('w-full'):
                    with ui.avatar():
                        ui.image('/static/ftouhi.jpeg')
                    with ui.column().classes('gap-0'):
                        ui.label('Fatouhi Meryam').style('padding-bottom:0px').classes('text-h7 text-black')
                        ui.label('+212-681990152').style('padding-top:0px').classes('text-h7 text-grey')
                ui.separator()
                with ui.row().classes('w-full'):
                    with ui.avatar():
                        ui.image('/static/wissal.jpeg')
                    with ui.column().classes('gap-0'):
                        ui.label('Wissal Razouki').style('padding-bottom:0px').classes('text-h7 text-black')
                        ui.label('+212-681990152').style('padding-top:0px').classes('text-h7 text-grey')
                ui.separator()
                with ui.row().classes('w-full'):
                    with ui.avatar():
                        ui.image('/static/rachid.jpeg')
                    with ui.column().classes('gap-0'):
                        ui.label('RAchid Daoudi').style('padding-bottom:0px').classes('text-h7 text-black')
                        ui.label('+212-681990152').style('padding-top:0px').classes('text-h7 text-grey')

    with ui.row().classes('w-full'):
        with ui.column().style('width:74%'):
            with ui.card().classes('w-full').style('height:480px'):
                ui.label('Recent Transactions :').classes('text-h6 text-black')
                with ui.grid(columns='auto 2fr 1fr 1fr 1fr 1fr').classes('w-full gap-0'):
                    for _ in range(1):
                        ui.label('#').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                        ui.label('Patient').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                        ui.label('Date').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                        ui.label('Status').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                        ui.label('Amount').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                        ui.label('Method').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                    for i in range(6):
                        ui.label(f'{i}').classes('font-bold').style('margin-top:15px;margin-bottom:5px')
                        with ui.row().classes('w-full'):
                            with ui.avatar().style('margin-top:5px;margin-bottom:5px'):
                                ui.image('/static/kawtar.jpeg')
                            with ui.column().classes('gap-0'):
                                ui.label('Kaoutar Charifi').style('padding-bottom:0px').classes(
                                    'text-h7 text-black').style('margin-top:5px')
                                ui.label('+212-681990152').style('padding-top:0px').classes('text-h7 text-grey')
                        ui.label('12/05/2023').classes('font-bold').style('text-align:center').style(
                            'margin-top:15px;margin-bottom:5px')
                        ui.label('paid').classes('text-green font-bold').style('text-align:center').style(
                            'margin-top:15px;margin-bottom:5px')
                        ui.label('1200 dh').classes('font-bold').style('text-align:center').style(
                            'margin-top:15px;margin-bottom:5px')
                        ui.label('Cash').classes('font-bold').style('text-align:center').style(
                            'margin-top:15px;margin-bottom:5px')

        with ui.column().style('width:23%'):
            with ui.card().classes('w-full').style('height:480px'):
                ui.label('Appointments :').classes('text-h6 text-black')
                ui.separator()
                with ui.timeline(side='right', layout='loose'):
                    ui.timeline_entry(subtitle='13:30',
                                      title='Kaoutar Charifi',
                                      avatar='/static/kawtar.jpeg')
                    ui.timeline_entry(title='Fatouhi Meryam',
                                      subtitle='15:30',
                                      avatar='/static/ftouhi.jpeg')
                    ui.timeline_entry(title='Mohamed Youss',
                                      subtitle='16:30',
                                      avatar='/static/med.jpeg')
                    ui.timeline_entry(title='Rachid Daoudi',
                                      subtitle='17:30',
                                      avatar='/static/rachid.jpeg')


def patientAppointment(patientid):
    patients = models.readallPatients()
    patients_list = []
    patients_dic = {}
    for patient in patients:
        patients_list.append(patient.nomPatient)
        patients_dic[patient.nomPatient] = patient.id
        patients_dic[patient.id] = patient.nomPatient
    doctors = models.readallDoctors()
    doctors_list = []
    doctors_dic = {}
    for doctor in doctors:
        doctors_list.append(doctor.nom)
        doctors_dic[doctor.id] = doctor.nom
    medRecordsCard.clear()
    menuButtons.clear()
    with menuButtons:
        theme.PatientMenu(patientid, "patientAppointment_button")

    def show_appointment(appointmentId):
        appointment_record = models.readOneAppointment(appointmentId)

        with ui.dialog().classes('w-full') as view_appointment, ui.card().classes('w-full'):
            ui.label('View/Edit Appointment').classes('text-h5 text-black font-bold')
            ui.separator()
            ui.label('Patient Name').classes('text-h6 text-black')
            a_view = ui.input().style('width:100%').classes(
                'bg-white').props('outlined')
            a_view.value = patients_dic.get(appointment_record.patientId)
            ui.label('Purpose of visit').classes('text-h6 text-black')
            b_view = ui.input().style('width:100%').classes('bg-white').props(
                'outlined')
            b_view.value = appointment_record.butVisite
            ui.label('Date of Visit').classes('text-h6 text-black')
            with ui.input('Date of Visit', on_change=lambda: menu.close()).style('width:100%').props(
                    'outlined') as date1_view:
                with date1_view.add_slot('append'):
                    ui.icon('edit_calendar').on('click', lambda: menu.open()).classes('cursor-pointer')
                with ui.menu() as menu:
                    ui.date().bind_value(date1_view)
            date1_view.value = appointment_record.dateVisite
            with ui.row().classes('w-full'):
                with ui.column().style('width:48%'):
                    ui.label('Start Time').classes('text-h6 text-black')
                    d_view = ui.input().style('width:100%').classes('bg-white').props('outlined')
                    d_view.value = appointment_record.heurDebut
                with ui.column().style('width:48%'):
                    ui.label('End Time').classes('text-h6 text-black')
                    f_view = ui.input().style('width:100%').classes('bg-white').props('outlined')
                    f_view.value = appointment_record.heurFin
            with ui.row().classes('w-full'):
                with ui.column().style('width:48%'):
                    ui.label('Assigned Doctor').classes('text-h6 text-black')
                    docs_view = ui.input().style('width:100%').classes(
                        'bg-white').props('outlined')
                    docs_view.value = doctors_dic.get(appointment_record.doctorId)
                with ui.column().style('width:48%'):
                    ui.label('Appointment Status').classes('text-h6 text-black')
                    h_view = ui.select(["Pending", "Canceled", "Accepted"], value="Accepted").style(
                        'width:100%').classes(
                        'bg-white').props('outlined')
                    h_view.value = appointment_record.statut
            ui.label('Available Rooms').classes('text-h6 text-black ')
            i_view = ui.select(["Room A12", "Room B4"], value="Room A12").style('width:100%').classes('bg-white').props(
                'outlined')
            i_view.value = appointment_record.chambre
            ui.label('Description').classes('text-h6 text-black ')
            j_view = ui.textarea().classes('w-full').props('outlined')
            j_view.value = appointment_record.description
            ui.button('Save Appointment', icon='save', color='green',
                      on_click=lambda: models.editAppointment(appointmentId, date1_view.value, d_view.value,
                                                              h_view.value, i_view.value, j_view.value, b_view.value,
                                                              f_view.value)).classes('w-full text-white')
        view_appointment.open()
    with medRecordsCard:
        with ui.row().classes('w-full'):
            ui.label('Appointments').classes('text-h6 text-black')
            ui.space()
        appointments = models.readAllAppointmentsById(patientid)
        with ui.grid(columns='auto 1fr 1fr 1fr 1fr auto').classes('w-full gap-0'):
            for _ in range(1):
                ui.label('Id').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                ui.label('Date').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                ui.label('Doctor').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                ui.label('Status').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                ui.label('Time').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                ui.label('Action').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
            for appointment in appointments:
                    ui.label(f'{appointment.id}').classes('font-bold').style('margin-top:15px;margin-bottom:5px')
                    ui.label(f'{appointment.dateVisite}').classes('font-bold').style('text-align:center').style('margin-top:15px;margin-bottom:5px')
                    ui.label(f'{appointment.doctorId}').classes('font-bold').style('text-align:center').style('margin-top:15px;margin-bottom:5px')
                    ui.label(f'{appointment.statut}').classes('font-bold').style('text-align:center').style('margin-top:15px;margin-bottom:5px')
                    ui.label(f'{appointment.heurDebut}').classes('font-bold').style('text-align:center').style('margin-top:15px;margin-bottom:5px')
                    ui.button(icon='visibility', color='white', on_click=lambda appointment=appointment: show_appointment(appointment.id)).classes('font-bold text-green w-1/2').style('margin-top:5px;margin-bottom:5px;margin-left:20px')


def patientInvoice(patientid):
    medRecordsCard.clear()
    menuButtons.clear()
    with menuButtons:
        theme.PatientMenu(patientid, "patientInvoice_button")
    with medRecordsCard:
        with ui.row().classes('w-full'):
            ui.label('Invoices').classes('text-h6 text-black')
            ui.space()
        invoices = models.readAllInvoicesById(patientid)
        with ui.grid(columns='1fr 1fr 1fr 1fr auto').classes('w-full gap-0'):
            for _ in range(1):
                ui.label('Invoice ID').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                ui.label('Created Date').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                ui.label('Due Date').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                ui.label('Notes').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                ui.label('Action').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
            for invoice in invoices:
                ui.label(f'{invoice.id}').classes('text-black').style('text-align:center').style('margin-top:15px;margin-bottom:5px')
                ui.label(f'{invoice.createddate}').style('text-align:center').style('margin-top:15px;margin-bottom:5px')
                ui.label(f'{invoice.duedate}').classes('text-orange').style('text-align:center').style('margin-top:15px;margin-bottom:5px')
                ui.label(f'{invoice.notes[:4]}...').style('text-align:center').style('margin-top:15px;margin-bottom:5px')
                ui.button(icon='visibility', color='white',on_click=lambda:ui.navigate.to(f'/View_invoice/{invoice.id}')).classes('font-bold text-green w-1/2').style('margin-top:5px;margin-bottom:5px;margin-left:20px')


def patientPayment(patientid):
    medRecordsCard.clear()
    menuButtons.clear()
    with menuButtons:
        theme.PatientMenu(patientid, "patientPayment_button")
    with medRecordsCard:
        with ui.row().classes('w-full'):
            ui.label('Payments ').classes('text-h6 text-black')
            ui.space()
        payments = models.readAllPaymentsById(patientid)
        with ui.grid(columns='auto 1fr 1fr 1fr 1fr auto').classes('w-full gap-0'):
            for _ in range(1):
                ui.label('Id').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                ui.label('Date').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                ui.label('Status').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                ui.label('Amount').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                ui.label('Method').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                ui.label('Action').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
            for payment in payments:
                ui.label(f'{payment.id}').classes('text-black').style('text-align:center').style(
                    'margin-top:15px;margin-bottom:5px')
                ui.label(f'{payment.createddate}').classes('text-black').style('text-align:center').style(
                    'margin-top:15px;margin-bottom:5px')
                ui.label(f'{payment.statut}').style('text-align:center').style('margin-top:15px;margin-bottom:5px').classes(
                    'text-green')
                ui.label(f'{payment.amount} dh').classes('text-orange').style('text-align:center').style(
                    'margin-top:15px;margin-bottom:5px')
                ui.label(f'{payment.methode}').style('text-align:center').style('margin-top:15px;margin-bottom:5px')
                ui.button(icon='visibility', color='white',on_click=lambda payment = payment :ui.navigate.to(f'/View_payment/{payment.id}')).classes('font-bold text-green w-1/2').style(
                    'margin-top:5px;margin-bottom:5px;margin-left:20px')


def patientImages(patientid):
    medRecordsCard.clear()
    menuButtons.clear()
    with menuButtons:
        theme.PatientMenu(patientid, "patientImages_button")
    def uploadfile(e):
        filename = e.name
        data64 = base64.b64encode(e.content.read())
        with open(f'static/{filename}', 'wb') as f:
            f.write(base64.b64decode(data64))
            models.newPatientfile(patientid, filename)
            ui.notify('l`image à été bien enregistré')
        uploadElement.reset()
        patientImages(patientid)
    with medRecordsCard:
        with ui.row().classes('w-full'):
            ui.label('Patient Images').classes('text-h6 text-black')
            ui.space()
        files = models.readallPatientFiles(patientid)
        def showImageFunc(nomFichier):
            with ui.dialog() as showImage, ui.card().classes('w-full'):
                ui.image(f'/static/{nomFichier}')
                with ui.row().classes('w-full'):
                    ui.button('Download', on_click=lambda nomFichier=nomFichier: ui.download(f'/static/{nomFichier}'))
                    ui.button('delete', on_click=lambda: models.deletePatientfile(nomFichier)).props('color="red"')
            showImage.open()
        with ui.grid(columns='1fr 1fr 1fr 1fr').classes('w-full gap-10'):
            for file in files:
                ui.image(f'/static/{file.nomFichier}').on('click', lambda file=file: showImageFunc(file.nomFichier))
        uploadElement = ui.upload(on_upload=lambda e: uploadfile(e)).classes('bg-white').style('width:100%').props(
            'color="black"')



def patientInfo(patientid):
    medRecordsCard.clear()
    menuButtons.clear()
    with menuButtons:
        theme.PatientMenu(patientid, "patientInfo_button")
    with medRecordsCard:
        with ui.row().classes('w-full'):
            ui.label('Patient Information').classes('text-h5 text-black font-bold')
        ui.label('Photo de Profil :').classes('text-h6 text-black')
        ui.upload(on_upload=lambda e: ui.notify(f'Uploaded {e.name}')).classes('bg-white').style('width:100%').props(
            'color="green"')
        with ui.column().style('width:98%'):
            ui.label('Nom et Prénom :').classes('text-h6 text-black')
            ui.input().classes('w-full').props('outlined')
            ui.label('Numéro de Téléphone :').classes('text-h6 text-black')
            ui.input().classes('w-full').props('outlined')
            ui.label('Email :').classes('text-h6 text-black')
            ui.input().classes('w-full').props('outlined')
        with ui.row().classes('w-full'):
            with ui.column().style('width:48%'):
                ui.label('Sexe :').classes('text-h6 text-black')
                select3 = ui.select(["Home", "Femme"], value="Femme").style('width:100%').classes('bg-white').props(
                    'outlined')
            with ui.column().style('width:48%'):
                ui.label('Emergency Contact :').classes('text-h6 text-black')
                ui.input().classes('w-full').props('outlined').style('width:100%')
        with ui.row().classes('w-full'):
            with ui.column().style('width:48%'):
                ui.label('Date de Naissence :').classes('text-h6 text-black')
                with ui.input('Date de Naissence', on_change=lambda: menu.close()).style('width:100%').props(
                        'outlined') as date1:
                    with date1.add_slot('append'):
                        ui.icon('edit_calendar').on('click', lambda: menu.open()).classes('cursor-pointer')
                    with ui.menu() as menu:
                        ui.date().bind_value(date1)
            with ui.column().style('width:48%'):
                ui.label('Adresse :').classes('text-h6 text-black')
                ui.input().classes('w-full').props('outlined').style('width:100%')
        with ui.row().classes('w-full'):
            ui.button('Delete Account', icon='delete', color='green').style('width:48%').classes('text-white')
            ui.button('Save Changes', icon='save', color='green').classes('text-white').style('width:48%')


def patientHealth(patientid):
    medRecordsCard.clear()
    menuButtons.clear()
    with menuButtons:
        theme.PatientMenu(patientid, "patientHealth_button")
    with medRecordsCard:
        with ui.row().classes('w-full'):
            ui.label('Patient Health Information').classes('text-h5 text-black font-bold')
        with ui.column().style('width:98%'):
            blood_type = ["A+", "B+"]
            ui.label('Blood Group :').classes('text-h6 text-black')
            ui.select(options=blood_type, value="Blood Type ...").classes('w-full').props('outlined')
            ui.label('Weight :').classes('text-h6 text-black')
            ui.input().classes('w-full').props('outlined')
            ui.label('Height :').classes('text-h6 text-black')
            ui.input().classes('w-full').props('outlined')
        with ui.row().classes('w-full'):
            with ui.column().style('width:48%'):
                ui.label('Allergies :').classes('text-h6 text-black')
                ui.input().style('width:100%').classes('bg-white').props('outlined')
            with ui.column().style('width:48%'):
                ui.label('Habits :').classes('text-h6 text-black')
                ui.input().classes('w-full').props('outlined').style('width:100%')
        with ui.row().classes('w-full'):
            ui.label('Medical History :').classes('text-h6 text-black')
            ui.input().classes('w-full').props('outlined').style('width:100%')

        with ui.row().classes('w-full'):
            ui.button('Save Changes', icon='save', color='green').classes('text-white').style('width:48%')


def viewRecordDialogFun(recordId):
    record = models.readOneMedicalRecord(recordId)
    treatments = models.readallPatientsServices(recordId)
    medicines = models.readallPatientsMedicines(recordId)
    with ui.dialog() as viewRecordDialog, ui.card().classes('w-full'):
        with ui.card().style('width:100%'):
            ui.label('Docteur').classes('text-h6 text-black font-bold')
            docteur = ui.input().style('width:100%').classes('bg-white').props('outlined')
            docteur.value = record.nomDocteur
            ui.label('Complains').classes('text-h6 text-black font-bold')
            Complains = ui.textarea().classes('w-full').props('outlined')
            Complains.value = record.plaintes
            ui.label('Diagnosis').classes('text-h6 text-black font-bold')
            diagnosis = ui.textarea().classes('w-full').props('outlined')
            diagnosis.value = record.diagnostic
            ui.label('Vital Signs').classes('text-h6 text-black font-bold')
            vitals = ui.textarea().classes('w-full').props('outlined')
            vitals.value = record.signesVitaux
            ui.label('Treatment').classes('text-h6 text-black font-bold')
            with ui.grid(columns='2fr  1fr').classes('w-full gap-0'):
                for _ in range(1):
                    ui.label('Nom de traitement ').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                    ui.label('Prix').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                for j in treatments:
                    ui.label(f'{j.nomService}').classes('text-green font-bold').style('text-align:center').style(
                        'margin-top:15px;margin-bottom:5px')
                    ui.label(f'{j.prixService}').classes('font-bold').style('text-align:center').style(
                        'margin-top:15px;margin-bottom:5px')
            ui.label('Medicine :').classes('text-h6 text-black font-bold')
            with ui.grid(columns='2fr 1fr auto 1fr 1fr 1fr').classes('w-full gap-0'):
                for _ in range(1):
                    ui.label('Nom de médicament').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                    ui.label('Prix').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                    ui.label('Dosage').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                    ui.label('Instructions').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                    ui.label('Quantité').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                    ui.label('Montant').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                for i in medicines:
                    ui.label(f'{i.nomMedicin}').classes('text-green font-bold').style('text-align:center').style(
                        'margin-top:15px;margin-bottom:5px')
                    ui.label(f'{i.prix}').classes('font-bold').style('text-align:center').style(
                        'margin-top:15px;margin-bottom:5px')
                    ui.label(f'{i.dosage}').classes('text-green font-bold').style('text-align:center').style(
                        'margin-top:15px;margin-bottom:5px')
                    ui.label(f'{i.instructions}').classes('font-bold').style('text-align:center').style(
                        'margin-top:15px;margin-bottom:5px')
                    ui.label(f'{i.quantity}').classes('text-green font-bold').style('text-align:center').style(
                        'margin-top:15px;margin-bottom:5px')
                    ui.label(f'{i.prix * i.quantity}').classes('font-bold').style('text-align:center').style(
                        'margin-top:15px;margin-bottom:5px')
            ui.label('Attachments :').classes('text-h6 text-black font-bold')
            recordFiles = models.readallPatientsAttachments(recordId)
            with ui.grid(columns=4).classes('w-full gap-5') as filesGrid:
                for file in recordFiles:
                    with ui.column():
                        ui.image(f'/static/patientfiles.png').on('click', lambda: ui.download(
                            f'/static/{file.nomFichier}')).classes('w-20')
                        ui.label(f'{file.nomFichier}')
    viewRecordDialog.open()


def medRecords(patientid):
    records = models.readallMedicalRecord(patientid)

    medRecordsCard.clear()
    menuButtons.clear()
    with menuButtons:
        theme.PatientMenu(patientid, "medRecords_button")
    with medRecordsCard:
        with ui.row().classes('w-full'):
            ui.label('Medical Record').classes('text-h6 text-black')
            ui.space()
            ui.button('New Record +', color='green',
                      on_click=lambda: ui.navigate.to(f'/New_MedicalRecord/{patientid}')).classes('text-white')
        for i in records:
            treatmentText = ''
            treatments = models.readallPatientsServices(i.id)
            medicines = models.readallPatientsMedicines(i.id)
            amount = 0
            for j in medicines:
                amount += j.prix * j.quantity
            for k in treatments:
                treatmentText = treatmentText + f' {k.nomService}'
                amount += k.prixService
            with ui.card().classes('w-full bg-blue-1'):
                with ui.row().classes('w-full'):
                    ui.label(f'{i.dateCreation}').classes('text-h8 text-black font-bold w-24')
                    with ui.column().classes('w-64'):
                        with ui.row().classes('w-full'):
                            ui.label('Complaint :').classes('text-h8 text-black font-bold')
                            ui.label(f'{i.plaintes[0:15]} ...').classes('text-h8 text-black')
                        with ui.row().classes('w-full'):
                            ui.label('Diagnosis :').classes('text-h8 text-black font-bold')
                            ui.label(f'{i.diagnostic[0:15]} ...').classes('text-h8 text-black')
                        with ui.row().classes('w-full'):
                            ui.label('Treatement :').classes('text-h8 text-black font-bold')
                            ui.label(f'{treatmentText[0:15]} ...').classes('text-h8 text-black')

                    ui.space()
                    ui.label(f'{amount} dh').classes('text-h8 text-green font-bold w-24')
                    ui.space()
                    with ui.column().classes('w-24'):
                        ui.button(icon='visibility', color='white',
                                  on_click=lambda i=i: viewRecordDialogFun(i.refNumber)).classes('text-green')
                        ui.button(icon='edit', color='white', on_click=lambda i=i, patientid=patientid: ui.navigate.to(
                            f'/Edit_MedicalRecord/{patientid}/{i.refNumber}')).classes('text-green')
                        ui.button(icon='delete', color='white').classes('text-red')


def View_patientDash(patientid):
    patient = models.readOnePatient(patientid)
    if patient is None:
        ui.notify(f"Patient '{patientid}' not found.", type="negative")
        ui.navigate.back()
        # Optional: Navigate to a default page or back to the patient list
        return
    global medRecordsCard, menuButtons, viewRecordDialog
    with ui.row().classes('w-full'):
        ui.button(icon='arrow_back', color='white', on_click=lambda: ui.navigate.back()).classes('text-black')
        ui.label(f'{patient.nomPatient}').classes('text-h5 text-black font-bold')
    with ui.row().classes('w-full'):
        with ui.card().style('width:32%;align-items:center'):
            with ui.avatar(size='150px'):
                ui.image(f'/static/{patient.photoProfil}')
            ui.label(f'{patient.nomPatient}').classes('text-h6 text-black font-bold')
            ui.label(f'{patient.email}').classes('text-h6 text-grey')
            ui.label(f'{patient.numTel}').classes('text-h6 text-black font-bold')
            with ui.column().classes('w-full') as menuButtons:
                theme.PatientMenu(patientid, "medRecords_button")

        with ui.card().style('width:66%') as medRecordsCard:
            medRecords(patientid)


def doctor_changePass(doctorName):
    doctorinfoCard.clear()
    doctormenuButtons.clear()
    with doctormenuButtons:
        theme.DoctorMenu(doctorName, "changePass_button")
    with doctorinfoCard:
        ui.label('Old Password').classes('text-h6 text-black font-bold')
        ui.input(password=True).classes('w-full').props('outlined')
        ui.label('New Password').classes('text-h6 text-black font-bold')
        ui.input(password=True).classes('w-full').props('outlined')
        ui.label('Confirm New Password').classes('text-h6 text-black font-bold')
        ui.input(password=True).classes('w-full').props('outlined')
        ui.button('Save Doctor', icon='save', color='green').classes('w-full text-white')


def doctor_access(doctorName):
    doctorinfoCard.clear()
    doctormenuButtons.clear()
    with doctormenuButtons:
        theme.DoctorMenu(doctorName, "access_button")
    with doctorinfoCard:
        ui.label('Permissions & Access :').classes('text-h6 text-black font-bold')
        with ui.grid(columns='2fr 1fr 1fr 1fr 1fr').classes('w-full gap-0'):
            for _ in range(1):
                ui.label('').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                ui.label('Read').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                ui.label('Edit').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                ui.label('Create').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                ui.label('Delete').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
            for i in range(1):
                ui.label('Patient').classes('text-green font-bold').style('text-align:center').style(
                    'margin-top:15px;margin-bottom:5px')
                ui.checkbox().style('margin-left:20px')
                ui.checkbox().style('margin-left:20px')
                ui.checkbox().style('margin-left:20px')
                ui.checkbox().style('margin-left:20px')
            for i in range(1):
                ui.label('Invoices').classes('text-green font-bold').style('text-align:center').style(
                    'margin-top:15px;margin-bottom:5px')
                ui.checkbox().style('margin-left:20px')
                ui.checkbox().style('margin-left:20px')
                ui.checkbox().style('margin-left:20px')
                ui.checkbox().style('margin-left:20px')
            for i in range(1):
                ui.label('Appointment').classes('text-green font-bold').style('text-align:center').style(
                    'margin-top:15px;margin-bottom:5px')
                ui.checkbox().style('margin-left:20px')
                ui.checkbox().style('margin-left:20px')
                ui.checkbox().style('margin-left:20px')
                ui.checkbox().style('margin-left:20px')
            for i in range(1):
                ui.label('Payments').classes('text-green font-bold').style('text-align:center').style(
                    'margin-top:15px;margin-bottom:5px')
                ui.checkbox().style('margin-left:20px')
                ui.checkbox().style('margin-left:20px')
                ui.checkbox().style('margin-left:20px')
                ui.checkbox().style('margin-left:20px')
        ui.button('Save Doctor', icon='save', color='green').classes('w-full text-white')


def doctor_patients(doctorName):
    doctorinfoCard.clear()
    doctormenuButtons.clear()
    with doctormenuButtons:
        theme.DoctorMenu(doctorName, "patients_button")
    with doctorinfoCard:
        with ui.row().classes('w-full'):
            ui.input('Nom du Patient').style('width:25%').classes('bg-grey-1')
            select2 = ui.select(["Home", "Femme", "Tous"], value="Femme").style('width:18%').classes('bg-grey-1')
            with ui.input('Date', on_change=lambda: menu.close()).style('width:18%').classes('bg-grey-1') as date:
                with date.add_slot('append'):
                    ui.icon('edit_calendar').on('click', lambda: menu.open()).classes('cursor-pointer')
                with ui.menu() as menu:
                    ui.date().bind_value(date)
            ui.button(icon='search', color='green-6').style('width:18%;height:55px').classes('text-white')

        with ui.grid(columns='auto 2fr 1fr 1fr 1fr 1fr auto').classes('w-full gap-0'):
            for _ in range(1):
                ui.label('#').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                ui.label('Patient').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                ui.label('Created at').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                ui.label('Gender').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                ui.label('Blood Group').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                ui.label('Age').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                ui.label('Actions').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
            for i in range(6):
                ui.label(f'{i}').classes('font-bold').style('margin-top:15px;margin-bottom:5px')
                with ui.column().classes('gap-0'):
                    nom = ui.label('Kaoutar Charifi').style('padding-bottom:0px').classes('text-h7 text-black').style(
                        'margin-top:5px')
                    ui.label('+212-681990152').style('padding-top:0px').classes('text-h7 text-grey')
                ui.label('12/05/2023').classes('font-bold').style('text-align:center').style(
                    'margin-top:15px;margin-bottom:5px')
                ui.label('Femme').classes('text-green font-bold').style('text-align:center').style(
                    'margin-top:15px;margin-bottom:5px')
                ui.label('A+').classes('font-bold').style('text-align:center').style(
                    'margin-top:15px;margin-bottom:5px')
                ui.label('32').classes('font-bold').style('text-align:center').style(
                    'margin-top:15px;margin-bottom:5px')
                #ui.button(icon='edit').classes('font-bold bg-grey-2 text-black w-5/6').style('margin-top:15px;margin-bottom:5px')
                with ui.expansion(icon='edit').classes('font-bold bg-white text-black w-full').style(
                        'margin-top:15px;margin-bottom:5px'):
                    with ui.row().classes('w-full'):
                        ui.button('Voir', icon='visibility', color='green',
                                  on_click=lambda: ui.navigate.to(f'/View_patient/{nom.text}')).classes('text-white')
                        ui.button('Supprimer', icon='delete', color='green').classes('text-white')


def doctor_appointments(doctorName):
    doctorinfoCard.clear()
    doctormenuButtons.clear()
    with doctormenuButtons:
        theme.DoctorMenu(doctorName, "patientAppointment_button")
    with doctorinfoCard:
        with ui.row().classes('w-full'):
            ui.label('Appointments').classes('text-h6 text-black')
            ui.space()
        with ui.grid(columns='1fr 1fr 1fr 1fr auto').classes('w-full gap-0'):
            for _ in range(1):
                ui.label('Date').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                ui.label('Patient').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                ui.label('Status').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                ui.label('Time').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                ui.label('Action').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
            for i in range(5):
                ui.label('Jun 12, 2021').classes('text-black').style('text-align:center').style(
                    'margin-top:15px;margin-bottom:5px')
                ui.label('Hugo Lloris').style('text-align:center').style('margin-top:15px;margin-bottom:5px')
                ui.label('Pending').classes('text-orange').style('text-align:center').style(
                    'margin-top:15px;margin-bottom:5px')
                ui.label('10:00 AM - 12:00 PM').style('text-align:center').style('margin-top:15px;margin-bottom:5px')
                ui.button(icon='visibility', color='white').classes('font-bold text-green w-1/2').style(
                    'margin-top:5px;margin-bottom:5px;margin-left:20px')


def doctor_personal_info(doctorName):
    doctorinfoCard.clear()
    doctormenuButtons.clear()
    with doctormenuButtons:
        theme.DoctorMenu(doctorName, "doctor_info_button")
    with doctorinfoCard:
        with ui.column().style('width:100%'):
            ui.label('Photo de Profil :').classes('text-h6 text-black')
            ui.upload(on_upload=lambda e: ui.notify(f'Uploaded {e.name}')).classes('bg-white').style(
                'width:100%').props('color="green"')
        with ui.row().style('width:100%'):
            with ui.column().style('width:48%'):
                ui.label('Nom et Prénom').classes('text-h6 text-black font-bold')
                ui.input().classes('w-full').props('outlined')
            with ui.column().style('width:48%'):
                ui.label('Rôle').classes('text-h6 text-black font-bold')
                select4 = ui.select(["Dr Foucci", "Dr Dana Scally"], value="Dr Foucci").style('width:100%').classes(
                    'bg-white').props('outlined')
        with ui.row().style('width:100%'):
            with ui.column().style('width:48%'):
                ui.label('Email').classes('text-h6 text-black font-bold')
                ui.input().classes('w-full').props('outlined')
            with ui.column().style('width:48%'):
                ui.label('Téléphone').classes('text-h6 text-black font-bold')
                ui.input().style('width:100%').classes('bg-white').props('outlined')
        ui.button('Save Doctor', icon='save', color='green').classes('w-full text-white')


def View_doctorDash(doctorid):
    doctor = models.readOneDoctor(doctorid)
    global doctorinfoCard, doctormenuButtons
    with ui.row().classes('w-full'):
        ui.button(icon='arrow_back', color='white', on_click=lambda: ui.navigate.back()).classes('text-black')
        ui.label(f'Dr. {doctor.nom}').classes('text-h5 text-black font-bold')
    with ui.row().classes('w-full'):
        with ui.card().style('width:32%;align-items:center'):
            with ui.avatar(size='150px'):
                ui.image(f'/static/{doctor.photoProfil}')
            ui.label(f'{doctor.nom}').classes('text-h6 text-black font-bold')
            ui.label(f'{doctor.email}').classes('text-h6 text-grey')
            ui.label(f'{doctor.numTel}').classes('text-h6 text-black font-bold')
            with ui.column().classes('w-full') as doctormenuButtons:
                theme.DoctorMenu(doctor.nom, "doctor_info_button")
        with ui.card().style('width:66%') as doctorinfoCard:
            doctor_personal_info(doctor.nom)

def doctorsDash():
    doctors = models.readallDoctors()
    ui.label('Doctors List').classes('text-h5 text-black font-bold')
    with ui.card().classes('w-full'):
        with ui.row().classes('w-full'):
            ui.input('Nom du docteur').style('width:18%').classes('bg-grey-1')
            ui.space()
            ui.button(icon='search', color='green-6').style('width:21.5%;height:55px').classes('text-white')

        with ui.grid(columns='auto 1fr 1fr 1fr 1fr auto').classes('w-full gap-0'):
            for _ in range(1):
                ui.label('#').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                ui.label('Doctor Name').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                ui.label('Phone').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                ui.label('Role').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                ui.label('Email').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                ui.label('Actions').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
            for i in doctors:
                doctorId = ui.label(f'{i.id}').classes('font-bold').style('margin-top:15px;margin-bottom:5px')
                with ui.row().classes('w-full'):
                    with ui.avatar().style('margin-top:5px;margin-bottom:5px'):
                        ui.image(f'/static/{i.photoProfil}')
                    nom = ui.label(f'{i.nom}').style('padding-bottom:0px').classes('text-h7 text-black font-bold').style(
                            'margin-top:20px')
                ui.label(f'{i.numTel}').classes('text-green font-bold').style('text-align:center').style(
                    'margin-top:15px;margin-bottom:5px')
                ui.label(f'{i.specialite}').classes('font-bold').style('text-align:center').style(
                    'margin-top:15px;margin-bottom:5px')
                ui.label(f'{i.email}').classes('font-bold').style('text-align:center').style(
                    'margin-top:15px;margin-bottom:5px')
                with ui.expansion(icon='edit').classes('font-bold bg-white text-black w-full').style(
                        'margin-top:15px;margin-bottom:5px'):
                    with ui.row().classes('w-full'):
                        ui.button('Voir', icon='visibility', color='green',
                                  on_click=lambda i=i: ui.navigate.to(
                                      f'View_doctor/{i.id}')).classes('text-white')
                        ui.button('Supprimer', icon='delete', color='green').classes('text-white')
        with ui.dialog() as new_doctor, ui.card().classes('w-full'):
            profile_pic = ""

            def uploadfile(e):
                nonlocal profile_pic
                filename = e.name
                profile_pic = filename
                data64 = base64.b64encode(e.content.read())
                with open(f'static/{filename}', 'wb') as f:
                    f.write(base64.b64decode(data64))
                    ui.notify('l`image à été bien enregistré')
                uploadElement.reset()
                save_doctor_button.visible = True

            with ui.card().style('width:100%'):
                with ui.column().style('width:100%'):
                    ui.label('Photo de Profil :').classes('text-h6 text-black')
                    uploadElement = ui.upload(on_upload=lambda e: uploadfile(e)).classes('bg-white').style(
                        'width:100%').props('color="green"')
                with ui.row().style('width:100%'):
                    with ui.column().style('width:48%'):
                        ui.label('Nom et Prénom').classes('text-h6 text-black font-bold')
                        nom = ui.input().classes('w-full').props('outlined')
                    with ui.column().style('width:48%'):
                        ui.label('Spécialité').classes('text-h6 text-black font-bold')
                        specialite = ui.select(["Cardiologie", "Dermatologie", "Neurologie", "Psychiatrie"],
                                               value="Neurologie").style('width:100%').classes('bg-white').props(
                            'outlined')
                with ui.row().style('width:100%'):
                    with ui.column().style('width:48%'):
                        ui.label('Email').classes('text-h6 text-black font-bold')
                        email = ui.input().classes('w-full').props('outlined')
                    with ui.column().style('width:48%'):
                        ui.label('Téléphone').classes('text-h6 text-black font-bold')
                        tel = ui.input().style('width:100%').classes('bg-white').props('outlined')
                ui.label('Password').classes('text-h6 text-black font-bold')
                motdepasse = ui.input(password=True).classes('w-full text-h6 text-black font-bold').props('outlined')
                ui.label('Permissions & Access :').classes('text-h6 text-black font-bold')
                with ui.grid(columns='2fr 1fr 1fr 1fr 1fr').classes('w-full gap-0'):
                    for _ in range(1):
                        ui.label('').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                        ui.label('Read').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                        ui.label('Edit').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                        ui.label('Create').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                        ui.label('Delete').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                    for i in range(1):
                        ui.label('Patient').classes('text-green font-bold').style('text-align:center').style(
                            'margin-top:15px;margin-bottom:5px')
                        ui.checkbox().style('margin-left:20px')
                        ui.checkbox().style('margin-left:20px')
                        ui.checkbox().style('margin-left:20px')
                        ui.checkbox().style('margin-left:20px')
                    for i in range(1):
                        ui.label('Invoices').classes('text-green font-bold').style('text-align:center').style(
                            'margin-top:15px;margin-bottom:5px')
                        ui.checkbox().style('margin-left:20px')
                        ui.checkbox().style('margin-left:20px')
                        ui.checkbox().style('margin-left:20px')
                        ui.checkbox().style('margin-left:20px')
                    for i in range(1):
                        ui.label('Appointment').classes('text-green font-bold').style('text-align:center').style(
                            'margin-top:15px;margin-bottom:5px')
                        ui.checkbox().style('margin-left:20px')
                        ui.checkbox().style('margin-left:20px')
                        ui.checkbox().style('margin-left:20px')
                        ui.checkbox().style('margin-left:20px')
                    for i in range(1):
                        ui.label('Payments').classes('text-green font-bold').style('text-align:center').style(
                            'margin-top:15px;margin-bottom:5px')
                        ui.checkbox().style('margin-left:20px')
                        ui.checkbox().style('margin-left:20px')
                        ui.checkbox().style('margin-left:20px')
                        ui.checkbox().style('margin-left:20px')

                def saveDoctor(profile_pic):

                    models.newDoctor(profile_pic, nom.value, email.value, motdepasse.value, tel.value, specialite.value,
                                     new_doctor)

                save_doctor_button = ui.button('Save Doctor', icon='save', color='green', on_click=lambda: saveDoctor(profile_pic)).classes('w-full text-white')
                save_doctor_button.visible = False

        with ui.page_sticky(position='bottom-right', x_offset=20, y_offset=20):
            ui.button(icon='add_circle', color='green', on_click=lambda: new_doctor.open()).props('fab')

def New_MedicalRecord(patientid):
    patient = models.readOnePatient(patientid)
    records = models.readallMedicalRecord(patientid)
    if len(records) == 0:
        NewRecordId = 1
    else:
        NewRecordId = records[-1].id + 1
    if patient == None:
        ui.notify('Pas de résultat', type='Negative')
        ui.navigate.back()
    else:
        with ui.row().classes('w-full'):
            ui.button(icon='arrow_back', color='white', on_click=lambda: ui.navigate.back()).classes('text-black')
            ui.label('New Medical Record').classes('text-h5 text-black font-bold')
        with ui.row().classes('w-full'):
            with ui.card().style('width:32%;align-items:center'):
                with ui.avatar(size='150px'):
                    if patient != None:
                        ui.image(f'/static/{patient.photoProfil}')
                    else:
                        ui.image(f'/static/profile_pic.png')

                ui.label(f'{patient.nomPatient}').classes('text-h6 text-black font-bold')
                ui.label(f'{patient.email}').classes('text-h6 text-grey')
                ui.label(f'{patient.numTel}').classes('text-h6 text-black font-bold')
            with ui.dialog() as addMedicine, ui.card().classes('w-full'):
                ui.label('Add Medicine').classes('text-h6 text-black font-bold')
                ui.separator()
                ui.label('Choose Medicine').classes('text-h7 text-black')

                medicineList = []
                medicines = models.readallMedicin()
                for i in medicines:
                    medicineList.append(i.nomMedicin)

                a = ui.select(medicineList).style('width:100%').classes('bg-white').props('outlined')
                ui.label('Instructions').classes('text-h7 text-black')
                b = ui.select(['After Meal', 'Before Meal'], value='Before Meal').style('width:100%').classes(
                    'bg-white').props('outlined')
                ui.label('Quantity').classes('text-h7 text-black')
                c = ui.input('').props('outlined').classes('w-full')
                ui.label('Dosage Quantity').classes('text-h7 text-black')
                d = ui.input('').props('outlined').classes('w-full')
                ui.label('Dosage').classes('text-h7 text-black')
                with ui.row().classes('w-full'):
                    Sm = ui.switch('Morning (M)', on_change=lambda: switchChange())
                    Sa = ui.switch('Afternoon (A)', on_change=lambda: switchChange())
                    Se = ui.switch('Evening (E)', on_change=lambda: switchChange())
                dosageStr = ''

                def switchChange():
                    nonlocal dosageStr
                    dosageList = []
                    dosageStr = ""
                    if Sm.value == True:
                        dosageList.append('Morning (M)')
                    if Sa.value == True:
                        dosageList.append('Afternoon (A)')
                    if Se.value == True:
                        dosageList.append('Evening (E)')
                    for i in dosageList:
                        dosageStr = dosageStr + f' {i}'

                ui.button('ADD', color='green', on_click=lambda: updateGrid()).classes('text-white')

            with ui.card().style('width:66%') as medRecordsCard:
                ui.label('Docteur').classes('text-h6 text-black font-bold')
                docteur = ui.select(["Dr Foucci", "Dr Dana Scally"], value="Dr Foucci").style('width:100%').classes(
                    'bg-white').props('outlined')
                ui.label('Complains').classes('text-h6 text-black font-bold')
                complains = ui.textarea().classes('w-full').props('outlined')
                ui.label('Diagnosis').classes('text-h6 text-black font-bold')
                diagnosis = ui.textarea().classes('w-full').props('outlined')
                ui.label('Vital Signs').classes('text-h6 text-black font-bold')
                signsVitaux = ui.textarea().classes('w-full').props('outlined')
                ui.label('Treatment').classes('text-h6 text-black font-bold')

                serviceList = []
                serviceDict = {}
                services = models.readallServices()
                for i in services:
                    serviceList.append(i.nomService)
                    serviceDict[i.nomService] = i.prix
                service_select = ui.select(serviceList, multiple=True).classes('w-full').props('outlined use-chips')
                ui.label('Medicine :').classes('text-h6 text-black font-bold')
                with ui.grid(columns='1fr 1fr 2fr 1fr 1fr 1fr auto').classes('w-full gap-0') as MedGrid:
                    def MedicineGrid():
                        PatientMedicene = models.readallPatientsMedicines(NewRecordId)
                        for _ in range(1):
                            ui.label('Item').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                            ui.label('Item Price').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                            ui.label('Dosage').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                            ui.label('Instructions').classes('border p-1 bg-grey-2 font-bold').style(
                                'text-align:center')
                            ui.label('Quantity').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                            ui.label('Amount').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                            ui.label('Actions').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                        if PatientMedicene != None:
                            for i in PatientMedicene:
                                ui.label(f'{i.nomMedicin}').classes('text-green font-bold').style(
                                    'text-align:center').style('margin-top:15px;margin-bottom:5px')
                                ui.label(f'{i.prix}').classes('font-bold').style('text-align:center').style(
                                    'margin-top:15px;margin-bottom:5px')
                                ui.label(f'{i.dosage}').classes('text-green font-bold').style(
                                    'text-align:center').style('margin-top:15px;margin-bottom:5px')
                                ui.label(f'{i.instructions}').classes('font-bold').style('text-align:center').style(
                                    'margin-top:15px;margin-bottom:5px')
                                ui.label(f'{i.quantity}').classes('text-green font-bold').style(
                                    'text-align:center').style('margin-top:15px;margin-bottom:5px')
                                ui.label(f'{i.prix * i.quantity}').classes('font-bold').style(
                                    'text-align:center').style('margin-top:15px;margin-bottom:5px')
                                #ui.button(icon='edit').classes('font-bold bg-grey-2 text-black w-5/6').style('margin-top:15px;margin-bottom:5px')
                                ui.button(icon='delete', color='white').classes('font-bold text-red w-full').style(
                                    'margin-top:5px;margin-bottom:5px')

                    MedicineGrid()

                def updateGrid():
                    models.newPatientMedicin(NewRecordId, patient.id, a.value,
                                             models.readOneMedicineByName(a.value).prix, b.value, c.value, d.value,
                                             dosageStr, addMedicine)
                    MedGrid.clear()
                    with MedGrid:
                        MedicineGrid()

                def uploadfile(e):
                    filename = e.name
                    data64 = base64.b64encode(e.content.read())
                    with open(f'static/{filename}', 'wb') as f:
                        f.write(base64.b64decode(data64))
                        models.newPatientAttachments(NewRecordId, patientid, filename)
                        ui.notify('l`image à été bien enregistré')
                    uploadElement.reset()
                    with filesGrid:
                        with ui.column():
                            ui.image(f'/static/patientfiles.png').on('click', lambda: ui.download(
                                f'/static/{filename}')).classes('w-20')
                            ui.label(f'{filename}')

                ui.button('Add Medicine', icon='add', color='white', on_click=lambda: addMedicine.open()).classes(
                    'font-bold text-red w-full').style('border-type:doted-line')
                ui.label('Attachments :').classes('text-h6 text-black font-bold')
                with ui.card().classes('w-full'):
                    with ui.grid(columns=4).classes('w-full gap-5') as filesGrid:
                        ui.label()
                uploadElement = ui.upload(on_upload=lambda e: uploadfile(e)).classes('bg-white').style(
                    'width:100%').props('color="black"')

                def saveRecord():
                    models.newMedicalRecord(NewRecordId, patientid, docteur.value, complains.value, diagnosis.value,
                                            signsVitaux.value, date.today())
                    for i, j in serviceDict.items():
                        models.newPatientServices(NewRecordId, patientid, i, j)
                    ui.notify('les données ont bien été enregistrées')

                ui.button('Save Patient', icon='save', color='green', on_click=lambda: saveRecord()).classes(
                    'w-full text-white')


def Edit_MedicalRecord(patientid, recordId):
    patient = models.readOnePatient(patientid)
    records = models.readallMedicalRecord(patientid)
    NewRecordId = recordId
    if patient == None:
        ui.notify('Pas de résultat', type='Negative')
        ui.navigate.back()
    else:
        with ui.row().classes('w-full'):
            ui.button(icon='arrow_back', color='white', on_click=lambda: ui.navigate.back()).classes('text-black')
            ui.label('Edit Medical Record').classes('text-h5 text-black font-bold')
        with ui.row().classes('w-full'):
            with ui.card().style('width:32%;align-items:center'):
                with ui.avatar(size='150px'):
                    if patient != None:
                        ui.image(f'/static/{patient.photoProfil}')
                    else:
                        ui.image(f'/static/profile_pic.png')

                ui.label(f'{patient.nomPatient}').classes('text-h6 text-black font-bold')
                ui.label(f'{patient.email}').classes('text-h6 text-grey')
                ui.label(f'{patient.numTel}').classes('text-h6 text-black font-bold')
            with ui.dialog() as addMedicine, ui.card().classes('w-full'):
                ui.label('Add Medicine').classes('text-h6 text-black font-bold')
                ui.separator()
                ui.label('Choose Medicine').classes('text-h7 text-black')

                medicineList = []
                medicines = models.readallMedicin()
                for i in medicines:
                    medicineList.append(i.nomMedicin)

                a = ui.select(medicineList).style('width:100%').classes('bg-white').props('outlined')
                ui.label('Instructions').classes('text-h7 text-black')
                b = ui.select(['After Meal', 'Before Meal'], value='Before Meal').style('width:100%').classes(
                    'bg-white').props('outlined')
                ui.label('Quantity').classes('text-h7 text-black')
                c = ui.input('').props('outlined').classes('w-full')
                ui.label('Dosage Quantity').classes('text-h7 text-black')
                d = ui.input('').props('outlined').classes('w-full')
                ui.label('Dosage').classes('text-h7 text-black')
                with ui.row().classes('w-full'):
                    Sm = ui.switch('Morning (M)', on_change=lambda: switchChange())
                    Sa = ui.switch('Afternoon (A)', on_change=lambda: switchChange())
                    Se = ui.switch('Evening (E)', on_change=lambda: switchChange())
                dosageStr = ''

                def switchChange():
                    nonlocal dosageStr
                    dosageList = []
                    dosageStr = ""
                    if Sm.value == True:
                        dosageList.append('Morning (M)')
                    if Sa.value == True:
                        dosageList.append('Afternoon (A)')
                    if Se.value == True:
                        dosageList.append('Evening (E)')
                    for i in dosageList:
                        dosageStr = dosageStr + f' {i}'

                ui.button('ADD', color='green', on_click=lambda: updateGrid()).classes('text-white')
            record = models.readOneMedicalRecord(recordId)
            with ui.card().style('width:66%') as medRecordsCard:
                ui.label('Docteur').classes('text-h6 text-black font-bold')
                docteur = ui.select(["Dr Foucci", "Dr Dana Scally"], value="Dr Foucci").style('width:100%').classes(
                    'bg-white').props('outlined')
                docteur.value = record.nomDocteur
                ui.label('Complains').classes('text-h6 text-black font-bold')
                complains = ui.textarea().classes('w-full').props('outlined')
                complains.value = record.plaintes
                ui.label('Diagnosis').classes('text-h6 text-black font-bold')
                diagnosis = ui.textarea().classes('w-full').props('outlined')
                diagnosis.value = record.diagnostic
                ui.label('Vital Signs').classes('text-h6 text-black font-bold')
                signsVitaux = ui.textarea().classes('w-full').props('outlined')
                signsVitaux.value = record.signesVitaux
                ui.label('Treatment').classes('text-h6 text-black font-bold')

                serviceList = []
                serviceDict = {}
                services = models.readallServices()
                for service in services:
                    serviceList.append(service.nomService)
                    serviceDict[service.nomService] = service.prix
                savedPatientServicesList = []
                savedPatientServices = models.readallPatientsServices(recordId)
                for patientService in savedPatientServices:
                    savedPatientServicesList.append(patientService.nomService)
                service_select = ui.select(serviceList, multiple=True, value=savedPatientServicesList).classes(
                    'w-full').props('outlined use-chips')
                ui.label('Medicine :').classes('text-h6 text-black font-bold')
                with ui.grid(columns='1fr 1fr 2fr 1fr 1fr 1fr auto').classes('w-full gap-0') as MedGrid:
                    def MedicineGrid():
                        PatientMedicene = models.readallPatientsMedicines(recordId)
                        for _ in range(1):
                            ui.label('Item').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                            ui.label('Item Price').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                            ui.label('Dosage').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                            ui.label('Instructions').classes('border p-1 bg-grey-2 font-bold').style(
                                'text-align:center')
                            ui.label('Quantity').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                            ui.label('Amount').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                            ui.label('Actions').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                        if PatientMedicene != None:
                            for i in PatientMedicene:
                                ui.label(f'{i.nomMedicin}').classes('text-green font-bold').style(
                                    'text-align:center').style('margin-top:15px;margin-bottom:5px')
                                ui.label(f'{i.prix}').classes('font-bold').style('text-align:center').style(
                                    'margin-top:15px;margin-bottom:5px')
                                ui.label(f'{i.dosage}').classes('text-green font-bold').style(
                                    'text-align:center').style('margin-top:15px;margin-bottom:5px')
                                ui.label(f'{i.instructions}').classes('font-bold').style('text-align:center').style(
                                    'margin-top:15px;margin-bottom:5px')
                                ui.label(f'{i.quantity}').classes('text-green font-bold').style(
                                    'text-align:center').style('margin-top:15px;margin-bottom:5px')
                                ui.label(f'{i.prix * i.quantity}').classes('font-bold').style(
                                    'text-align:center').style('margin-top:15px;margin-bottom:5px')
                                #ui.button(icon='edit').classes('font-bold bg-grey-2 text-black w-5/6').style('margin-top:15px;margin-bottom:5px')
                                ui.button(icon='delete', color='white').classes('font-bold text-red w-full').style(
                                    'margin-top:5px;margin-bottom:5px')

                    MedicineGrid()

                def updateGrid():
                    models.newPatientMedicin(recordId, patient.id, a.value, models.readOneMedicineByName(a.value).prix,
                                             b.value, c.value, d.value, dosageStr, addMedicine)
                    MedGrid.clear()
                    with MedGrid:
                        MedicineGrid()

                def uploadfile(e):
                    filename = e.name
                    data64 = base64.b64encode(e.content.read())
                    with open(f'static/{filename}', 'wb') as f:
                        f.write(base64.b64decode(data64))
                        models.newPatientAttachments(recordId, patientid, filename)
                        ui.notify('l`image à été bien enregistré')
                    uploadElement.reset()
                    with filesGrid:
                        with ui.column():
                            ui.image(f'/static/patientfiles.png').on('click', lambda: ui.download(
                                f'/static/{filename}')).classes('w-20')
                            ui.label(f'{filename}')

                ui.button('Add Medicine', icon='add', color='white', on_click=lambda: addMedicine.open()).classes(
                    'font-bold text-red w-full').style('border-type:doted-line')
                ui.label('Attachments :').classes('text-h6 text-black font-bold')
                with ui.card().classes('w-full'):
                    recordFiles = models.readallPatientsAttachments(recordId)
                    with ui.grid(columns=4).classes('w-full gap-5') as filesGrid:
                        for file in recordFiles:
                            with ui.column():
                                ui.image(f'/static/patientfiles.png').on('click', lambda: ui.download(
                                    f'/static/{file.nomFichier}')).classes('w-20')
                                ui.label(f'{file.nomFichier}')

                uploadElement = ui.upload(on_upload=lambda e: uploadfile(e)).classes('bg-white').style(
                    'width:100%').props('color="black"')

                def saveRecord():
                    models.editMedicalRecord(recordId, patientid, docteur.value, complains.value, diagnosis.value,
                                             signsVitaux.value, date.today())
                    for value in service_select.value:
                        if value not in savedPatientServicesList:
                            for i, j in serviceDict.items():
                                if i == value:
                                    models.newPatientServices(recordId, patientid, i, j)
                    ui.notify('les données ont bien été enregistrées')

                ui.button('Save Patient', icon='save', color='green', on_click=lambda: saveRecord()).classes(
                    'w-full text-white')


def appointmentsDash():
    patients = models.readallPatients()
    patients_list = []
    patients_dic = {}
    for patient in patients:
        patients_list.append(patient.nomPatient)
        patients_dic[patient.nomPatient] = patient.id
        patients_dic[patient.id] = patient.nomPatient
    doctors = models.readallDoctors()
    doctors_list = []
    doctors_dic = {}
    for doctor in doctors:
        doctors_list.append(doctor.nom)
        doctors_dic[doctor.id] = doctor.nom
    appointments = models.readAllAppointments()
    events_list = []
    for appointment in appointments:
        color = 'green'
        if appointment.statut == 'Pending':
            color = 'red'
        elif appointment.statut == 'Accepted':
            color = 'green'
        else:
            color = 'grey'
        events_list.append({
            'title': models.readOnePatient(appointment.patientId).nomPatient,
            'start': str(appointment.dateVisite) + ' ' + str(appointment.heurDebut),
            'end': str(appointment.dateVisite)+ ' ' + str(appointment.heurFin),
            'color': color,
            'id': appointment.id,
        })
    print(events_list)
    ui.label('Appointments').classes('text-h5 text-black font-bold')
    options = {
        'initialView': 'dayGridMonth',
        'headerToolbar': {'left': 'title', 'right': ''},
        'footerToolbar': {'right': 'prev,next today'},
        'slotMinTime': '05:00:00',
        'slotMaxTime': '22:00:00',
        'allDaySlot': False,
        'timeZone': 'local',
        'height': 'auto',
        'width': 'auto',
        'events': events_list,
    }

    def handle_click(event: events.GenericEventArguments):
      def show_appointment(appointmentId):
        appointment_record = models.readOneAppointment(appointmentId)

        with ui.dialog().classes('w-full') as view_appointment, ui.card().classes('w-full'):
            ui.label('View/Edit Appointment').classes('text-h5 text-black font-bold')
            ui.separator()
            ui.label('Patient Name').classes('text-h6 text-black')
            a_view = ui.input().style('width:100%').classes(
                'bg-white').props('outlined')
            a_view.value = patients_dic.get(appointment_record.patientId)
            ui.label('Purpose of visit').classes('text-h6 text-black')
            b_view = ui.input().style('width:100%').classes('bg-white').props(
                'outlined')
            b_view.value = appointment_record.butVisite
            ui.label('Date of Visit').classes('text-h6 text-black')
            with ui.input('Date of Visit', on_change=lambda: menu.close()).style('width:100%').props(
                    'outlined') as date1_view:
                with date1_view.add_slot('append'):
                    ui.icon('edit_calendar').on('click', lambda: menu.open()).classes('cursor-pointer')
                with ui.menu() as menu:
                    ui.date().bind_value(date1_view)
            date1_view.value = appointment_record.dateVisite
            with ui.row().classes('w-full'):
                with ui.column().style('width:48%'):

                    ui.label('Start Time').classes('text-h6 text-black')
                    d_view = ui.input().style('width:100%').classes('bg-white').props('outlined')
                    d_view.value = appointment_record.heurDebut
                with ui.column().style('width:48%'):
                    ui.label('End Time').classes('text-h6 text-black')
                    f_view = ui.input().style('width:100%').classes('bg-white').props('outlined')
                    f_view.value = appointment_record.heurFin
            with ui.row().classes('w-full'):
                with ui.column().style('width:48%'):
                    ui.label('Assigned Doctor').classes('text-h6 text-black')
                    docs_view = ui.input().style('width:100%').classes(
                        'bg-white').props('outlined')
                    docs_view.value = doctors_dic.get(appointment_record.doctorId)
                with ui.column().style('width:48%'):
                    ui.label('Appointment Status').classes('text-h6 text-black')
                    h_view = ui.select(["Pending", "Canceled", "Accepted"], value="Accepted").style('width:100%').classes(
                        'bg-white').props('outlined')
                    h_view.value = appointment_record.statut
            ui.label('Available Rooms').classes('text-h6 text-black ')
            i_view = ui.select(["Room A12", "Room B4"], value="Room A12").style('width:100%').classes('bg-white').props(
                'outlined')
            i_view.value = appointment_record.chambre
            ui.label('Description').classes('text-h6 text-black ')
            j_view = ui.textarea().classes('w-full').props('outlined')
            j_view.value = appointment_record.description
            ui.button('Save Appointment', icon='save', color='green',on_click=lambda: models.editAppointment(appointmentId, date1_view.value, d_view.value, h_view.value, i_view.value, j_view.value, b_view.value, f_view.value)).classes('w-full text-white')
        view_appointment.open()
      if 'info' in event.args:
            show_appointment(event.args['info']['event']['id'])

    with ui.card().classes('w-full bg-white'):
        fullcalendar(options, on_click=handle_click)
        with ui.dialog() as new_appointment, ui.card().classes('w-full'):
            ui.label('New Appointment').classes('text-h5 text-black font-bold')
            ui.separator()
            ui.label('Choose Patient').classes('text-h6 text-black')
            a = ui.select(patients_list).style('width:100%').classes(
                'bg-white').props('outlined')
            ui.label('Purpose of visit').classes('text-h6 text-black')
            b = ui.input().style('width:100%').classes('bg-white').props(
                'outlined')
            ui.label('Date of Visit').classes('text-h6 text-black')
            with ui.input('Date of Visit', on_change=lambda: menu.close()).style('width:100%').props(
                    'outlined') as date1:
                with date1.add_slot('append'):
                    ui.icon('edit_calendar').on('click', lambda: menu.open()).classes('cursor-pointer')
                with ui.menu() as menu:
                    ui.date().bind_value(date1)
            with ui.row().classes('w-full'):
                with ui.column().style('width:48%'):
                    timeSlots = ["00:00", "01:00", "02:00", "03:00", "04:00", "05:00", "06:00", "07:00", "08:00",
                                 "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00",
                                 "18:00", "19:00", "20:00", "21:00", "22:00", "23:00"]
                    ui.label('Start Time').classes('text-h6 text-black')
                    d = ui.select(timeSlots, value="00:00").style('width:100%').classes('bg-white').props('outlined')
                with ui.column().style('width:48%'):
                    ui.label('End Time').classes('text-h6 text-black')
                    f = ui.select(timeSlots, value="01:00").style('width:100%').classes('bg-white').props('outlined')
            with ui.row().classes('w-full'):
                with ui.column().style('width:48%'):
                    ui.label('Choose Doctor').classes('text-h6 text-black')
                    docs = ui.select(doctors_list).style('width:100%').classes(
                        'bg-white').props('outlined')
                with ui.column().style('width:48%'):
                    ui.label('Appointment Status').classes('text-h6 text-black')
                    h = ui.select(["Pending", "Canceled", "Accepted"], value="Accepted").style('width:100%').classes(
                        'bg-white').props('outlined')
            ui.label('Available Rooms').classes('text-h6 text-black ')
            i = ui.select(["Room A12", "Room B4"], value="Room A12").style('width:100%').classes('bg-white').props(
                'outlined')
            ui.label('Description').classes('text-h6 text-black ')
            j = ui.textarea().classes('w-full').props('outlined')
            ui.button('Save Appointment', icon='save', color='green',on_click=lambda: models.newAppointment(patients_dic.get(a.value), doctors_dic.get(docs.value), date1.value, d.value, h.value, i.value, j.value, b.value, f.value)).classes('w-full text-white')

    with ui.page_sticky(position='bottom-left', x_offset=20, y_offset=20):
        ui.button(icon='add_circle', color='green', on_click=lambda: new_appointment.open()).props('fab')





def staffDash():
    staffs = models.readAllStaff()
    ui.label('Staff List').classes('text-h5 text-black font-bold')
    with ui.card().classes('w-full'):
        with ui.row().classes('w-full'):
            ui.input('Nom du Personnel').style('width:18%').classes('bg-grey-1')
            ui.space()
            ui.button(icon='search', color='green-6').style('width:21.5%;height:55px').classes('text-white')

        with ui.grid(columns='auto 1fr 1fr 1fr 1fr auto').classes('w-full gap-0'):
            for _ in range(1):
                ui.label('#').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                ui.label('Doctor Name').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                ui.label('Phone').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                ui.label('Role').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                ui.label('Email').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                ui.label('Actions').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
            for i in staffs:
                staffId = ui.label(f'{i.id}').classes('font-bold').style('margin-top:15px;margin-bottom:5px')
                with ui.row().classes('w-full'):
                    with ui.avatar().style('margin-top:5px;margin-bottom:5px'):
                        ui.image(f'/static/{i.photoProfil}')

                    nom = ui.label(f'{i.nom}').style('padding-bottom:0px').classes('text-h7 text-black font-bold').style(
                            'margin-top:20px')
                ui.label(f'{i.numTel}').classes('text-green font-bold').style('text-align:center').style(
                    'margin-top:15px;margin-bottom:5px')
                ui.label(f'{i.role}').classes('font-bold').style('text-align:center').style(
                    'margin-top:15px;margin-bottom:5px')
                ui.label(f'{i.email}').classes('font-bold').style('text-align:center').style(
                    'margin-top:15px;margin-bottom:5px')
                with ui.expansion(icon='edit').classes('font-bold bg-white text-black w-full').style(
                        'margin-top:15px;margin-bottom:5px'):
                    with ui.row().classes('w-full'):
                        ui.button('Voir', icon='visibility', color='green', on_click=lambda: edit_staff.open()).classes(
                            'text-white')
                        ui.button('Supprimer', icon='delete', color='green').classes('text-white')
        with ui.dialog() as new_staff, ui.card().classes('w-full'):
            profile_pic = ""

            def uploadfile(e):
                nonlocal profile_pic
                filename = e.name
                profile_pic = filename
                data64 = base64.b64encode(e.content.read())
                with open(f'static/{filename}', 'wb') as f:
                    f.write(base64.b64decode(data64))
                    ui.notify('l`image à été bien enregistré')
                uploadElement.reset()

            with ui.card().style('width:100%'):
                with ui.column().style('width:100%'):
                    ui.label('Photo de Profil :').classes('text-h6 text-black')
                    uploadElement = ui.upload(on_upload=lambda e: uploadfile(e)).classes('bg-white').style(
                        'width:100%').props('color="green"')
                with ui.row().style('width:100%'):
                    with ui.column().style('width:48%'):
                        ui.label('Nom et Prénom').classes('text-h6 text-black font-bold')
                        nom = ui.input().classes('w-full').props('outlined')
                    with ui.column().style('width:48%'):
                        ui.label('Rôle').classes('text-h6 text-black font-bold')
                        role = ui.select(["Cardiologie", "Dermatologie", "Neurologie", "Psychiatrie"],
                                         value="Neurologie").style('width:100%').classes('bg-white').props('outlined')
                with ui.row().style('width:100%'):
                    with ui.column().style('width:48%'):
                        ui.label('Email').classes('text-h6 text-black font-bold')
                        email = ui.input().classes('w-full').props('outlined')
                    with ui.column().style('width:48%'):
                        ui.label('Téléphone').classes('text-h6 text-black font-bold')
                        tel = ui.input().style('width:100%').classes('bg-white').props('outlined')
                ui.label('Password').classes('text-h6 text-black font-bold')
                motdepasse = ui.input(password=True).classes('w-full text-h6 text-black font-bold').props('outlined')
                ui.label('Permissions & Access :').classes('text-h6 text-black font-bold')
                with ui.grid(columns='2fr 1fr 1fr 1fr 1fr').classes('w-full gap-0'):
                    for _ in range(1):
                        ui.label('').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                        ui.label('Read').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                        ui.label('Edit').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                        ui.label('Create').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                        ui.label('Delete').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                    for i in range(1):
                        ui.label('Patient').classes('text-green font-bold').style('text-align:center').style(
                            'margin-top:15px;margin-bottom:5px')
                        ui.checkbox().style('margin-left:20px')
                        ui.checkbox().style('margin-left:20px')
                        ui.checkbox().style('margin-left:20px')
                        ui.checkbox().style('margin-left:20px')
                    for i in range(1):
                        ui.label('Invoices').classes('text-green font-bold').style('text-align:center').style(
                            'margin-top:15px;margin-bottom:5px')
                        ui.checkbox().style('margin-left:20px')
                        ui.checkbox().style('margin-left:20px')
                        ui.checkbox().style('margin-left:20px')
                        ui.checkbox().style('margin-left:20px')
                    for i in range(1):
                        ui.label('Appointment').classes('text-green font-bold').style('text-align:center').style(
                            'margin-top:15px;margin-bottom:5px')
                        ui.checkbox().style('margin-left:20px')
                        ui.checkbox().style('margin-left:20px')
                        ui.checkbox().style('margin-left:20px')
                        ui.checkbox().style('margin-left:20px')
                    for i in range(1):
                        ui.label('Payments').classes('text-green font-bold').style('text-align:center').style(
                            'margin-top:15px;margin-bottom:5px')
                        ui.checkbox().style('margin-left:20px')
                        ui.checkbox().style('margin-left:20px')
                        ui.checkbox().style('margin-left:20px')
                        ui.checkbox().style('margin-left:20px')

                def saveStaff(profile_pic):
                    models.newStaff(profile_pic, nom.value, email.value, motdepasse.value, tel.value, role.value,
                                    new_staff)

                ui.button('Save Staff', icon='save', color='green', on_click=lambda: saveStaff(profile_pic)).classes(
                    'w-full text-white')

        with ui.dialog() as edit_staff, ui.card().classes('w-full'):
            with ui.card().style('width:100%') as medRecordsCard:
                with ui.column().style('width:100%'):
                    ui.label('Photo de Profil :').classes('text-h6 text-black')
                    ui.upload(on_upload=lambda e: ui.notify(f'Uploaded {e.name}')).classes('bg-white').style(
                        'width:100%').props('color="green"')
                with ui.row().style('width:100%'):
                    with ui.column().style('width:48%'):
                        ui.label('Nom et Prénom').classes('text-h6 text-black font-bold')
                        ui.input().classes('w-full').props('outlined')
                    with ui.column().style('width:48%'):
                        ui.label('Rôle').classes('text-h6 text-black font-bold')
                        select4 = ui.select(["Dr Foucci", "Dr Dana Scally"], value="Dr Foucci").style(
                            'width:100%').classes('bg-white').props('outlined')
                with ui.row().style('width:100%'):
                    with ui.column().style('width:48%'):
                        ui.label('Email').classes('text-h6 text-black font-bold')
                        ui.input().classes('w-full').props('outlined')
                    with ui.column().style('width:48%'):
                        ui.label('Téléphone').classes('text-h6 text-black font-bold')
                        ui.input().style('width:100%').classes('bg-white').props('outlined')
                ui.label('Password').classes('text-h6 text-black font-bold')
                ui.input(password=True).classes('w-full text-h6 text-black font-bold').props('outlined')
                ui.label('Permissions & Access :').classes('text-h6 text-black font-bold')
                with ui.grid(columns='2fr 1fr 1fr 1fr 1fr').classes('w-full gap-0'):
                    for _ in range(1):
                        ui.label('').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                        ui.label('Read').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                        ui.label('Edit').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                        ui.label('Create').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                        ui.label('Delete').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                    for i in range(1):
                        ui.label('Patient').classes('text-green font-bold').style('text-align:center').style(
                            'margin-top:15px;margin-bottom:5px')
                        ui.checkbox().style('margin-left:20px')
                        ui.checkbox().style('margin-left:20px')
                        ui.checkbox().style('margin-left:20px')
                        ui.checkbox().style('margin-left:20px')
                    for i in range(1):
                        ui.label('Invoices').classes('text-green font-bold').style('text-align:center').style(
                            'margin-top:15px;margin-bottom:5px')
                        ui.checkbox().style('margin-left:20px')
                        ui.checkbox().style('margin-left:20px')
                        ui.checkbox().style('margin-left:20px')
                        ui.checkbox().style('margin-left:20px')
                    for i in range(1):
                        ui.label('Appointment').classes('text-green font-bold').style('text-align:center').style(
                            'margin-top:15px;margin-bottom:5px')
                        ui.checkbox().style('margin-left:20px')
                        ui.checkbox().style('margin-left:20px')
                        ui.checkbox().style('margin-left:20px')
                        ui.checkbox().style('margin-left:20px')
                    for i in range(1):
                        ui.label('Payments').classes('text-green font-bold').style('text-align:center').style(
                            'margin-top:15px;margin-bottom:5px')
                        ui.checkbox().style('margin-left:20px')
                        ui.checkbox().style('margin-left:20px')
                        ui.checkbox().style('margin-left:20px')
                        ui.checkbox().style('margin-left:20px')
        with ui.page_sticky(position='bottom-right', x_offset=20, y_offset=20):
            ui.button(icon='add_circle', color='green', on_click=lambda: new_staff.open()).props('fab')


def servicesDash():
    with ui.dialog() as NewService, ui.card().classes('w-full'):
        with ui.row().classes('w-full'):
            ui.label('New Sérvice').classes('text-h5 text-black font-bold')
            ui.space()
            ui.icon('close').classes('text-h5 text-red font-bold').on('click', lambda: NewService.close())
        ui.label('Nom du sérvice').classes('text-h6 text-black')
        service_name = ui.input().props('outlined').classes('w-full')
        ui.label('prix').classes('text-h6 text-black')
        service_prix = ui.number().props('outlined').classes('w-full')
        ui.label('Description').classes('text-h6 text-black')
        service_desc = ui.textarea().props('outlined').classes('w-full')
        service_enabled = ui.switch('désactivé', on_change=lambda: Switch_changed()).classes(
            'bg-white text-red font-bold')

        def Switch_changed():
            if service_enabled.value:
                service_enabled.text = 'activé'
                service_enabled.classes(replace='text-green font-bold')
            else:
                service_enabled.text = 'désactivé'
                service_enabled.classes(replace='text-red font-bold')

        ui.button('Sauvegarder', color='green',
                  on_click=lambda: models.newService(service_name.value, service_prix.value, service_desc.value,
                                                     service_enabled.value, NewService)).classes(
            'text-white self-center')

    def EditServiceFunc(serviceId):
        service = models.readOneService(serviceId)
        with ui.dialog() as EditService, ui.card().classes('w-full'):
            with ui.row().classes('w-full'):
                ui.label('Edit Sérvice').classes('text-h5 text-black font-bold')
                ui.space()
                ui.icon('close').classes('text-h5 text-red font-bold').on('click', lambda: EditService.close())
            ui.label('Nom du sérvice').classes('text-h6 text-black')
            service_nameEdit = ui.input().props('outlined').classes('w-full')
            service_nameEdit.value = service.nomService
            ui.label('prix').classes('text-h6 text-black')
            service_prixEdit = ui.number().props('outlined').classes('w-full')
            service_prixEdit.value = service.prix
            ui.label('Déscription').classes('text-h6 text-black')
            service_descEdit = ui.textarea().props('outlined').classes('w-full')
            service_descEdit.value = service.description

            def Switch_changedEdit():
                if service_enabledEdit.value:
                    service_enabledEdit.text = 'activé'
                    service_enabledEdit.classes(replace='text-green font-bold')
                else:
                    service_enabledEdit.text = 'désactivé'
                    service_enabledEdit.classes(replace='text-red font-bold')

            service_enabledEdit = ui.switch('désactivé', on_change=lambda: Switch_changedEdit()).classes(
                'bg-white text-red font-bold')
            service_enabledEdit.value = service.enabled

            Switch_changedEdit()
            ui.button('Sauvegarder', color='green',
                      on_click=lambda: models.editService(service.id, service_nameEdit.value, service_prixEdit.value,
                                                          service_descEdit.value, service_enabledEdit.value)).classes(
                'text-white self-center')
        EditService.open()

    ui.label('Sérvices').classes('text-h5 text-black font-bold')
    with ui.card().classes('w-full'):
        with ui.row().classes('w-full'):
            ui.input('Nom du Service').style('width:18%').classes('bg-white').props('outlined')
            ui.space()
            ui.button(icon='search', color='green-6').style('width:20%;height:55px').classes('text-white')
        services = models.readallServices()
        with ui.grid(columns='1fr 1fr 1fr 2fr auto').classes('w-full gap-0'):
            for _ in range(1):
                ui.label('Nom du service').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                ui.label('Prix').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                ui.label('Statut').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                ui.label('Déscription').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                ui.label('Actions').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
            for i in services:
                nom = ui.label(f'{i.nomService}').classes('font-bold').style('text-align:center').style(
                    'margin-top:15px;margin-bottom:5px;marign-left:20px')
                ui.label(f'{i.prix}').classes('text-black font-bold').style('text-align:center').style(
                    'margin-top:15px;margin-bottom:5px')
                statut = ui.label('').classes('font-bold text-green').style('text-align:center').style(
                    'margin-top:15px;margin-bottom:5px')
                if i.enabled:
                    statut.text = 'activé'
                    statut.classes(replace='text-green font-bold')
                else:
                    statut.text = 'désactivé'
                    statut.classes(replace='text-red font-bold')
                ui.label(f'{i.description[0:25]}').classes('text-black font-bold').style('text-align:center').style(
                    'margin-top:15px;margin-bottom:5px')
                with ui.expansion(icon='edit').classes('font-bold bg-white text-black w-full').style(
                        'margin-top:15px;margin-bottom:5px'):
                    with ui.row().classes('w-full'):
                        ui.button('Modifier', icon='visibility', color='green',
                                  on_click=lambda i=i: EditServiceFunc(i.id)).classes('text-white')
                        ui.button('Supprimer', icon='delete', color='green').classes('text-white')
    with ui.page_sticky(position='bottom-right', x_offset=20, y_offset=20):
        ui.button(icon='add_circle', color='green', on_click=lambda: NewService.open()).props('fab')


def medicineDash():
    with ui.dialog() as NewMedicine, ui.card().classes('w-full'):
        with ui.row().classes('w-full'):
            ui.label('Nouvelle médecine').classes('text-h5 text-black font-bold')
            ui.space()
            ui.icon('close').classes('text-h5 text-red font-bold').on('click', lambda: NewMedicine.close())
        with ui.row().classes('w-full'):
            medicinName = ui.input('Nom du Medicament').props('outlined').style('width:47%')
            measure = ui.select(['Sélectionnez Mesure', 'Mg', 'Capsule', 'Tablet'], value='Sélectionnez Mesure').props(
                'outlined').style('width:47%')
        with ui.row().classes('w-full'):
            price = ui.number('Price').props('outlined').style('width:47%')
            instock = ui.number('InStock').props('outlined').style('width:47%')
        ui.label('Déscription').classes('text-h6 text-black')
        description = ui.textarea().props('outlined').classes('w-full')
        ui.button('Sauvegarder', color='green',
                  on_click=lambda: models.newMedicine(medicinName.value, measure.value, price.value, instock.value,
                                                      description.value, NewMedicine)).classes('text-white self-center')

    def EditMedicineFunc(MedicineId):
        medicine = models.readOneMedicine(MedicineId)
        with ui.dialog() as EditMedicine, ui.card().classes('w-full'):
            with ui.row().classes('w-full'):
                ui.label('Modifier Le Médecine').classes('text-h5 text-black font-bold')
                ui.space()
                ui.icon('close').classes('text-h5 text-red font-bold').on('click', lambda: EditMedicine.close())
            with ui.row().classes('w-full'):
                medicinName = ui.input('Nom du Medicament').props('outlined').style('width:47%')
                medicinName.value = medicine.nomMedicin
                measure = ui.select(['Select Measure', 'Mg', 'Capsule', 'Tablet'], value='Sélectionnez Mesure').props(
                    'outlined').style('width:47%')
                measure.value = medicine.measure
            with ui.row().classes('w-full'):
                price = ui.number('Prix').props('outlined').style('width:47%')
                price.value = medicine.prix
                instock = ui.number('InStock').props('outlined').style('width:47%')
                instock.value = medicine.inStock

            ui.label('Déscription').classes('text-h6 text-black')
            desc = ui.textarea().props('outlined').classes('w-full')
            desc.value = medicine.description
            ui.button('Sauvegarder', color='green',
                      on_click=lambda: models.editMedicine(MedicineId, medicinName.value, measure.value, price.value,
                                                           instock.value, desc.value)).classes('text-white self-center')
        EditMedicine.open()

    ui.label('Médecine').classes('text-h5 text-black font-bold')
    with ui.card().classes('w-full'):
        with ui.row().classes('w-full'):
            ui.input('Nom du Medicament').style('width:18%').classes('bg-white').props('outlined')
            ui.space()
            ui.button(icon='search', color='green-6').style('width:20%;height:55px').classes('text-white')
        meds = models.readallMedicin()
        with ui.grid(columns='auto 1fr 1fr 1fr 1fr 1fr auto').classes('w-full gap-0'):
            for _ in range(1):
                ui.label('Id').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                ui.label('Nom du Medicament').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                ui.label('Statut').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                ui.label('Prix').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                ui.label('InStock').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                ui.label('Measure').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                ui.label('Actions').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
            for i in meds:
                MedicineId = ui.label(f'{i.id}').classes('font-bold').style('text-align:center').style(
                    'margin-top:15px;margin-bottom:5px;marign-left:20px')
                nom = ui.label(f'{i.nomMedicin}').classes('font-bold').style('text-align:center').style(
                    'margin-top:15px;margin-bottom:5px;marign-left:20px')

                statut = ui.label(f'').classes('font-bold').style('text-align:center').style(
                    'margin-top:15px;margin-bottom:5px')
                if int(i.inStock) > 0:
                    statut.text = 'Disponible'
                    statut.classes(replace='text-green font-bold')
                else:
                    statut.text = 'En rupture de stock'
                    statut.classes(replace='text-red font-bold')
                ui.label(f'{i.prix}').classes('text-green font-bold').style('text-align:center').style(
                    'margin-top:15px;margin-bottom:5px')
                ui.label(f'{i.inStock}').classes('font-bold text-black').style('text-align:center').style(
                    'margin-top:15px;margin-bottom:5px')
                ui.label(f'{i.measure}').classes('font-bold text-black').style('text-align:center').style(
                    'margin-top:15px;margin-bottom:5px')
                with ui.expansion(icon='edit').classes('font-bold bg-white text-black w-full').style(
                        'margin-top:15px;margin-bottom:5px'):
                    with ui.row().classes('w-full'):
                        ui.button('Modifier', icon='visibility', color='green',
                                  on_click=lambda MedicineId=MedicineId: EditMedicineFunc(
                                      int(MedicineId.text))).classes('text-white')
                        ui.button('Supprimer', icon='delete', color='green').classes('text-white')
    with ui.page_sticky(position='bottom-right', x_offset=20, y_offset=20):
        ui.button(icon='add_circle', color='green', on_click=lambda: NewMedicine.open()).props('fab')


def invoicesDash():

    invoices = models.readAllInvoices()
    def calculate_total(recordId):
        sous_total = 0
        medicines = models.readallPatientsMedicines(recordId)
        services = models.readallPatientsServices(recordId)
        for medicine in medicines:
            sous_total += (medicine.quantity * medicine.prix)
        for service in services:
            sous_total += service.prixService
        return sous_total

    ui.label('Invoices').classes('text-h5 text-black font-bold')
    with ui.card().classes('w-full'):
        with ui.row().classes('w-full'):
            ui.input('Nom du Patient').style('width:18%').classes('bg-grey-1')
            select2 = ui.select(["Paid", "Canceled", "Due"], value="Paid").style('width:18%').classes('bg-grey-1')
            with ui.input('Date', on_change=lambda: menu.close()).style('width:18%').classes('bg-grey-1') as date:
                with date.add_slot('append'):
                    ui.icon('edit_calendar').on('click', lambda: menu.open()).classes('cursor-pointer')
                with ui.menu() as menu:
                    ui.date().bind_value(date)
            ui.button(icon='search', color='green-6').style('width:20%;height:55px').classes('text-white')

        with ui.grid(columns='auto 1fr 1fr 1fr 1fr auto').classes('w-full gap-0'):
            for _ in range(1):
                ui.label('Invoice ID').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                ui.label('Patient').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                ui.label('Created Date').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                ui.label('Due Date').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                ui.label('Amount').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                ui.label('Actions').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
            for i in invoices:
                patient = models.readOnePatient(i.patientId)
                invoiceId = ui.label(f'{i.id}').classes('font-bold').style('margin-top:15px;margin-bottom:5px')
                with ui.row().classes('w-full'):
                    with ui.avatar().style('margin-top:5px;margin-bottom:5px'):
                        ui.image(f'/static/{patient.photoProfil}')
                    with ui.column().classes('gap-0'):
                        nom = ui.label(f'{patient.nomPatient}').style('padding-bottom:0px').classes('text-h7 text-black').style('margin-top:5px')
                        ui.label(f'{patient.numTel}').style('padding-top:0px').classes('text-h7 text-grey')
                ui.label(f'{i.createddate}').classes('font-bold').style('text-align:center').style('margin-top:15px;margin-bottom:5px')
                ui.label(f'{i.duedate}').classes('text-green font-bold').style('text-align:center').style('margin-top:15px;margin-bottom:5px')
                ui.label(f'{calculate_total(i.recordId)} dh').classes('font-bold').style('text-align:center').style('margin-top:15px;margin-bottom:5px')
                with ui.expansion(icon='edit').classes('font-bold bg-white text-black w-full').style('margin-top:15px;margin-bottom:5px'):
                    with ui.row().classes('w-full'):
                        ui.button('Voir', icon='visibility', color='green',
                                  on_click=lambda: ui.navigate.to(f'View_invoice/{invoiceId.text}')).classes('text-white')
                        ui.button('Supprimer', icon='delete', color='green').classes('text-white')
    with ui.page_sticky(position='bottom-right', x_offset=20, y_offset=20):
        ui.button(icon='add_circle', color='green', on_click=lambda: ui.navigate.to('Create_invoice')).props('fab')


def View_invoiceDash(invoiceId):
    montant = 0
    invoice = models.readOneInvoice(invoiceId)
    patient = models.readOnePatient(invoice.patientId)
    medicines = models.readallPatientsMedicines(invoice.recordId)
    services = models.readallPatientsServices(invoice.recordId)
    def calculate_total(recordId):
        nonlocal montant
        sous_total = 0
        medicines = models.readallPatientsMedicines(recordId)
        services = models.readallPatientsServices(recordId)
        for medicine in medicines:
            sous_total += (medicine.quantity * medicine.prix)
        for service in services:
            sous_total += service.prixService
        sub_total.text = f'{sous_total} dh'
        discounted_Total = sous_total - invoice.discount
        taxTotal = (invoice.tax * discounted_Total) / 100
        grand_total.text = f'{discounted_Total - taxTotal} dh'
        montant = discounted_Total - taxTotal


    with ui.dialog() as generatePay, ui.card().classes('w-full'):
        with ui.row().classes('w-full'):
            ui.label('Generate Payment').classes('text-h5 text-black font-bold')
            ui.space()
            ui.icon('close').classes('text-h5 text-red font-bold').on('click', lambda: generatePay.close())
        ui.label('Status').classes('text-h6 text-black')
        statut = ui.select(['Status...', 'Paid', 'Canceled', 'Pending'], value='Status...').props('outlined').classes('w-full')
        ui.label('Payment Method').classes('text-h6 text-black')
        methode = ui.select(['Method...', 'Cash', 'Check', 'Visa Card'], value='Method...').props('outlined').classes('w-full')
        ui.button('Generate payment', color='green', on_click=lambda: models.newPayment(invoice.patientId, invoice.createddate, invoice.duedate, invoice.discount, invoice.tax, statut.value, methode.value,invoice.notes, invoice.id,montant)).classes('text-white self-center')

    with ui.row().classes('w-full'):
        ui.button(icon='arrow_back', color='white', on_click=lambda: ui.navigate.back()).classes('text-black')
        ui.label('View Invoice').classes('text-h5 text-black font-bold')
        ui.space()
        ui.button('Generate payment', color='green', on_click=lambda: generatePay.open()).classes('text-white')
    with ui.card().classes('w-full').style('border-radius: 15px'):
        with ui.row().classes('w-full'):
            ui.image('/static/logo.webp').classes('w-1/12 self-left')
            ui.space()
            ui.label(f'Created at : {invoice.createddate}')
            ui.label(f'Due Date : {invoice.duedate}')
        with ui.row().classes('w-full'):
            with ui.card().style('border-radius: 15px; width:48%;height:195px'):
                ui.label('From :').classes('text-h5 text-black font-bold').style('margin-top: 15px')
                ui.label('Medical Center').classes('text-h7 text-black')
                ui.label('medical-center@gmail.com').classes('text-h7 text-black')
                ui.label('+212-681990152').classes('text-h7 text-black')
            ui.space()
            with ui.card().style('border-radius: 15px; width:48%;height:195px'):
                with ui.row().classes('w-full'):
                    ui.label('To :').classes('text-h5 text-black font-bold').style('margin-top: 15px')
                    ui.space()
                ui.label(f'{patient.nomPatient}').classes('text-h7 text-black')
                ui.label(f'{patient.email}').classes('text-h7 text-black')
                ui.label(f'{patient.numTel}').classes('text-h7 text-black')
        with ui.row().classes('w-full'):
            with ui.card().style('border-radius: 15px; width:66%'):
                with ui.grid(columns='auto 1fr 1fr 1fr auto').classes('w-full gap-0'):
                    for _ in range(1):
                        ui.label('Item').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                        ui.label('Item Price').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                        ui.label('Quantity').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                        ui.label('Amount').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                        ui.label('type').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                    for service in services:
                        ui.label(f'{service.nomService}').classes('font-bold').style(
                            'margin-top:15px;margin-bottom:5px')
                        ui.label(f'{service.prixService}').style('padding-top:0px').classes('text-h7 text-black').style(
                            'margin-top:15px;margin-bottom:5px;margin-left:35px')
                        ui.label(f'{1}').classes('font-bold').style('text-align:center').style(
                            'margin-top:15px;margin-bottom:5px')
                        ui.label(f'{service.prixService}').classes('font-bold').style('text-align:center').style(
                            'margin-top:15px;margin-bottom:5px')
                        ui.label('Sérvice').classes('font-bold').style('text-align:center').style(
                            'margin-top:15px;margin-bottom:5px')
                    for medicine in medicines:
                        ui.label(f'{medicine.nomMedicin}').classes('font-bold').style(
                            'margin-top:15px;margin-bottom:5px')
                        ui.label(f'{medicine.prix}').style('padding-top:0px').classes('text-h7 text-black').style(
                            'margin-top:15px;margin-bottom:5px;margin-left:35px')
                        ui.label(f'{medicine.quantity}').classes('font-bold').style('text-align:center').style(
                            'margin-top:15px;margin-bottom:5px')
                        ui.label(f'{medicine.quantity * medicine.prix}').classes('font-bold').style(
                            'text-align:center').style(
                            'margin-top:15px;margin-bottom:5px')
                        ui.label('Médicament').classes('font-bold').style('text-align:center').style(
                            'margin-top:15px;margin-bottom:5px')
            with ui.card().style('border-radius: 15px; width:31%'):
                with ui.row().classes('w-full'):
                    ui.label('Sub Total:').classes('text-h6 text-black')
                    ui.space()
                    sub_total = ui.label('0 dh').classes('text-h6 text-black')
                with ui.row().classes('w-full'):
                    ui.label('Discount:').classes('text-h6 text-black')
                    ui.space()
                    discount = ui.label(f'{invoice.discount} dh').classes('text-h6 text-black')
                with ui.row().classes('w-full'):
                    ui.label('Tax:').classes('text-h6 text-black')
                    ui.space()
                    tax = ui.label(f'{invoice.tax} dh').classes('text-h6 text-black')
                with ui.row().classes('w-full'):
                    ui.label('Grand Total:').classes('text-h6 text-black')
                    ui.space()
                    grand_total = ui.label('0 dh').classes('text-h6 text-green')
                ui.label('Notes:').classes('text-h6 text-black font-bold')
                notes = ui.textarea(f'{invoice.notes}').props('outlined').classes('w-full')
                notes.enabled = False
                calculate_total(invoice.recordId)


def Create_invoiceDash():
    patients = models.readallPatients()
    Global_discount = 0
    Global_tax = 0
    patientsList = ["Choose Patient"]
    patientsDict = {}
    recordsList = ["Choose Record Date"]
    recordsDict = {}
    sous_total = 0
    for patient in patients:
        patientsList.append(patient.nomPatient)
        patientsDict[patient.nomPatient] = patient.id
        patientsDict["Choose Patient"] = "Choose Patient"

    def fetchRecords(patientId):
        recordsList = []
        if patientId != "Choose Patient":
            patientrecords = models.readallMedicalRecord(patientId)
            recordsList = ["Choose Record Date"]
            for record in patientrecords:
                if record.invoiceGenerated == False:
                   recordsList.append(record.dateCreation)
                   recordsDict[record.dateCreation] = record.id
            print(recordsDict)
            medRecordsSelect.visible = True
            medRecordsSelect.options = recordsList
            medRecordsSelect.update()
            medRecordsSelect.value = recordsList[0]
            name.text = models.readOnePatient(patientId).nomPatient
            email.text = models.readOnePatient(patientId).email
            tel.text = models.readOnePatient(patientId).numTel
        else:
            ui.navigate.to('/Create_invoice')

    def fetchPatientDetails(recordID, patientId):
        nonlocal sous_total
        if recordID == None:
            print('No records found')
        medicines = models.readallPatientsMedicines(recordID)
        services = models.readallPatientsServices(recordID)
        invoiceGrid.clear()
        sous_total = 0
        with invoiceGrid:
            for _ in range(1):
                ui.label('Item').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                ui.label('Item Price').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                ui.label('Quantity').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                ui.label('Amount').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                ui.label('Type').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
            for service in services:
                sous_total += service.prixService
                ui.label(f'{service.nomService}').classes('font-bold').style('margin-top:15px;margin-bottom:5px')
                ui.label(f'{service.prixService}').style('padding-top:0px').classes('text-h7 text-black').style(
                    'margin-top:15px;margin-bottom:5px;margin-left:35px')
                ui.label(f'{1}').classes('font-bold').style('text-align:center').style(
                    'margin-top:15px;margin-bottom:5px')
                ui.label(f'{service.prixService}').classes('font-bold').style('text-align:center').style(
                    'margin-top:15px;margin-bottom:5px')
                ui.label('Sérvice').classes('font-bold').style('text-align:center').style(
                    'margin-top:15px;margin-bottom:5px')
            for medicine in medicines:
                sous_total += (medicine.quantity * medicine.prix)
                ui.label(f'{medicine.nomMedicin}').classes('font-bold').style('margin-top:15px;margin-bottom:5px')
                ui.label(f'{medicine.prix}').style('padding-top:0px').classes('text-h7 text-black').style(
                    'margin-top:15px;margin-bottom:5px;margin-left:35px')
                ui.label(f'{medicine.quantity}').classes('font-bold').style('text-align:center').style(
                    'margin-top:15px;margin-bottom:5px')
                ui.label(f'{medicine.quantity * medicine.prix}').classes('font-bold').style('text-align:center').style(
                    'margin-top:15px;margin-bottom:5px')
                ui.label('Médicament').classes('font-bold').style('text-align:center').style(
                    'margin-top:15px;margin-bottom:5px')
            sub_total.text = f'{sous_total:.2f} dh'
            grand_total.text = f'{sous_total:.2f} dh'
            saveInvoice_button.enabled = True

    with ui.row().classes('w-full'):
        ui.button(icon='arrow_back', color='white', on_click=lambda: ui.navigate.back()).classes('text-black')
        ui.label('Create Invoice').classes('text-h5 text-black font-bold')
    with ui.card().classes('w-full').style('border-radius: 15px'):
        with ui.row().classes('w-full'):
            ui.image('/static/logo.webp').classes('w-1/12 self-left')
            ui.space()
            with ui.input('Due Date', on_change=lambda: menu.close()).style(
                    'width:18%; margin-top: 15px;border-radius: 15px').classes('bg-grey-1').props('outlined') as DuedateInput:
                with DuedateInput.add_slot('append'):
                    ui.icon('edit_calendar').on('click', lambda: menu.open()).classes('cursor-pointer')
                with ui.menu() as menu:
                    ui.date().bind_value(DuedateInput)
        with ui.row().classes('w-full'):
            with ui.card().style('border-radius: 15px; width:48%;height:195px'):
                ui.label('From :').classes('text-h5 text-black font-bold').style('margin-top: 15px')
                ui.label('Medical Center').classes('text-h7 text-black')
                ui.label('medical-center@gmail.com').classes('text-h7 text-black')
                ui.label('+212-681990152').classes('text-h7 text-black')
            ui.space()
            with ui.card().style('border-radius: 15px; width:48%;height:195px'):
                with ui.row().classes('w-full'):
                    ui.label('To :').classes('text-h5 text-black font-bold').style('margin-top: 15px')
                    ui.space()
                    patient = ui.select(options=patientsList,
                                        value='Choose Patient',
                                        on_change=lambda: fetchRecords(patientsDict[patient.value])).props('outlined')
                    medRecordsSelect = ui.select(options=recordsList,
                                                 value=recordsList[0],
                                                 on_change=lambda e: fetchPatientDetails(recordsDict.get(e.value),patientsDict[patient.value])).props('outlined')
                    medRecordsSelect.visible = False
                name = ui.label().classes('text-h7 text-black')
                email = ui.label().classes('text-h7 text-black')
                tel = ui.label().classes('text-h7 text-black')

        with ui.row().classes('w-full'):
            with ui.card().style('border-radius: 15px; width:66%'):
                with ui.grid(columns='auto 1fr 1fr 1fr auto').classes('w-full gap-0') as invoiceGrid:
                    pass

                saveInvoice_button = ui.button('Save Invoice',on_click=lambda:(models.newInvoice(patientsDict.get(patient.value),recordsDict.get(medRecordsSelect.value),date.today(),DuedateInput.value,float(discountInput.value),float(taxInput.value),notes.value),models.editMedicalRecordByInvoice(recordsDict.get(medRecordsSelect.value),True))).classes('w-full bg-white text-green').style(
                    'border: none; border: 2px dotted black')
                saveInvoice_button.enabled = False
            with ui.card().style('border-radius: 15px; width:31%'):
                def calcul_total(sous_total):
                    discounted_Total = sous_total - discountInput.value
                    discount.text = discountInput.value
                    taxTotal = (taxInput.value * discounted_Total) / 100
                    tax.text = taxTotal
                    grand_total.text = f'{discounted_Total - taxTotal} dh'

                with ui.row().classes('w-full'):
                    discountInput = ui.number('Discount (dh)',value=0).props('outlined').style('width:46%')
                    taxInput = ui.number('Tax (%)',value=0).props('outlined').style('width:46%')
                ui.button(icon='task_alt', on_click=lambda: calcul_total(sous_total)).classes('w-full')
                with ui.row().classes('w-full'):
                    ui.label('Sub Total:').classes('text-h6 text-black')
                    ui.space()
                    sub_total = ui.label('0 dh').classes('text-h6 text-black')
                with ui.row().classes('w-full'):
                    ui.label('Discount:').classes('text-h6 text-black')
                    ui.space()
                    discount = ui.label('0 dh').classes('text-h6 text-black')
                with ui.row().classes('w-full'):
                    ui.label('Tax:').classes('text-h6 text-black')
                    ui.space()
                    tax = ui.label('0 dh').classes('text-h6 text-black')
                with ui.row().classes('w-full'):
                    ui.label('Grand Total:').classes('text-h6 text-black')
                    ui.space()
                    grand_total = ui.label('0 dh').classes('text-h6 text-green')
                ui.label('Notes:').classes('text-h6 text-black font-bold')
                notes = ui.textarea().props('outlined').classes('w-full')


def paymentsDash():
    payments = models.readAllPayments()
    dailyPayments = 0
    monthlyPayments = 0
    yearlyPayments = 0
    def calculate_totals():
        nonlocal dailyPayments, monthlyPayments, yearlyPayments
        for payment in payments:
            if payment.statut == "Paid" and payment.createddate.day == date.today().day:
                dailyPayments += payment.amount
            if payment.statut == "Paid" and payment.createddate.month == date.today().month:
                monthlyPayments += payment.amount
            if payment.statut == "Paid" and payment.createddate.year == date.today().year:
                yearlyPayments += payment.amount

    calculate_totals()
    with ui.row().classes('w-full'):
        with ui.card().style('width:32%'):
            with ui.row().classes('w-full'):
                ui.label('Total Payments Today :').classes('text-h6 text-black')
                ui.space()
            with ui.row().classes('w-full'):
                ui.label(f'{dailyPayments} dh').classes('text-h6 text-blue font-bold')
                ui.space()
                ui.icon('today').classes('text-h5 text-green')
        with ui.card().style('width:32%'):
            with ui.row().classes('w-full'):
                ui.label('Total Payments This Month :').classes('text-h6 text-black')
                ui.space()
            with ui.row().classes('w-full'):
                ui.label(f'{monthlyPayments} dh').classes('text-h6 text-blue font-bold')
                ui.space()
                ui.icon('calendar_month').classes('text-h5 text-green')
        with ui.card().style('width:32%'):
            with ui.row().classes('w-full'):
                ui.label('Total Payments this year :').classes('text-h6 text-black')
                ui.space()
            with ui.row().classes('w-full'):
                ui.label(f'{yearlyPayments} dh').classes('text-h6 text-blue font-bold')
                ui.space()
                ui.icon('event_available').classes('text-h5 text-green')

    with ui.card().classes('w-full'):
        with ui.row().classes('w-full'):
            ui.input('Nom du Patient').style('width:18%').classes('bg-grey-1')
            select2 = ui.select(["Paid", "Canceled", "Due"], value="Paid").style('width:18%').classes('bg-grey-1')
            with ui.input('Date', on_change=lambda: menu.close()).style('width:18%').classes('bg-grey-1') as dateInput:
                with dateInput.add_slot('append'):
                    ui.icon('edit_calendar').on('click', lambda: menu.open()).classes('cursor-pointer')
                with ui.menu() as menu:
                    ui.date().bind_value(dateInput)
            ui.button(icon='search', color='green-6').style('width:20%;height:55px').classes('text-white')

        with ui.grid(columns='auto 2fr 1fr 1fr 1fr 1fr auto').classes('w-full gap-0'):
            for _ in range(1):
                ui.label('#').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                ui.label('Patient').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                ui.label('Created at').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                ui.label('Status').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                ui.label('Amount').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                ui.label('Method').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                ui.label('Actions').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
            for payment in payments:
                patient = models.readOnePatient(payment.patientId)
                ui.label(f'{payment.id}').classes('font-bold').style('margin-top:15px;margin-bottom:5px')
                with ui.row().classes('w-full'):
                    with ui.avatar().style('margin-top:5px;margin-bottom:5px'):
                        ui.image(f'/static/{patient.photoProfil}')
                    with ui.column().classes('gap-0'):
                        nom = ui.label(f'{patient.nomPatient}').style('padding-bottom:0px').classes(
                            'text-h7 text-black').style('margin-top:5px')
                        ui.label(f'{patient.numTel}').style('padding-top:0px').classes('text-h7 text-grey')
                ui.label(f'{payment.createddate}').classes('font-bold').style('text-align:center').style(
                    'margin-top:15px;margin-bottom:5px')
                ui.label(f'{payment.statut}').classes('text-green font-bold').style('text-align:center').style(
                    'margin-top:15px;margin-bottom:5px')
                ui.label(f'{payment.amount}').classes('font-bold').style('text-align:center').style(
                    'margin-top:15px;margin-bottom:5px')
                ui.label(f'{payment.methode}').classes('font-bold').style('text-align:center').style(
                    'margin-top:15px;margin-bottom:5px')
                #ui.button(icon='edit').classes('font-bold bg-grey-2 text-black w-5/6').style('margin-top:15px;margin-bottom:5px')
                with ui.expansion(icon='edit').classes('font-bold bg-white text-black w-full').style(
                        'margin-top:15px;margin-bottom:5px'):
                    with ui.row().classes('w-full'):
                        ui.button('Voir', icon='visibility', color='green',
                                  on_click=lambda: ui.navigate.to(f'View_payment/{payment.id}')).classes('text-white')
                        ui.button('Supprimer', icon='delete', color='green').classes('text-white')

def View_payment(paymentId):
    payment = models.readOnePayment(paymentId)
    montant = 0
    invoice = models.readOneInvoice(payment.invoiceId)
    patient = models.readOnePatient(invoice.patientId)
    medicines = models.readallPatientsMedicines(invoice.recordId)
    services = models.readallPatientsServices(invoice.recordId)
    def calculate_total(recordId):
        nonlocal montant
        sous_total = 0
        medicines = models.readallPatientsMedicines(recordId)
        services = models.readallPatientsServices(recordId)
        for medicine in medicines:
            sous_total += (medicine.quantity * medicine.prix)
        for service in services:
            sous_total += service.prixService
        sub_total.text = f'{sous_total} dh'
        discounted_Total = sous_total - invoice.discount
        taxTotal = (invoice.tax * discounted_Total) / 100
        grand_total.text = f'{discounted_Total - taxTotal} dh'
        montant = discounted_Total - taxTotal

    with ui.row().classes('w-full'):
        ui.button(icon='arrow_back', color='white', on_click=lambda: ui.navigate.back()).classes('text-black')
        ui.label('View Invoice').classes('text-h5 text-black font-bold')
        ui.space()
        statut = ui.select(['Status...', 'Paid', 'Canceled', 'Pending'], value=payment.statut).props('outlined')
        methode = ui.select(['Method...', 'Cash', 'Check', 'Visa Card'], value=payment.methode).props('outlined')
    with ui.card().classes('w-full').style('border-radius: 15px'):
        with ui.row().classes('w-full'):
            ui.image('/static/logo.webp').classes('w-1/12 self-left')
            ui.space()
            ui.label(f'Created at : {invoice.createddate}')
            ui.label(f'Due Date : {invoice.duedate}')
        with ui.row().classes('w-full'):
            with ui.card().style('border-radius: 15px; width:48%;height:195px'):
                ui.label('From :').classes('text-h5 text-black font-bold').style('margin-top: 15px')
                ui.label('Medical Center').classes('text-h7 text-black')
                ui.label('medical-center@gmail.com').classes('text-h7 text-black')
                ui.label('+212-681990152').classes('text-h7 text-black')
            ui.space()
            with ui.card().style('border-radius: 15px; width:48%;height:195px'):
                with ui.row().classes('w-full'):
                    ui.label('To :').classes('text-h5 text-black font-bold').style('margin-top: 15px')
                    ui.space()
                ui.label(f'{patient.nomPatient}').classes('text-h7 text-black')
                ui.label(f'{patient.email}').classes('text-h7 text-black')
                ui.label(f'{patient.numTel}').classes('text-h7 text-black')
        with ui.row().classes('w-full'):
            with ui.card().style('border-radius: 15px; width:66%'):
                with ui.grid(columns='auto 1fr 1fr 1fr auto').classes('w-full gap-0'):
                    for _ in range(1):
                        ui.label('Item').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                        ui.label('Item Price').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                        ui.label('Quantity').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                        ui.label('Amount').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                        ui.label('type').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                    for service in services:
                        ui.label(f'{service.nomService}').classes('font-bold').style(
                            'margin-top:15px;margin-bottom:5px')
                        ui.label(f'{service.prixService}').style('padding-top:0px').classes('text-h7 text-black').style(
                            'margin-top:15px;margin-bottom:5px;margin-left:35px')
                        ui.label(f'{1}').classes('font-bold').style('text-align:center').style(
                            'margin-top:15px;margin-bottom:5px')
                        ui.label(f'{service.prixService}').classes('font-bold').style('text-align:center').style(
                            'margin-top:15px;margin-bottom:5px')
                        ui.label('Sérvice').classes('font-bold').style('text-align:center').style(
                            'margin-top:15px;margin-bottom:5px')
                    for medicine in medicines:
                        ui.label(f'{medicine.nomMedicin}').classes('font-bold').style(
                            'margin-top:15px;margin-bottom:5px')
                        ui.label(f'{medicine.prix}').style('padding-top:0px').classes('text-h7 text-black').style(
                            'margin-top:15px;margin-bottom:5px;margin-left:35px')
                        ui.label(f'{medicine.quantity}').classes('font-bold').style('text-align:center').style(
                            'margin-top:15px;margin-bottom:5px')
                        ui.label(f'{medicine.quantity * medicine.prix}').classes('font-bold').style(
                            'text-align:center').style(
                            'margin-top:15px;margin-bottom:5px')
                        ui.label('Médicament').classes('font-bold').style('text-align:center').style(
                            'margin-top:15px;margin-bottom:5px')
            with ui.card().style('border-radius: 15px; width:31%'):
                with ui.row().classes('w-full'):
                    ui.label('Sub Total:').classes('text-h6 text-black')
                    ui.space()
                    sub_total = ui.label('0 dh').classes('text-h6 text-black')
                with ui.row().classes('w-full'):
                    ui.label('Discount:').classes('text-h6 text-black')
                    ui.space()
                    discount = ui.label(f'{invoice.discount} dh').classes('text-h6 text-black')
                with ui.row().classes('w-full'):
                    ui.label('Tax:').classes('text-h6 text-black')
                    ui.space()
                    tax = ui.label(f'{invoice.tax} dh').classes('text-h6 text-black')
                with ui.row().classes('w-full'):
                    ui.label('Grand Total:').classes('text-h6 text-black')
                    ui.space()
                    grand_total = ui.label('0 dh').classes('text-h6 text-green')
                ui.label('Notes:').classes('text-h6 text-black font-bold')
                notes = ui.textarea(f'{invoice.notes}').props('outlined').classes('w-full')
                notes.enabled = False
                calculate_total(invoice.recordId)

def patientsDash():
    with ui.row().classes('w-full'):
        with ui.card().style('width:32%'):
            with ui.row().classes('w-full'):
                ui.label('Total Patients Today :').classes('text-h6 text-black')
                ui.space()
            with ui.row().classes('w-full'):
                ui.label('1345').classes('text-h6 text-blue font-bold')
                ui.space()
                ui.icon('personal_injury').classes('text-h5 text-green')
        with ui.card().style('width:32%'):
            with ui.row().classes('w-full'):
                ui.label('Total Patients This Month :').classes('text-h6 text-black')
                ui.space()
            with ui.row().classes('w-full'):
                ui.label('375').classes('text-h6 text-blue font-bold')
                ui.space()
                ui.icon('personal_injury').classes('text-h5 text-green')
        with ui.card().style('width:32%'):
            with ui.row().classes('w-full'):
                ui.label('Total Patients this year :').classes('text-h6 text-black')
                ui.space()
            with ui.row().classes('w-full'):
                ui.label('45').classes('text-h6 text-blue font-bold')
                ui.space()
                ui.icon('personal_injury').classes('text-h5 text-green')

    with ui.card().classes('w-full'):
        patients = models.readallPatients()
        with ui.row().classes('w-full'):
            ui.input('Nom du Patient').style('width:18%').classes('bg-grey-1')
            select1 = ui.select(["Newest First", "Oldest First"], value="Newest First").style('width:18%').classes(
                'bg-grey-1')
            select2 = ui.select(["Home", "Femme", "Tous"], value="Femme").style('width:18%').classes('bg-grey-1')
            with ui.input('Date', on_change=lambda: menu.close()).style('width:18%').classes('bg-grey-1') as datefilter:
                with datefilter.add_slot('append'):
                    ui.icon('edit_calendar').on('click', lambda: menu.open()).classes('cursor-pointer')
                with ui.menu() as menu:
                    ui.date().bind_value(datefilter)
            ui.button(icon='search', color='green-6').style('width:20%;height:55px').classes('text-white')
        today = date.today()
        with ui.grid(columns='auto 2fr 1fr 1fr 1fr 1fr auto').classes('w-full gap-0'):
            for _ in range(1):
                ui.label('#').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                ui.label('Patient').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                ui.label('Created at').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                ui.label('Gender').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                ui.label('Email').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                ui.label('Age').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
                ui.label('Actions').classes('border p-1 bg-grey-2 font-bold').style('text-align:center')
            for i in patients:
                ui.label(f'{i.id}').classes('font-bold').style('margin-top:15px;margin-bottom:5px')
                with ui.row().classes('w-full'):
                    with ui.avatar().style('margin-top:5px;margin-bottom:5px'):
                        ui.image(f'/static/{i.photoProfil}')
                    with ui.column().classes('gap-0'):
                        nom = ui.label(f'{i.nomPatient}').style('padding-bottom:0px').classes(
                            'text-h7 text-black text-bold').style('margin-top:5px')
                        ui.label(f'{i.numTel}').style('padding-top:0px').classes('text-h7 text-grey')
                ui.label(f'{i.numTel}').classes('font-bold').style('text-align:center').style(
                    'margin-top:15px;margin-bottom:5px')
                ui.label(f'{i.sexe}').classes('text-green font-bold').style('text-align:center').style(
                    'margin-top:15px;margin-bottom:5px')
                ui.label(f'{i.email}').classes('font-bold').style('text-align:center').style(
                    'margin-top:15px;margin-bottom:5px')
                ui.label(f'{today.year - i.dateNaissance.year}').classes('font-bold').style('text-align:center').style(
                    'margin-top:15px;margin-bottom:5px')
                #ui.button(icon='edit').classes('font-bold bg-grey-2 text-black w-5/6').style('margin-top:15px;margin-bottom:5px')
                with ui.expansion(icon='edit').classes('font-bold bg-white text-black w-full').style(
                        'margin-top:15px;margin-bottom:5px'):
                    with ui.row().classes('w-full'):
                        ui.button('Voir', icon='visibility', color='green',
                                  on_click=lambda i=i: ui.navigate.to(f'View_patient/{i.id}')).classes('text-white')
                        ui.button('Supprimer', icon='delete', color='green').classes('text-white')
        with ui.page_sticky(position='bottom-right', x_offset=20, y_offset=20):
            ui.button(icon='add_circle', color='green', on_click=lambda: ui.navigate.to('Create_patient')).props('fab')


def Create_patientDash():
    h = '/static/profile_pic.png'

    def up(e):
        nonlocal h
        filename = e.name
        h = filename
        print("h = ", h)
        data64 = base64.b64encode(e.content.read())
        with open(f'static/{filename}', 'wb') as f:
            f.write(base64.b64decode(data64))
            ui.notify('l`image à été bien enregistré')

    with ui.row().classes('w-full'):
        ui.button(icon='arrow_back', color='white', on_click=lambda: ui.navigate.back()).classes('text-black')
        ui.label('Create Patient').classes('text-h5 text-black font-bold')
    with ui.card().classes('w-full'):
        with ui.row().classes('w-full'):
            with ui.column().style('width:30%'):
                ui.label('Photo de Profil :').classes('text-h6 text-black')
                ui.upload(on_upload=lambda e: up(e)).classes('bg-white').style('width:100%;height:295px').props(
                    'color="green"')
            with ui.column().style('width:68%'):
                ui.label('Nom et Prénom :').classes('text-h6 text-black')
                a = ui.input().classes('w-full').props('outlined')
                ui.label('Numéro de Téléphone :').classes('text-h6 text-black')
                b = ui.input().classes('w-full').props('outlined')
                ui.label('Email :').classes('text-h6 text-black')
                c = ui.input().classes('w-full').props('outlined')
        with ui.row().classes('w-full'):
            with ui.column().style('width:49%'):
                ui.label('Sexe :').classes('text-h6 text-black')
                d = select3 = ui.select(["Homme", "Femme"], value="Femme").style('width:100%').classes(
                    'bg-white').props('outlined')
            with ui.column().style('width:49%'):
                ui.label('Emergency Contact :').classes('text-h6 text-black')
                e = ui.input().classes('w-full').props('outlined').style('width:100%')
        with ui.row().classes('w-full'):
            with ui.column().style('width:49%'):
                ui.label('Date de Naissence :').classes('text-h6 text-black')
                with ui.input('Date de Naissence', on_change=lambda: menu.close()).style('width:100%').props(
                        'outlined') as date1:
                    with date1.add_slot('append'):
                        ui.icon('edit_calendar').on('click', lambda: menu.open()).classes('cursor-pointer')
                    with ui.menu() as menu:
                        ui.date().bind_value(date1)
            with ui.column().style('width:49%'):
                ui.label('Adresse :').classes('text-h6 text-black')
                g = ui.input().classes('w-full').props('outlined').style('width:100%')
        ui.button('Save Record', icon='save', color='green',
                  on_click=lambda: models.newPatient(a.value, b.value, c.value, d.value, e.value, date1.value, g.value,
                                                     date.today(), h)).classes('w-full text-white')
