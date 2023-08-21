from fastapi import FastAPI
from pydantic import BaseModel


class HealthCheck(BaseModel):
    status: str = "OK"


def create_app() -> FastAPI:
    app = FastAPI(title="fastapi-eb-template", debug=True)

    @app.get(
        "/health",
        status_code=200,
        summary="Perform a Health Check",
        response_model=HealthCheck,
        tags=["Health"],
    )
    def health_check() -> HealthCheck:
        return HealthCheck(status="OK")

    return app


app = create_app()

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", reload=True, log_level="debug")
