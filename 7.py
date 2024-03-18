from fastapi import FastAPI

app = FastAPI()

@app.get("/address/{address}")
def check(address: str):
    if len(address) <= 100:
        return "آدرس وارد شده معتبر است"
    else:
        return "طول آدرس بیشتر از حد مجاز (100 کاراکتر) است"