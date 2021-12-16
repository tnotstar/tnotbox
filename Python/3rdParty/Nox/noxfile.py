# -*- coding: utf-8 -*-

import nox


@nox.session
def black(session):
    session.install("black")
    session.run("black", ".")


@nox.session
def lint(session):
    session.install("flake8")
    session.run("flake8", "example.py")


@nox.session
def run(session):
    session.install(".")
    session.run("python", "example.py")


# EOF
