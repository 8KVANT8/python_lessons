class PointTrack:
    def __init__(self, x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError('координаты должны быть числами')
        self._x = x
        self._y = y

    def __str__(self):
        return f"PointTrack: {self._x}, {self._y}"


class Track:
    def __init__(self, *args):
        self.__points = []
        if isinstance(args[0], (int, float)) and isinstance(args[1], (int, float)):
            self.__points.append(PointTrack(args[0], args[1]))
        else:
            self.__points.extend(args)

    @property
    def points(self):
        return tuple(self.__points)

    def add_back(self, pt):  ##добавление новой точки в конец маршрута (pt - объект класса PointTrack)
        self.__points.append(pt)

    def add_front(self, pt): ## добавление новой точки в начало маршрута(pt - объект класса PointTrack)
        self.__points.insert(0, pt)

    def pop_back(self): ## удаление последней точки из маршрута
        self.__points.pop()

    def pop_front(self):  ## удаление первой точки из маршрута
        self.__points.pop(0)



