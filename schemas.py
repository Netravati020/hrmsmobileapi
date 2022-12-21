from datetime import datetime, date, time
from pydantic import BaseModel
from sqlalchemy import DateTime
from typing import Optional



# class User(BaseModel):
#
#     user_id:Optional[str]
#     name:Optional[str]
#     password:Optional[str]
#     email:Optional[str]
#
#
# class Login(BaseModel):
#     purchase_id: str
#     password:str
#
#     class Config:
#         orm_mode = True
#
#
# class Token(BaseModel):
#     access_token: str
#     token_type: str
#
#     class Config:
#         orm_mode = True
#
# class TokenData(BaseModel):
#     purchase_id: str
#
#     class Config:
#         orm_mode = True
#
# class newuser(BaseModel):
#
#     name:str
#
#     class Config:
#         orm_mode = True
# class leavstatus(BaseModel):
#
#     status:str
#
#     class Config:
#         orm_mode = True
#
# class Leave(BaseModel):
#     employee_id :str
#     name :Optional[str]
#     fromdate :Optional[date]
#     todate :Optional[date]
#     days :Optional[int]
#     leave_type:Optional[str]
#     reason :str
#     status:str
#
#     class Config:
#         arbitrary_types_allowed = True
#
# class punch(BaseModel):
#
#     Date :Optional[date]
#     intime :Optional[time]
#     outtime :Optional[time]
#     totaltime:Optional[time]
#     attendance :Optional[str]
#     payroll :Optional[str]
#
#     class Config:
#         orm_mode = True
#
# class basicinfo(BaseModel):
#     branch: Optional[str]
#     department: Optional[str]
#     doj: Optional[str]
#     dob: Optional[str]
#     phone: Optional[str]
#
#     class Config:
#         orm_mode = True
#
# class Task(BaseModel):
#     meeting_name: Optional[str]
#     deadline: Optional[str]
#     priority: Optional[str]
#     update_status: Optional[str]
#     edit_status: Optional[str]
#     re_assign: Optional[str]
#
#     class Config:
#         orm_mode = True
#
# class Retirement(BaseModel):
#     emp_dob : Optional[date]
#     age:Optional[int]
#     date_time :Optional[datetime]
#
#     month_time :Optional[int]
#
#     retirement_day :Optional[date]
#
# class Personaldetail(BaseModel):
#     personal_mobile :Optional[int]
#     personal_email :Optional[str]
#     official_mobile:Optional[int]
#     official_email:Optional[str]
#     emergency_contact_person:Optional[str]
#     emergency_contact_number :Optional[int]
#
# class Editpersonal(BaseModel):
#     official_mobile: Optional[int]
#
# class Educationaldetail(BaseModel):
#     type :str
#     course :str
#     passed_out_year :int
#     percentage :float
#     registration_No :str
#
# class Gravience(BaseModel):
#     name :Optional[str]
#     developer :Optional[str]
#     branch :Optional[str]
#     gravience_type :Optional[str]
#     gravience_description :Optional[str]
#
# class Resign(BaseModel):
#     Employeename :Optional[str]
#     department :Optional[str]
#     resignation_reason :Optional[str]
#     last_workingday:date

class Educational(BaseModel):
    empid:Optional[str]
    type :Optional[str]
    course :Optional[str]
    passout :Optional[int]
    percentage :Optional[float]
    reg_number :Optional[str]
    created_by:Optional[str]
    created_on:Optional[datetime]

class updateedu(BaseModel):
    course:str

