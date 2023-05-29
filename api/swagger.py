from flask_swagger_ui import get_swaggerui_blueprint

SWAGGER_URL = "/apidocs"  # URL for exposing Swagger UI (can be customized)
API_URL = "/api/static/swagger.json"  # URL for your Swagger JSON file (generated dynamically or manually)

# Call factory function to create a Swagger UI blueprint
swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        "app_name": "API Documentation"  # Customize your Swagger UI page title
    }
)
