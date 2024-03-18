from fastapi import FastAPI

app = FastAPI()

valid_faculty = {
    "فنی و مهندسی",
    "علوم پایه",
    "علوم انسانی",
    "دامپزشکی",
    "اقتصاد",
    "کشاورزی",
    "منابع طبیعی"
}

@app.get("/check_faculty/{faculty}")
def check_faculty(faculty: str):
    if faculty in valid_faculty:
        return f"دانشکده {faculty} معتبر است"
    else:
        return f"دانشکده {faculty} معتبر نیست"
