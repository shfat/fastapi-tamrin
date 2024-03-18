from fastapi import FastAPI

app = FastAPI()

@app.get("/check_mobile/{mobile}")
def check_mobile(mobile: str):
    if len(mobile) != 11 or not mobile[2:].isdigit():
        return f"شماره تلفن همراه وارد شده معتبر نیست"
    if mobile[0:2] != "09":
        return f"شماره تلفن باید با 09 شروع شود"
    return f"شماره تلفن همراه وارد شده معتبر است"

