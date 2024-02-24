from IObject import IObject


class Point:
    def __init__(self, pointPosition: IObject.VectorIn3D):
        self.pointPosition: IObject.VectorIn3D = pointPosition
