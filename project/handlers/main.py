from project.handlers import WebHandler


class Landing(WebHandler):

    ''' Returns the age-old, enigmatic success response. '''

    def get(self):
        self.render('main/landing.html')


class Donate(WebHandler):

    ''' Donate page for Meals on Wheels '''

    def get(self):
        self.render('main/donate.html')


class Login(WebHandler):

    ''' Redirect the user to a login page that will continue to the site root. '''

    def get(self):

        ''' Generate a login URL and return a redirect. '''

        return self.redirect(self.api.users.create_login_url('/'))
