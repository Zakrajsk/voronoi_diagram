from matplotlib import pyplot

def PlotPoints(point):
    """
    Plots all points
    """
    coords_x = list()
    coords_y = list()
    for one in point:
        coords_x.append(one.x)
        coords_y.append(one.y)

    pyplot.scatter(coords_x, coords_y)
    pyplot.show()

def PlotConnectedPoints(points):
    """
    Plots all points and their connections
    """
    coords_x = list()
    coords_y = list()
    for point in points:
        coords_x.append(point.x)
        coords_y.append(point.y)
        pyplot.scatter(point.x, point.y)
        for conn in point.connections:
            pyplot.plot([point.x, conn.x], [point.y, conn.y])

    pyplot.scatter(coords_x, coords_y)
    pyplot.show()


def PlotTriangles(triangles):
    """
    Plots all triangles
    """
    for one in triangles:
        coords_x = list()
        coords_y = list()
        for point in one.points:
            coords_x.append(point.x)
            coords_y.append(point.y)
        coords_x.append(one.points[0].x)
        coords_y.append(one.points[0].y)
        pyplot.plot(coords_x, coords_y)
    pyplot.show()
    