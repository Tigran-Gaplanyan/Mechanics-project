from Spring import Spring

class Body:
    def __init__(self, m: float, spring: Spring):
        self.m = m
        self.spring = spring

    def move(self, t: float, dt: float, x0: float, vo: float) -> List[float]:
        x = x0
        v = vo
        xs = [x0]
        for i in range(int(t / dt)):
            f = -self.spring.get_force(x)
            a = f / self.m
            v += a * dt
            x += v * dt
            xs.append(x)
        return xs