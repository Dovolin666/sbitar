from pony.orm import *
import datetime
from nicegui import ui

db = Database()  # We'll connect to the database in 'database.py'


class Patients(db.Entity):
    nomPatient = Required(str)
    numTel = Optional(str)
    email = Required(str)
    sexe = Optional(str)
    contactUrgence = Optional(str)
    dateNaissance = Optional(datetime.date)
    adresse = Optional(str)
    photoProfil = Optional(str)
    createdAt = Optional(datetime.date)


class PatientMedRecords(db.Entity):
    refNumber = Required(int)
    patientId = Required(int)
    nomDocteur = Required(str)
    plaintes = Optional(str)
    diagnostic = Optional(str)
    signesVitaux = Optional(str)
    invoiceGenerated = Optional(bool)
    dateCreation = Required(datetime.date)


class PatientTreatments(db.Entity):
    recordId = Required(int)
    patientId = Required(int)
    nomService = Optional(str)
    prixService = Optional(float)


class PatientMedicins(db.Entity):
    recordId = Required(int)
    patientId = Required(int)
    nomMedicin = Required(str)
    prix = Optional(float)
    instructions = Optional(str)
    quantity = Required(float)
    dosageQty = Required(float)
    dosage = Optional(str)


class PatientAttachments(db.Entity):
    recordId = Required(int)
    patientId = Required(int)
    nomFichier = Optional(str)

class PatientFiles(db.Entity):
    patientId = Required(int)
    nomFichier = Optional(str)
class Invoices(db.Entity):
    patientId = Required(int)
    recordId = Required(int)
    createddate = Required(datetime.date)
    duedate = Required(datetime.date)
    discount = Optional(float)
    tax = Optional(float)
    notes = Optional(str)


class Payments(db.Entity):
    patientId = Required(int)
    invoiceId = Required(int)
    createddate = Required(datetime.date)
    duedate = Required(datetime.date)
    discount = Optional(float)
    tax = Optional(float)
    statut = Required(str)
    methode = Required(str)
    notes = Optional(str)
    amount = Required(float)


class Doctors(db.Entity):
    photoProfil = Optional(str)
    nom = Required(str)
    email = Required(str)
    motpass = Required(str)
    numTel = Optional(str)
    specialite = Optional(str)


class DoctorsAccess(db.Entity):
    doctorId = Required(int)

    patientsRead = Optional(bool)
    patientsEdit = Optional(bool)
    patientsUpdate = Optional(bool)
    patientsDelete = Optional(bool)

    invoicesRead = Optional(bool)
    invoicesEdit = Optional(bool)
    invoicesUpdate = Optional(bool)
    invoicesDelete = Optional(bool)

    appointmentRead = Optional(bool)
    appointmentEdit = Optional(bool)
    appointmentUpdate = Optional(bool)
    appointmentDelete = Optional(bool)

    paymentsRead = Optional(bool)
    paymentsEdit = Optional(bool)
    paymentsUpdate = Optional(bool)
    paymentsDelete = Optional(bool)


class Medicines(db.Entity):
    nomMedicin = Required(str)
    measure = Required(str)
    prix = Required(float)
    inStock = Required(float)
    description = Optional(str)


class Services(db.Entity):
    nomService = Required(str)
    prix = Required(float)
    description = Optional(str)
    enabled = Optional(bool)


class Appointments(db.Entity):
    patientId = Required(int)
    butVisite = Optional(str)
    dateVisite = Required(datetime.date)
    heurDebut = Required(datetime.time)
    heurFin = Required(datetime.time)
    doctorId = Required(int)
    statut = Optional(str)
    chambre = Optional(str)
    description = Optional(str)


class Staffs(db.Entity):
    photoProfil = Optional(str)
    nom = Required(str)
    email = Required(str)
    motpass = Required(str)
    numTel = Optional(str)
    role = Optional(str)


