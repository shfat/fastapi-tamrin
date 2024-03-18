from fastapi import FastAPI

app = FastAPI()


@app.get('/{name}')
def func(name: str):
    if len(name) > 10:
        return f".نام وارد شده نباید بیشتر از 10 کاراکتر باشد"

    for char in name:
        if not ('آ' <= char <= 'ی'):
            return f"نام وارد شده فقط  باید حاوی حروف فارسی باشد و نباید حاوی عدد, علائم خاص یا فاصله باشد"

    return name
