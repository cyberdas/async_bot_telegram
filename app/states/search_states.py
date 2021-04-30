from aiogram.dispatcher.filters.state import StatesGroup, State


class HeadSearch(StatesGroup):
    waiting_for_vacancy = State()
    waiting_for_region = State()
    waiting_for_job_type = State()
