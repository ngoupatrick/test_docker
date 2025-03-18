from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .middleware import Mid_Factor

from fastapi.responses import FileResponse


factor = Mid_Factor()

port = factor.PORT
version = factor.VERSION_APP
appname = factor.APP_NAME
api_base = factor.BACKEND_API_BASE
devname = factor.DEVNAME
github_url = factor.GITHUB_URL
email = factor.EMAIL
version_prefix =f"{factor.BACKEND_API_BASE}" # is empty
favicon_path = factor.FAVICON_PATH

description = """
A REST API build with FASTAPI exposing first web service.

This REST API is able to;
- bla bla
- ...
    """

app = FastAPI(
    title=appname,
    description=description,
    version=version,
    license_info={"name": "MIT License", "url": "https://opensource.org/license/mit"},
    contact={
        "name": devname,
        "url": github_url,
        "email": email,
    },
    terms_of_service="https://example.com/tos",
    openapi_url=f"{version_prefix}/openapi.json",
    docs_url=f"{version_prefix}/docs",
    redoc_url=f"{version_prefix}/redoc"
)

app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
        allow_credentials=True,
    )

@app.get("/")
async def root():
    return {"message": "Hello World"}
    
@app.get('/favicon.ico', include_in_schema=False)
async def favicon():
    return FileResponse(favicon_path)
