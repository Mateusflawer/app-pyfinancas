import datetime
import locale
from data import controller, saver, loader


locale.setlocale(locale.LC_ALL, "portuguese_brazil")


def format_data_br(data):
    if isinstance(data, str):
        formato = "%Y-%m-%d"
        formato_br = "%d/%m/%Y"
        data_datetime = datetime.datetime.strptime(data, formato)
        data_str = data_datetime.strftime(formato_br)
        return data_str