class StaffAccess(db.Entity):
    staffId = Required(int)

    patientsRead = Optional(bool)
    patientsEdit = Optional(bool)
    patientsUpdate = Optional(bool)
    patientsDelete = Optional(bool)

    invoicesRead = Optional(bool)
    invoicesEdit = Optional(bool)
    invoicesUpdate = Optional(bool)
    invoicesDelete = Optional(bool)

    appointmentRead = Optional(bool)
    appointmentEdit = Optional(bool)
    appointmentUpdate = Optional(bool)
    appointmentDelete = Optional(bool)

    paymentsRead = Optional(bool)
    paymentsEdit = Optional(bool)
    paymentsUpdate = Optional(bool)
    paymentsDelete = Optional(bool)


db.bind(provider='sqlite', filename='database2.sqlite', create_db=True)
db.generate_mapping(create_tables=True)


@db_session
def newMedicine(a, b, c, d, e, f):
    try:
        medicine = Medicines(nomMedicin=a, measure=b, prix=c, inStock=d, description=e)
        ui.notify('les données ont bien été enregistrées')
        f.close()
        ui.navigate.to('/medicine')
    except Exception as ex:
        ui.notify(f'Erreur : {ex}')


@db_session
def readallMedicin():
    try:
        meds = select(k for k in Medicines)[:]
        return meds
    except Exception as e:
        ui.notify(f'Erreur : {e}')


@db_session
def readOneMedicine(medicineId):
    medicine = Medicines.get(id=medicineId)
    return medicine
    ui.notify('les données ont bien été actualisé')


@db_session
def readOneMedicineByName(medicineName):
    medicine = Medicines.get(nomMedicin=medicineName)
    return medicine
    ui.notify('les données ont bien été actualisé')


@db_session
def editMedicine(medicineId, a, b, c, d, e):
    try:
        medicine = Medicines.get(id=medicineId)
        medicine.set(nomMedicin=a, measure=b, prix=c, inStock=d, description=e)
        ui.notify('les données ont bien été modifié')
        ui.navigate.to('/medicine')
    except Exception as ex:
        ui.notify(f'Erreur : {ex}')


@db_session
def newService(a, b, c, d, e):
    try:
        service = Services(nomService=a, prix=b, description=c, enabled=d)
        ui.notify('les données ont bien été enregistrées')
        e.close()
        ui.navigate.to('/services')
    except Exception as ex:
        ui.notify(f'Erreur : {ex}')


@db_session
def readallServices():
    try:
        services = select(k for k in Services)[:]
        return services
    except Exception as e:
        ui.notify(f'Erreur : {e}')


@db_session
def readOneService(serviceId):
    service = Services.get(id=serviceId)
    return service
    ui.notify('les données ont bien été actualisé')


@db_session
def editService(serviceId, a, b, c, d):
    try:
        service = Services.get(id=serviceId)
        service.set(nomService=a, prix=b, description=c, enabled=d)
        ui.notify('les données ont bien été modifié')
        ui.navigate.to('/services')
    except Exception as ex:
        ui.notify(f'Erreur : {ex}')


@db_session
def newPatient(a, b, c, d, e, f, g, i, h):
    try:
        patient = Patients(nomPatient=a, numTel=b, email=c, sexe=d, contactUrgence=e, dateNaissance=f, adresse=g,
                           photoProfil=h, createdAt=i)
        ui.notify('les données ont bien été enregistrées')
        ui.navigate.to('/patients')
    except Exception as ex:
        ui.notify(f'Erreur : {ex}')


@db_session
def readallPatients():
    try:
        patients = select(k for k in Patients)[:]
        return patients
    except Exception as e:
        ui.notify(f'Erreur : {e}')


@db_session
def readOnePatient(patientid):
    patient = Patients.get(id=patientid)
    return patient
    ui.notify('les données ont bien été actualisé')


@db_session
def newMedicalRecord(x, a, b, c, d, e, f):
    try:
        patient = PatientMedRecords(refNumber=x, patientId=a, nomDocteur=b, plaintes=c, diagnostic=d, signesVitaux=e,
                                    dateCreation=f)
        ui.notify('les données ont bien été enregistrées')
        ui.navigate.to(f'/View_patient/{a}')
    except Exception as ex:
        ui.notify(f'Erreur : {ex}')


