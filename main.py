import glob
import os
import parser
import shutil
from sqlalchemy import and_, not_, or_
from typing import Optional

import dateutil.utils
from dateutil.relativedelta import relativedelta
from fastapi import FastAPI, Depends, HTTPException, status, UploadFile,File
from fastapi.responses import FileResponse
from starlette.staticfiles import StaticFiles

import models
import schemas
import hashing
import tokn
import oauth
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
models.Base.metadata.create_all(bind=engine)
from datetime import datetime, date

app = FastAPI()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
 # craete user
@app.post('/log', tags=['login'])
def create_user(request: schemas.User, db:Session=Depends(get_db)):

    new_user= models.User(emp_id=request.emp_id,name=request.name,email=request.email,password=hashing.Hash.encrypt(request.password))

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


# user authentication
@app.post("/token", tags=['Authentication'])
async def login_access(request:OAuth2PasswordRequestForm = Depends(),db:Session=Depends(get_db)):
    user = db.query(models.User).filter(models.User.emp_id == request.username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Incorrect username or password")

    # if not hashing.Hash.verify(user.password, request.password):
    #     raise HTTPException(
    #         status_code=status.HTTP_404_NOT_FOUND,
    #         detail="Incorrect  password")

    access_token = tokn.create_access_token(data={"sub": user.emp_id})
    return {"access_token": access_token, "token_type": "bearer"}


# insert employee educational details
@app.post('/edu',tags=['Educational'])
def add_educat(request:schemas.Educational,db:Session=Depends(get_db),current_user: schemas.User=Depends(oauth.get_current_user)):
    edu= models.Educational(empid=request.empid,type=request.type,course=request.course,passout=request.passout,percentage=request.percentage,reg_number=request.reg_number,created_by=request.created_by,created_on=request.created_on)
    db.add(edu)
    db.commit()
    db.refresh(edu)
    return edu

# read employee educational details order by empoloyee pssout
@app.get('/', tags=['Educational'])
def educational(db:Session=Depends(get_db),current_user: schemas.User=Depends(oauth.get_current_user)):
    educational= db.query(models.Educational.sno,models.Educational.type,models.Educational.course,models.Educational.percentage,models.Educational.passout,models.Educational.reg_number).order_by(models.Educational.passout).first()
    return educational

# read employee details
@app.get('/empdetail',tags=['Employee details'])
def empdetail(db:Session=Depends(get_db),current_user: schemas.User=Depends(oauth.get_current_user)):
    emp=db.query(models.Employee_details).first()
    return emp

# update employee educational details
@app.patch('/{sno}', tags=['update education'])
def updateedu(sno, request: schemas.updateedu,db:Session=Depends(get_db)):
    emp =db.query(models.Educational).filter(models.Educational.sno==sno)
    if not emp:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Sorry some details missing {sno}")

    emp.update(dict(request))
    db.commit()

    return 'Education Details are updated'

# delete employee educational details
@app.delete('/{sno}', status_code=status.HTTP_200_OK, tags=['emp education delete'])
def delete(sno,  db:Session=Depends(get_db)):
    u=db.query(models.Educational).filter(models.Educational.sno == sno).delete(synchronize_session=False)
    if not u:
        raise HTTPException(status_code=status.HTTP_404_NOT_IMPLEMENTED, detail=f"Sorry some details missing {sno}")

    db.commit()
    return "Successfully deleted"



# view persional details
@app.get('/personal Info', tags=['personal info'])
def personal(access_key:str,db:Session=Depends(get_db),current_user: schemas.User=Depends(oauth.get_current_user)):
    personal=db.query(models.Employee_details.employee_name,models.Employee_details.doj,models.Employee_details.retirement_date,models.Employee_details.date_of_birth,models.Employee_details.gender,models.Employee_details.aadhar,models.Employee_details.pan,models.Employee_details.personal_mobile,models.Employee_details.personal_email,models.Employee_details.emergency_contact_person,models.Employee_details.emergency_mobile,models.Employee_details.physically_handicapped,models.Employee_details.marital_status,models.Employee_details.spouse_name,models.Employee_details.noofchildren,models.Employee_details.religion,models.Employee_details.father_name,models.Employee_details.present_address,models.Employee_details.city,models.Employee_details.present_state,models.Employee_details.pincode,models.Employee_details.blood_group,models.Employee_details.off_emp_id,models.Employee_details.off_mobile,models.Employee_details.nom_name,models.Employee_details.nom_rel,models.Employee_details.nom_per,models.Employee_details.nom_name2,models.Employee_details.nom_per2,models.Employee_details.nom_name3,models.Employee_details.nom_rel3,models.Employee_details.nom_per3).where(models.Employee_details.accesskey==access_key).all()
    return personal


# view status and qrstatus of employee
@app.get('/epmst',tags=['emp status'])
def empstatus(access_key:str,db:Session=Depends(get_db)):
    emp=db.query(models.Employee_details.status,models.Employee_details.qrstatus).where(models.Employee_details.accesskey==access_key).first()
    return emp

# team list view
@app.get('/teamlist', tags=['team list'])
def team(emp_id:str,db:Session=Depends(get_db)):
    team=db.query(models.Employee_details.empid,models.Employee_details.employee_name,models.Employee_details.designation,models.Employee_details.department,models.Employee_details.personal_mobile,models.Employee_details.branch,models.Employee_details.doj).where(models.Employee_details.reporting_to==emp_id,models.Employee_details.status=='Active').all()
    if not team:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Sorry some details missing ")
    return team

@app.post('/',tags=['hr payroll'])
def hpayroll(reque:schemas.HRpay,db:Session=Depends(get_db)):
    pay=models.HRpayrol(end_date=reque.end_date)
    endat=pay.end_date+relativedelta(month=3)
    payrol=models.HRpayrol(month=reque.month,year=reque.year,start_date=reque.start_date,end_date=reque.end_date,accessdate=reque.accessdate,days=reque.days)
    db.add(payrol)
    db.commit()
    db.refresh(payrol)
    return payrol,endat


@app.post('/leav',tags=['apply leave'])
def leave(request:schemas.Leave,db:Session=Depends(get_db)):
    leav=models.Leave_management(empid=request.empid,emp_name=request.emp_name,leave_type=request.leave_type,applied_date=request.applied_date,applied_time=request.applied_time,from_date=request.from_date,to_date=request.to_date,days=request.days,reason=request.reason,status=request.status,attachment=request.attachment,employee_status=request.employee_status,approver=request.approver,approved_date=request.approved_date,source=request.source,branch=request.branch,cancelled_by=request.cancelled_by,cancelled_on=request.cancelled_on)
    db.add(leav)
    db.commit()
    db.refresh(leav)
    return leav

@app.get('/leave1', tags=['apply leave1'])
def apply(emp_id:str,emp_id_reporting_to:str,db:Session=Depends(get_db)):
    applyleave=db.query(models.Employee_details.branch_state).where(models.Employee_details.empid==emp_id).first()
    applyleav=db.query(models.Employee_details.tokenid).where(models.Employee_details.empid==emp_id_reporting_to).first()

    return(applyleave,applyleav)

@app.post('/interbational',tags=['add attenders'])
def add_attender(request:schemas.Internationalpatient,db:Session=Depends(get_db)):
    add_attenders=models.Internationalptientatten(transid=request.transid,title=request.title,fullname=request.fullname,passport=request.passport,nationality=request.nationality,empid=request.empid,empname=request.empname,createdon=request.createdon,updateon=request.updateon,ipaddress=request.ipaddress)
    db.add(add_attenders)
    db.commit()
    db.refresh(add_attenders)
    return add_attenders

@app.get('/att',tags=['attendrs list'])
def list(trans_id:str,db:Session=Depends(get_db)):
    list=db.query(models.Internationalptientatten.sno,models.Internationalptientatten.title,models.Internationalptientatten.transid,models.Internationalptientatten.passport,models.Internationalptientatten.fullname,models.Internationalptientatten.nationality).where(models.Internationalptientatten.transid==trans_id).first()
    return list

@app.post('/addem',tags=['addembassy'])
def addemb(request:schemas.Embassy,db:Session=Depends(get_db)):
    addembassy=models.Embassy(embassy_name=request.embassy_name,type=request.type,address=request.address,telephone=request.telephone,fax=request.fax,emailid=request.emailid,web=request.web)
    db.add(addembassy)
    db.commit()
    db.refresh(addembassy)
    return addembassy

@app.post('/addtask',tags=['add task'])
def addtask(request:schemas.Addtask,db:Session=Depends(get_db)):
    task=models.Task(meeting_id=request.meeting_id,meeting_name=request.meeting_name,description=request.description,deadline=request.deadline,emp_id=request.emp_id,name=request.name,department=request.department,designation=request.designation,branch=request.branch,priority=request.priority,assign=request.assign,assign_remarks=request.assign_remarks,assign_status=request.assign_status,app_rej_on=request.app_rej_on,status=request.status,remarks=request.remarks,document_file=request.document_file,completed_time=request.completed_time,created_by=request.created_by,created_on=request.created_on)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

@app.get('/admin',tags=['admin attendance'])
def admin(emp_id:str,db:Session=Depends(get_db)):
    gravience=db.query(models.Grievance_map.empid,models.Grievance_map.branch,models.Grievance_map.type).where(models.Grievance_map.type!= 'Corporate Head',models.Grievance_map.empid==emp_id).first()
    return gravience

@app.post('/comp',tags=['compansatory off'])
def comp(request:schemas.compnsatoryoff,db:Session=Depends(get_db)):
    compansotory=models.Compansetoryoff(empid=request.empid,emp_name=request.emp_name,leave_type=request.leave_type,applied_date=request.applied_date,applied_time=request.applied_time,from_date=request.from_date,to_date=request.to_date,days=request.days,reason=request.reason,status=request.status,approver=request.approver,approved_date=request.approved_date,branch=request.branch,source=request.source,extra=request.extra,type=request.type)
    db.add(compansotory)
    db.commit()
    db.refresh(compansotory)
    return compansotory

@app.get('/holiday',tags=['leave type & attendance'])
def holiday(fdate:str,emp:str,employ_id:Optional[str]=None,da:Optional[str]=None,state:Optional[str]=None,dat:Optional[str]=None,db:Session=Depends(get_db)):
    holiday=db.query(models.Holidaytype.leavetype).where(models.Holidaytype.state==state,models.Holidaytype.date==dat,models.Holidaytype.status=="Yes").all()

    attendance=db.query(models.Attendance).where(models.Attendance.empid==employ_id,models.Attendance.date==da,models.Attendance.Attendance=="Present").all()
    compansotory=db.query(models.Compansetoryoff).filter(models.Compansetoryoff.from_date==fdate, models.Compansetoryoff.empid==emp,and_(models.Compansetoryoff.status!="Approved"), and_(models.Compansetoryoff.status!="Cancel"),and_(models.Compansetoryoff.status!="Applied")).all()
    return holiday,attendance, compansotory

@app.get('/at',tags=['attendance'])
def atten(fdate:date,tdate:date,emp_id:str,db:Session=Depends(get_db)):
    attendance=db.query(models.Attendance.date,models.Attendance.intime,models.Attendance.outtime,models.Attendance.twt,models.Attendance.payroll_status,models.Attendance.shift).filter(models.Attendance.empid==emp_id,models.Attendance.date.between(fdate,tdate)).order_by(models.Attendance.date).all()
    return attendance

@app.get('/auto',tags=['autosearch employee details'])
def auto(emp_id,db:Session=Depends(get_db)):
    autosearch=db.query(models.Employee_details.employee_name,models.Employee_details.empid).where(models.Employee_details.reporting_to==emp_id,models.Employee_details.status=="Active").all()
    return autosearch

@app.post('/c{sno}', tags=['cancel compoffleave'])
def cancellv(sno, request: schemas.Updatecomp,db:Session=Depends(get_db)):
    cancelcomp =db.query(models.Compansetoryoff).filter(models.Compansetoryoff.sno==sno)
    if not cancelcomp:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Sorry some details missing {sno}")

    cancelcomp.update(dict(request))
    db.commit()

    return 'You have cancelled Compensatory off'

@app.get('/cluster',tags=['cluster emphead'])
def cluster(branch:str,db:Session=Depends(get_db)):
    cluster=db.query(models.Employee_details.branch).where(models.Employee_details.branch!=branch).distinct().order_by(models.Employee_details.branch).all()
    return cluster

@app.get('/forgot',tags=['forgot password'])
def forg(emp_id:str,dob:str,db:Session=Depends(get_db)):
    forgot=db.query(models.Employee_details.date_of_birth).where(models.Employee_details.empid==emp_id,and_(models.Employee_details.date_of_birth==dob)).all()
    if not forgot:
        raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail=f"Your details not matched")

    return "your data matched"


