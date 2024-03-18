from fastapi import FastAPI

app = FastAPI()

@app.get("/id/{serial}")
def check_id(serial: str):
    parts = serial.split('.')
    if len(parts) != 3:
        return "سریال شناسنامه باید شامل سه بخش باشد"

    first = parts[0]
    second = parts[1]
    third = parts[2]

    if len(first) != 1:
        return "اولین بخش سریال شناسنامه باید شامل یک حرف باشد"
    if not ('آ' <= first <= 'ی'):
        return "اولین بخش سریال شناسنامه باید یکی از حروف الفبای فارسی باشد"

    if len(second) != 2:
        return "دومین بخش سریال شناسنامه باید شامل ۲ رقم باشد"
    if not second.isdigit():
        return "دومین بخش سریال شناسنامه باید عددی باشد"

    if len(third) != 6:
        return "سومین بخش سریال شناسنامه باید شامل ۶ رقم باشد"
    if not third.isdigit():
        return "سومین بخش سریال شناسنامه باید عددی باشد"

    return "فرمت سریال شناسنامه درست است"
