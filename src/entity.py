import enum

from aiogram.filters.callback_data import CallbackData


class Role(enum.StrEnum):
    ref = enum.auto()
    candidate = enum.auto()
    admin = enum.auto()