@app.get('/lanans',tags=['landanswered'])
def la(emp_id,qz_id:str,db:Session=Depends(get_db)):
    laans=db.query(models.Landans.attempt).distinct().where(models.Landans.empid==emp_id, and_(models.Landans.quiz_id==qz_id)).count()
    return laans

@app.post('/landanswe',tags=['landanswered'])
def lananswer(request:schemas.Landans,db:Session=Depends(get_db)):
    queryland=models.Landans(quiz_id=request.quiz_id,question_id=request.question_id,option_selected=request.option_selected,ans_status=request.ans_status,empid=request.empid,date_time=request.date_time,attempt=request.attempt)
    db.add_all(queryland)
    db.commit()
    db.refresh(queryland)
    return queryland

@app.post('/lresult',tags=['landdresult'])
def lr(req:schemas.Landresult,db:Session=Depends(get_db)):
    landresult=models.Landqresult(quiz_id=req.quiz_id,empid=req.empid,totalques=req.totalques,totalans=req.totalans,rightans=req.rightans,wrongans=req.wrongans,date_time=req.date_time,attempt_count=req.attempt_count,result=req.result,score=req.score)

    db.add_all([landresult])
    db.commit()

    db.refresh(landresult)
    return landresult



@app.post('/finance',tags=['financetime sheet'])
def fi(request:schemas.Financetime,db:Session=Depends(get_db)):
    finance=models.Finatimesheet(work_date=request.work_date,day=request.day,work_done=request.work_done,time_spent=request.time_spent,type=request.type,frequency=request.frequency,activity=request.activity,department=request.department,created_by=request.created_by,report_to=request.report_to,created_on=request.created_on)
    db.add(finance)
    db.commit()
    db.refresh(finance)
    return finance

