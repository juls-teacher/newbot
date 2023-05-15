from aiohttp import web
from aiohttp_apispec import docs, request_schema, setup_aiohttp_apispec

from schema import MessageSchema


routes = web.RouteTableDef()

@docs(
   tags=["telegram"],
   summary="Send message API",
   description="This end-point sends message to telegram bot user/users",
)
@request_schema(MessageSchema())
@routes.post("/")
async def index_get(request: web.Request) -> web.Response:
    return web.json_response({"status": "OK"})


if __name__ == "__main__":
    app = web.Application()
    setup_aiohttp_apispec(
        app=app, title="Hectar Bot documentation", version="v1.0",
        url="/api/docs/swagger.json", swagger_path="/api/docs",
    )
    app.add_routes(routes)
    web.run_app(app, port=5000)
