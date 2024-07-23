from drf_yasg import openapi


def openapi_info():
    return openapi.Info(
        title="Rectangle Detector API",
        default_version='v1',
        description='API for detection "points of interest" (corners of rectangles) in an image',
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="vanleo528@yandex.ru"),
        license=openapi.License(name="BSD License"),
    )


openapi_info_instance = openapi_info()
