import json


class HandlingFileMeta(type):
    """
    Realized work with file
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):

        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class HandlingFile(metaclass=HandlingFileMeta):

    def __init__(self):
        self.dict_requisites = {}

    def write(self):
        with open('./text.txt', 'w', encoding='utf-8') as File:
            json.dump(self.dict_requisites, File)

    def read(self):
        with open('./text.txt', 'r', encoding='utf-8') as File:
            s = File.read()

        try:
            dict_req = json.loads(s)
            self.dict_requisites = dict_req
        except KeyError:
            self.dict_requisites = {}


if __name__ == "__main__":
    test = HandlingFile()
    test2 = HandlingFile()

    test.dict_requisites["232"] = 213
    test.dict_requisites["ad"] = 231

    print(test.dict_requisites)
    print(test2.dict_requisites)

