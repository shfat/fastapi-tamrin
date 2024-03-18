from fastapi import FastAPI

app = FastAPI()

@app.get("/marital_status/{marital}")
def marital_status(marital: str):
    if marital == "مجرد" or marital == "متاهل":
        return f"وضعیت تاهل {marital} معتبر است"
    else:
        return f"وضعیت تاهل {marital} معتبر نیست"
