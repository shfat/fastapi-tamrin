from fastapi import FastAPI

app = FastAPI()


@app.get("/birthdate/{date}")
def check_birthdate(date: str):
    if len(date) != 10:
        return "تاریخ وارد شده باید دقیقاً ۱۰ کاراکتر باشد و بخش ها با نقطه از هم جدا شوند"

    parts = date.split('.')
    if len(parts) != 3:
        return "تاریخ باید دارای سه بخش (به ترتیب سال, ماه و روز) باشد"

    year, month, day = parts
    if not (year.isdigit() and month.isdigit() and day.isdigit()):
        return "تاریخ وارد شده باید شامل اعداد باشد"

    year = int(year)
    month = int(month)
    day = int(day)

    if not (1300 <= year <= 1402):
        return "سال وارد شده باید بین 1300 تا 1402 باشد"

    if not (1 <= month <= 12):
        return "ماه وارد شده باید بین 1 تا 12 باشد"

    if (1 <= month <= 6) and not (1 <= day <= 31):
            return "روز وارد شده باید بین 1 تا 31 باشد"

    if (7 <= month <= 12) and not (1 <= day <= 30):
            return "روز وارد شده باید بین 1 تا 30 باشد"

    return "فرمت تاریخ تولد درست است"