@db_session
def editMedicalRecord(x, a, b, c, d, e, f):
    try:
        patient = PatientMedRecords.get(refNumber=x)
        patient.set(refNumber=x, patientId=a, nomDocteur=b, plaintes=c, diagnostic=d, signesVitaux=e, dateCreation=f)
        ui.notify('les données ont bien été enregistrées')
        ui.navigate.to(f'/View_patient/{a}')
    except Exception as ex:
        ui.notify(f'Erreur : {ex}')
@db_session
def editMedicalRecordByInvoice(x, a):
        patient = PatientMedRecords.get(refNumber=x)
        patient.set(invoiceGenerated= a)


@db_session
def readOneMedicalRecord(refNumber):
    medrecord = PatientMedRecords.get(refNumber=refNumber)
    return medrecord
    ui.notify('les données ont bien été actualisé')


@db_session
def readallMedicalRecord(pid):
    try:
        medrecords = select(k for k in PatientMedRecords if k.patientId == pid)[:]
        return medrecords
    except Exception as e:
        ui.notify(f'Erreur : {e}')


@db_session
def newPatientMedicin(x, a, b, c, d, e, f, g, i):
    try:
        medicin = PatientMedicins(recordId=x, patientId=a, nomMedicin=b, prix=c, instructions=d, quantity=e,
                                  dosageQty=f, dosage=g)
        ui.notify('les données ont bien été enregistrées')
        i.close()
    except Exception as ex:
        ui.notify(f'Erreur : {ex}')


@db_session
def readallPatientsMedicines(recordid):
    try:
        medicines = select(k for k in PatientMedicins if k.recordId == recordid)[:]
        return medicines
    except Exception as e:
        ui.notify(f'Erreur : {e}')


@db_session
def newPatientServices(x, a, b, c):
    try:
        services = PatientTreatments(recordId=x, patientId=a, nomService=b, prixService=c)
    except Exception as ex:
        ui.notify(f'Erreur : {ex}')


@db_session
def readallPatientsServices(recordId):
    try:
        services = select(k for k in PatientTreatments if k.recordId == recordId)[:]
        return services
    except Exception as e:
        ui.notify(f'Erreur : {e}')


@db_session
def newPatientAttachments(x, a, b):
    try:
        newFile = PatientAttachments(recordId=x, patientId=a, nomFichier=b)
        ui.notify('les données ont bien été enregistrées')
    except Exception as ex:
        ui.notify(f'Erreur : {ex}')


@db_session
def readallPatientsAttachments(recordId):
    try:
        attachments = select(k for k in PatientAttachments if k.recordId == recordId)[:]
        return attachments
    except Exception as e:
        ui.notify(f'Erreur : {e}')

@db_session
def newPatientfile(a, b):
    try:
        newFile = PatientFiles(patientId=a, nomFichier=b)
        ui.notify('les données ont bien été enregistrées')
    except Exception as ex:
        ui.notify(f'Erreur : {ex}')

@db_session
def readallPatientFiles(patientId):
    try:
        files = select(k for k in PatientFiles if k.patientId == patientId)[:]
        return files
    except Exception as e:
        ui.notify(f'Erreur : {e}')
@db_session
def newDoctor(a, b, c, d, e, f, g):
    try:
        doctor = Doctors(photoProfil=a, nom=b, email=c, motpass=d, numTel=e, specialite=f)
        ui.notify('les données ont bien été enregistrées')
        g.close()
        ui.navigate.to('/doctors')
    except Exception as ex:
        ui.notify(f'Erreur : {ex}')

@db_session
def readOneDoctor(doctorId):
    doctor = Doctors.get(id=doctorId)
    return doctor
    ui.notify('les données ont bien été actualisé')
@db_session
def readallDoctors():
    try:
        doctors = select(k for k in Doctors)[:]
        return doctors
    except Exception as e:
        ui.notify(f'Erreur : {e}')


