from masonite.controllers import Controller
from masonite.views import View
from masonite.request import Request
from masonite.authentication import Auth
from masonite.facades import Dump


class ProfileController(Controller):
    def edit(self, view: View):
        return view.render("auth/profile")

    def update(self, request: Request, auth: Auth, view: View):
        # Dump.dd(request.all())
        auth.user().update_profile(request.all())
        return view.render("auth/home")
