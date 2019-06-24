from abc import abstractmethod, ABC


class TouchScreenLaptop(ABC):

    @abstractmethod
    def scroll(self):
        pass

    @abstractmethod
    def click(self):
        pass


class HP(TouchScreenLaptop):

    def scroll(self):
        print("Scrolling HP")


class DELL(TouchScreenLaptop):

    def scroll(self):
        print("Scrolling HP")


class HPNoteBook(HP):
    def click(self):
        print("HP notebook click")


class DELLNoteBook(DELL):
    def click(self):
        print("DELL notebook click")


hp = HPNoteBook()
hp.click()
hp.scroll()

dell = DELLNoteBook()
dell.scroll()
dell.click()