import logic
import datetime

exportfilename = 'export ' + datetime.datetime.now().strftime("%d-%m-%Y %H-%M-%S") + '.xlsx'  # Сгенерить имя файла


if __name__ == '__main__':
    logic.cleanobsoletefiles()
    logic.makemagic(filename=exportfilename)
