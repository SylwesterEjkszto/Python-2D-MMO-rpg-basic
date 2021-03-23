class Camera:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def slide_to(self, destination, dt, speed_factor=0.5, anchor_point=None):
        """slide a 2D camera to a certain destination smoothly."""
        if anchor_point is None:
            anchor_point = (0, 0)
        else:
            anchor_point = tuple(anchor_point)

        fac = clamp(speed_factor * dt)

        self.x += (destination[0] - self.x - anchor_point[0]) * fac
        self.y += (destination[1] - self.y - anchor_point[1]) * fac


cam = Camera(0, 0)