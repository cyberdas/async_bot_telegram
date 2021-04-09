from aiogram.dispatcher.filters.state import StatesGroup, State



class HeadSearch(StatesGroup):
    waiting_for_vacancy = State()
