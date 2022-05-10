from masonite.routes import Route
from masonite.authentication import Auth

ROUTES = [Route.get("/", "WelcomeController@show"),
          Route.group([
              Route.get("/profile", "ProfileController@edit").middleware('auth'),
              Route.post("/profile", "ProfileController@update").middleware('auth'),
          ],middleware=['auth']),
          Auth.routes()
]
