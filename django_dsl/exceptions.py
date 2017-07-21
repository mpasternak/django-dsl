# -*- encoding: utf-8 -*-


class CompileException(Exception):
    def __init__(self, message):
        self.message = message


class NoSuchShortcutError(KeyError):
    pass