@app.get('/fintimesheet', tags=['timesheet list'])
def time(dept:str,fdate:date,tdate:date,emp_id:str,db:Session=Depends(get_db)):
    timeshet=db.query(models.Finatimesheet.sno,models.Finatimesheet.work_date,models.Finatimesheet.day,models.Finatimesheet.work_done,models.Finatimesheet.time_spent,models.Finatimesheet.type,models.Finatimesheet.frequency,models.Finatimesheet.activity,models.Finatimesheet.department,models.Finatimesheet.report_to,models.Finatimesheet.created_on,models.Finatimesheet.created_by).where(models.Finatimesheet.department==dept,models.Finatimesheet.created_on.between(fdate,tdate)),or_((models.Finatimesheet.report_to==emp_id),and_(models.Finatimesheet.created_on.between(fdate,tdate))).order_by(models.Finatimesheet.work_date)[::-1].all()
    return timeshet

@app.get('/lgrant',tags=['leave grantsumm'])
def leav(emp_id:str,db:Session=Depends(get_db)):
    grant=db.query(models.Compansetoryoff.sno,models.Compansetoryoff.leave_type,models.Compansetoryoff.applied_date,models.Compansetoryoff.from_date,models.Compansetoryoff.to_date,models.Compansetoryoff.days,models.Compansetoryoff.reason,models.Compansetoryoff.status).where(models.Compansetoryoff.empid==emp_id,models.Compansetoryoff.status!='Cancel').order_by(models.Compansetoryoff.sno).all()
    return grant

