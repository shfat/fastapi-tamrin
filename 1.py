from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# الف

@app.get('/path/{StudentNumber}')
def StdN_path(StudentNumber: str):
    if len(StudentNumber) != 11:
        return f"شماره دانشجویی باید یازده رقم باشد. تعداد ارقام وارد شده نادرست است"
    if int(StudentNumber[0:3]) > 402 or int(StudentNumber[0:3]) < 400:
        return f"قسمت سال نادرست است"
    if int(StudentNumber[3:9]) != 114150:
        return f".قسمت ثابت نادرست است"
    if int(StudentNumber[9:11]) == 0:
        return f".قسمت اندیس نادرست است"
    else:
        return f".شماره دانشجویی وارد شده درست است"

# ب

@app.get('/query/')
def StdN_query(StudentNumber: str):
    if len(StudentNumber) != 11:
        return f"شماره دانشجویی باید یازده رقم باشد. تعداد ارقام وارد شده نادرست است"
    if int(StudentNumber[0:3]) > 402 or int(StudentNumber[0:3]) < 400:
        return f"قسمت سال نادرست است"
    if int(StudentNumber[3:9]) != 114150:
        return f".قسمت ثابت نادرست است"
    if int(StudentNumber[9:11]) == 0:
        return f".قسمت اندیس نادرست است"
    else:
        return f".شماره دانشجویی وارد شده درست است"

# ج

class StudentNumber(BaseModel):
    student_number: str

@app.post('/post/')
def StdN_post(stdn: StudentNumber):
    if len(stdn.student_number) != 11:
        return f"شماره دانشجویی باید یازده رقم باشد. تعداد ارقام وارد شده نادرست است"
    if int(stdn.student_number[0:3]) > 402 or int(stdn.student_number[0:3]) < 400:
        return f"قسمت سال نادرست است"
    if int(stdn.student_number[3:9]) != 114150:
        return f".قسمت ثابت نادرست است"
    if int(stdn.student_number[9:11]) == 0:
        return f".قسمت اندیس نادرست است"
    else:
        return f".شماره دانشجویی وارد شده درست است"
