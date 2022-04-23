from .model import Card 
from .schema import CardSchema

BASE_ROUTE = "predict"


def register_routes(api, app, root="api/v1"):
    from .controller import api as card_api

    api.add_namespace(card_api, path=f"/{root}/{BASE_ROUTE}")
