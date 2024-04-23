from starlette.responses import RedirectResponse
import fastapi

router = fastapi.APIRouter(tags=["health check"])


@router.get("/")
async def main():
    """
    Redirects to the FastAPI documentation page.

    Returns:
        RedirectResponse: Redirects to the "/docs/" URL.
    """
    return RedirectResponse(url="/docs/")


@router.get("/health-checker")
async def hello_world():
    """
    Checks the health status of the API.

    Returns:
        dict: A dictionary containing a ping-pong message indicating the API is running.
    """
    return {"Ping": "Pong"}, 200