class Emplydetails(BaseModel):
    empid:Optional[str]
    password:Optional[str]
    mobile_password:Optional[str]
    employee_name:Optional[str]
    title:Optional[str]
    first_name:Optional[str]
    middle_name:Optional[str]
    last_name:Optional[str]
    state:Optional[str]
    city:Optional[str]
    pincode:Optional[str]
    branch:Optional[str]
    branch_state:Optional[str]
    designation:Optional[str]
    grade:Optional[str]
    cost_center:Optional[str]
    doj:Optional[date]
    last_working_datedate:Optional[date]
    left_reason:Optional[str]
    seperation_type:Optional[str]
    reason_type:Optional[str]
    rehire:Optional[str]
    date_of_birthdate:Optional[date]
    reporting_to:Optional[str]
    reporting_officer:Optional[str]
    directory:Optional[str]
    department:Optional[str]
    sub_department:Optional[str]
    quality_category:Optional[str]
    department_eff_date:Optional[date]
    band_grade:Optional[str]
    band_grade_eff_date:Optional[date]
    position:Optional[str]
    employment_type:Optional[str]
    employe_type_eff_date:Optional[date]
    off_emp_id:Optional[str]
    off_mobile:Optional[int]
    roles:Optional[str]
    branch_access:Optional[str]
    confirmation_status:Optional[str]
    date_of_confirmation:Optional[date]
    confirmation_due_date:Optional[date]
    date_of_last_promotion:Optional[date]
    tenure:Optional[float]
    total_experience:Optional[float]
    Category:Optional[str]
    FBP_value:Optional[str]
    Gross:Optional[int]
    ctc:Optional[int]
    annual_variable_pay:Optional[int]
    annual_ctc:Optional[int]
    increment_date:Optional[date]
    tds_status:Optional[str]
    payment_mode:Optional[str]
    ac_number:Optional[str]
    bank_name:Optional[str]
    ifsc:Optional[str]
    esi_status:Optional[str]
    esi:Optional[str]
    uan:Optional[str]
    pan:Optional[str]
    aadhar:Optional[str]
    aadhar_ref:Optional[str]
    pf_status:Optional[str]
    pf:Optional[str]
    passport:Optional[str]
    driving:Optional[str]
    retirement_date:Optional[date]
    status:Optional[str]
    notice_period:Optional[str]
    resignation_date:Optional[date]
    mode_of_separation:Optional[str]
    assigned_shift:Optional[str]
    weekoffday:Optional[str]
    onduty:Optional[str]
    default_shift_eff_date:Optional[date]
    gender:Optional[str]
    father_name:Optional[str]
    personal_mobile:Optional[int]
    personal_email:Optional[str]
    placeofbirth:Optional[str]
    age:Optional[int]
    nationality:Optional[str]
    religion:Optional[str]
    marital_status:Optional[str]
    spouse_name:Optional[str]
    noofchildren:Optional[int]
    wedding_date:Optional[date]
    nom_name:Optional[str]
    nom_rel:Optional[str]
    nom_per:Optional[str]
    nom_name2:Optional[str]
    nom_rel2:Optional[str]
    nom_per2:Optional[str]
    nom_name3:Optional[str]
    nom_rel3:Optional[str]
    nom_per3:Optional[str]
    present_address:Optional[str]
    present_state:Optional[str]
    permanent_address:Optional[str]
    permanent_state:Optional[str]
    blood_group:Optional[str]
    emergency_contact_person:Optional[str]
    emergency_landline:Optional[str]
    emergency_mobile:Optional[int]
    physically_handicapped:Optional[str]
    nps_status:Optional[str]
    pt_state:Optional[str]
    countries:Optional[str]
    casual_leave:Optional[int]
    compen_off:Optional[int]
    earn_leave:Optional[int]
    on_duty:Optional[int]
    optional_holiday:Optional[int]
    sick_leave:Optional[int]
    week_off:Optional[int]
    created_byname:Optional[str]
    created_byempid:Optional[str]
    created_on:Optional[date]
    created_time:Optional[time]
    at_work_hrs:Optional[time]
    brand_calls:Optional[str]
    pt_status:Optional[str]
    emp_image:Optional[str]
    appointment_letter:Optional[str]
    app_uploaded_on:Optional[datetime]
    app_uploaded_by:Optional[str]
    increment_letter:Optional[str]
    incr_uploaded_on:Optional[datetime]
    incr_uploaded_by:Optional[str]
    bgv_letter:Optional[str]
    bgv_uploaded_on:Optional[datetime]
    bgv_uploaded_by:Optional[str]
    international:Optional[str]
    issue_tracker:Optional[int]
    login_date:Optional[date]
    login_time:Optional[time]
    logout_date:Optional[date]
    logout_time:Optional[time]
    os_version:Optional[str]
    model:Optional[str]
    udid:Optional[str]
    tokenid:Optional[str]
    change_pass_ip:Optional[str]
    change_pass_on:Optional[datetime]
    master_access:Optional[int]
    recruitment:Optional[int]
    mrf_access:Optional[str]
    onboarding:Optional[int]
    pms:Optional[str]
    payroll_upload:Optional[int]
    payroll_run:Optional[int]
    payroll_branch:Optional[int]
    payroll_paysheets:Optional[int]
    leaveattendance:Optional[int]
    otreport:Optional[str]
    tdsreport:Optional[int]
    essreport:Optional[int]
    kyns_report:Optional[int]
    exitinterview:Optional[int]
    qrstatus:Optional[int]
    task_manager:Optional[int]
    license:Optional[int]
    reports_access:Optional[int]
    refname1:Optional[str]
    refmail1:Optional[str]
    refnum1:Optional[int]
    refdep1:Optional[str]
    refdes1:Optional[str]
    refname2:Optional[int]
    refmail2:Optional[str]
    refnum2:Optional[int]
    refdep2:Optional[str]
    refdes2:Optional[str]
    refname3:Optional[str]
    refmail3:Optional[str]
    refnum3:Optional[int]
    refdep3:Optional[str]
    refdes3:Optional[str]
    refname4:Optional[str]
    refmail4:Optional[str]
    refnum4:Optional[int]
    refdep4:Optional[str]
    refdes4:Optional[str]
    refname5:Optional[str]
    refmail5:Optional[str]
    refnum5:Optional[int]
    refdep5:Optional[str]
    refdes5:Optional[str]
    accesskey:Optional[str]
    androidpermissions:Optional[str]
    androidsubmenu:Optional[str]
    androiddashboard:Optional[str]
    IS_ADMIN:Optional[str]
    code:Optional[str]
    risk_allowance:Optional[str]
    risk_amount:Optional[str]

    class Config:
        orm_mode = True