@app.get('/teamlv',tags=['team leave grant approved'])
def tmlvgrant(id:str,db:Session=Depends(get_db)):
    tmleave=db.query(models.Compansetoryoff.from_date).where(models.Compansetoryoff.sno==id,models.Compansetoryoff.status=='Pending').all()
    return tmleave

@app.put('/cmap',tags=['team leavgrant approve'])
def comapp(id, request: schemas.Compapprove,db:Session=Depends(get_db)):
    cm =db.query(models.Compansetoryoff).where(models.Compansetoryoff.sno==id,and_(models.Compansetoryoff.status=='Pending'))
    if not cm:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Sorry some details missing {id}")

    cm.update(dict(request))
    db.commit()

    return 'Compensatory Off Approved'

@app.put('/tmreject',tags=['team leavgrant reject'])
def lvrej(id,request:schemas.Compapprove,db:Session=Depends(get_db)):
    tr=db.query(models.Compansetoryoff).where(models.Compansetoryoff.sno==id,and_(models.Compansetoryoff.status=='Pending'))
    if not tr:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Sorry some details missing {id}")

    tr.update(dict(request))
    db.commit()

    return 'Compensatory Off rejected'

# update employee personal details
@app.post('/{sno}', tags=['update personal details'])
def updatpersonal(sno, request: schemas.personalup,db:Session=Depends(get_db)):
    per =db.query(models.Employee_details).filter(models.Employee_details.sno==sno)
    if not per:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Sorry some details missing {sno}")

    per.update(dict(request))
    db.commit()

    return 'personal Details are updated'
