from fastapi import FastAPI

app = FastAPI()

valid_majors = ["مهندسی کامپیوتر", "مهندسی برق(الکترونیک)", "مهندسی برق(قدرت)", "مهندسی مکانیک و پلیمر", "مهندسی معدن",
                "مهندسی عمران", "مهندسی شهرسازی"]


@app.get("/check_major/{major}")
def check_major(major: str):
    if major in valid_majors:
        return f"رشته تحصیلی {major} معتبر است و متعلق به دانشکده فنی و مهندسی می باشد"
    else:
        return f"رشته تحصیلی {major} معتبر نیست"
