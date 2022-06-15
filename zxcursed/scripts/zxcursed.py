import uvicorn


def main():
    uvicorn.run("zxcursed.main:app", host="127.0.0.1", port=8080, reload=True)