@db_session
def newStaff(a, b, c, d, e, f, g):
    try:
        newstaff = Staffs(photoProfil=a, nom=b, email=c, motpass=d, numTel=e, role=f)
        ui.notify('les données ont bien été enregistrées')
        g.close()
        ui.navigate.to('/staff')
    except Exception as ex:
        ui.notify(f'Erreur : {ex}')


@db_session
def readAllStaff():
    try:
        staffs = select(k for k in Staffs)[:]
        return staffs
    except Exception as e:
        ui.notify(f'Erreur : {e}')


@db_session
def newInvoice(a, x, b, c, d, e, f):
    try:
        newinvoice = Invoices(patientId=a, recordId =x,createddate=b, duedate=c, discount=d, tax=e, notes=f)
        ui.notify('les données ont bien été enregistrées')
        ui.navigate.to('/invoices')

    except Exception as ex:
        ui.notify(f'Erreur : {ex}')

@db_session
def readAllInvoices():
    try:
        invoices = select(k for k in Invoices)[:]
        return invoices
    except Exception as e:
        ui.notify(f'Erreur : {e}')

@db_session
def readAllInvoicesById(patientid):
    try:
        invoices = select(k for k in Invoices if k.patientId == patientid)[:]
        return invoices
    except Exception as e:
        ui.notify(f'Erreur : {e}')

@db_session
def readOneInvoice(invoiceId):
    invoice = Invoices.get(id=invoiceId)
    return invoice
    ui.notify('les données ont bien été actualisé')


@db_session
def newPayment(a, b, c, d, e, f, g, h, i,j):
    try:
        newpayment = Payments(patientId=a,createddate=b, duedate=c, discount=d, tax=e,statut =f,methode=g, notes=h, invoiceId=i,amount=j)
        ui.notify('les données ont bien été enregistrées')
        ui.navigate.to('/payments')

    except Exception as ex:
        ui.notify(f'Erreur : {ex}')


@db_session
def readAllPayments():
    try:
        payments = select(k for k in Payments)[:]
        return payments
    except Exception as e:
        ui.notify(f'Erreur : {e}')

@db_session
def readAllPaymentsById(patientId):
    try:
        payments = select(k for k in Payments if k.patientId == patientId)[:]
        return payments
    except Exception as e:
        ui.notify(f'Erreur : {e}')
@db_session
def readOnePayment(paymentId):
    payment = Payments.get(id=paymentId)
    return payment
    ui.notify('les données ont bien été actualisé')

@db_session
def newAppointment(a, b, c, d, e, f, g, h, i):
    try:
        newappointment = Appointments(patientId=a, doctorId=b, dateVisite=c, heurDebut=d, statut=e, chambre=f, description=g, butVisite=h, heurFin=i)
        ui.notify('les données ont bien été enregistrées')
        ui.navigate.to('/appointments')

    except Exception as ex:
        ui.notify(f'Erreur : {ex}')

@db_session
def readAllAppointments():
    try:
        appointments = select(k for k in Appointments)[:]
        return appointments
    except Exception as e:
        ui.notify(f'Erreur : {e}')

@db_session
def readAllAppointmentsById(patientId):
    try:
        appointments = select(k for k in Appointments if k.patientId == patientId)[:]
        return appointments
    except Exception as e:
        ui.notify(f'Erreur : {e}')
@db_session
def readOneAppointment(appointmentId):
    appointment = Appointments.get(id=appointmentId)
    return appointment
    ui.notify('les données ont bien été actualisé')

@db_session
def editAppointment(id, c, d, e, f, g, h, i):
    try:
        appointment = Appointments.get(id=id)
        appointment.dateVisite = c
        appointment.heurDebut = d
        appointment.statut = e
        appointment.chambre = f
        appointment.description = g
        appointment.butVisite = h
        appointment.heurFin = i
        ui.notify('les données ont bien été modifiées')
        ui.navigate.to('/appointments')

    except Exception as ex:
        ui.notify(f'Erreur : {ex}')