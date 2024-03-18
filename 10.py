from fastapi import FastAPI

app = FastAPI()


@app.get("/check_landline/{landline}")
def check_landline(landline: str):
    if landline.count('_') != 1:
        return f"شماره تلفن وارد شده باید دارای دو بخش پیش شماره و شماره ثابت باشد و با _ از هم جدا شوند"

    parts = landline.split('_')
    first = parts[0]
    second = parts[1]

    if len(first) != 3 or len(second) != 8:
        return f"پیش شماره باید سه رقمی و شماره تلفن ثابت باید هشت رقمی باشد"

    if not (first.isdigit() and second.isdigit()):
        return f"شماره تلفن باید به عدد وارد شود"

    return f"شماره تلفن ثابت وارد شده معتبر است"
