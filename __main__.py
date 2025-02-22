from fastapi import FastAPI
import uvicorn


app = FastAPI()


@app.get("/healthcheck")
def healthcheck() -> dict:
    return dict()


def main() -> None:
    uvicorn.run(app, host="0.0.0.0")


if __name__ == "__main__":
    main()
