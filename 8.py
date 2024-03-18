from fastapi import FastAPI

app = FastAPI()

@app.get("/check/{postal_code}")
def check(postal_code: str):
    if len(postal_code) != 10 or not postal_code.isdigit():
        return f"کد پستی وارد شده معتبر نیست"
    else:
        return f"کد پستی وارد شده معتبر است"
