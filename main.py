import logic
import datetime

exportfilename = 'export ' + datetime.datetime.now().strftime("%d-%m-%Y %H-%M-%S") + '.xlsx'  # Сгенерить имя файла
firsttable = None
secondtable = None


if __name__ == '__main__':
    logic.cleanobsoletefiles()
    logic.makemagic()
