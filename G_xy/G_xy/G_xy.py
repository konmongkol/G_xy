import numpy as np
class G_xy:
    r_x = 0
    r_y = 0
    lr_x = []
    lr_y = []
    v = 0
    # def __init__(self):
        # self.V = V
    def r_x(self,t):
        theta = (np.pi)/4
        v_x = self.V * np.cos(theta)
        return v_x * t
    def r_y(self,t):
        g = 9.8
        theta = (np.pi)/4
        v_y = self.V * np.cos(theta)
        return (v_y * t) - 1/2 * g * (t ** 2)
    def __str__():
        return 'konmongkol'

if __name__ == '__main__':
    print(1)
        