class personalup(BaseModel):
    personal_mobile:int

    class Config:
        orm_mode = True

class HRpay(BaseModel):
    month :Optional[str]
    year :Optional[str]
    start_date :Optional[date]
    end_date :Optional[date]
    accessdate :Optional[date]
    days :Optional[int]
    class Config:
        orm_mode = True

class Leave(BaseModel):
    empid :Optional[str]
    emp_name :Optional[str]
    leave_type:Optional[str]
    applied_date :Optional[date]
    applied_time :Optional[time]
    from_date :Optional[date]
    to_date :Optional[date]
    days :Optional[str]
    reason :Optional[str]
    status :Optional[str]
    attachment :Optional[str]
    employee_status :Optional[str]
    approver :Optional[str]
    approved_date :Optional[datetime]
    source :Optional[str]
    branch :Optional[str]
    cancelled_by :Optional[str]
    cancelled_on :Optional[datetime]

    class Config:
        orm_mode = True

class Internationalpatient(BaseModel):
    transid:Optional[str]
    title :Optional[str]
    fullname  :Optional[str]
    passport :Optional[str]
    nationality :Optional[str]
    empid  :Optional[str]
    empname :Optional[str]
    createdon :Optional[datetime]
    updateon:Optional[datetime]
    ipaddress :Optional[datetime]

    class Config:
        orm_mode = True

class Embassy(BaseModel):
    embassy_name:Optional[str]
    type :Optional[str]
    address :Optional[str]
    telephone :Optional[str]
    fax :Optional[str]
    emailid :Optional[str]
    web :Optional[str]

    class Config:
        orm_mode = True

class Addtask(BaseModel):
    meeting_id: str
    meeting_name: str
    description: str
    deadline: str
    emp_id: str
    name: str
    department: str
    designation: str
    branch: str
    priority: str
    assign: str
    assign_remarks: str
    assign_status: str
    app_rej_on: date
    status: str
    remarks: str
    document_file: str
    completed_time: time
    created_by: str
    created_on: time

    class Config:
        orm_mode = True

class compnsatoryoff(BaseModel):
    empid :Optional[str]
    emp_name :Optional[str]
    leave_type :Optional[str]
    applied_date :Optional[date]
    applied_time :Optional[time]
    from_date :Optional[date]
    to_date :Optional[date]
    days:Optional[int]
    reason :Optional[str]
    status:Optional[str]
    approver :Optional[str]
    approved_date :Optional[datetime]
    branch :Optional[str]
    source :Optional[str]
    extra: Optional[time]
    type :Optional[str]

    class Config:
        orm_mode = True

class Updatecomp(BaseModel):
    status:str

    class Config:
        orm_mode = True

class Landans(BaseModel):
    quiz_id :Optional[int]
    question_id :Optional[int]
    option_selected :Optional[str]
    ans_status:Optional[int]
    empid :Optional[str]
    date_time :Optional[datetime]
    attempt :Optional[int]


class Landresult(BaseModel):
    quiz_id:Optional[int]
    empid :Optional[str]
    totalques :Optional[int]
    totalans : Optional[int]
    rightans : Optional[int]
    wrongans :Optional[int]
    date_time: Optional[datetime]
    attempt_count : Optional[int]
    result :Optional[str]
    score :Optional[str]
    class Config:
        orm_mode = True

class Financetime(BaseModel):
    work_date :date
    day :str
    work_done  :str
    time_spent  :str
    type  :str
    frequency  :str
    activity  :str
    department :str
    created_by  :str
    report_to  :str
    created_on: datetime

    class Config:
        orm_mode = True

class Compapprove(BaseModel):
    status:str
    approved_date:datetime

    class Config:
        orm_mode = True

class Leavecredits(BaseModel):
    empid :str
    employee_name :str
    credit_date :date
    credit_time :time
    leave_type :str
    opening_balance :int
    year_credit :int
    credit :int
    debit :int
    encashment :int
    credited_empid :str
    expity_date :date
    used_status :str
    comp_id :str
    source :str

