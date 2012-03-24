# -*- coding: utf-8 -*-
"""URL definitions."""
from webapp2 import Route
from webapp2_extras.routes import HandlerPrefixRoute

rules = [

    HandlerPrefixRoute('project.handlers.', [

        ## === Main URLs === ##
        Route('/', name='landing', handler='main.Landing'),
        Route('/make-a-donation', name='donation', handler='main.Donate'),

        ## === Security URLs === ##
        HandlerPrefixRoute('main.', [

            Route('/login', name='auth/login', handler='Login'),
            Route('/logout', name='auth/logout', handler='Logout'),
            Route('/register', name='auth/register', handler='Register'),

        ])

    ])
]
