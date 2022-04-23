def register_routes(api, app, root="api"):
    from app.strategy import register_routes as attach_strategy

    # Add routes
    attach_strategy(api, app)
