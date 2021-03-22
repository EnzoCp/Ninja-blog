from ninja import NinjaAPI

api = NinjaAPI()


@api.get("/hello")
def hello(request):
    return "Hello world"


@api.get('names/<str:name_1>/<str:name_2>/')
def names(request, name_1, name_2):
    return f'1 nome = {name_1};  2 nome = {name_2}'