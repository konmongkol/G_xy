import numpy as np
import matplotlib.pyplot as plt
class G_xy:
    # r_x = 0
    # r_y = 0
    # lr_x = []
    # lr_y = []
    # v = 0
    # def __init__(self):
    #     self.V
    
    def xt(self):
        fig = plt.figure()
        ax = plt.axes(xlim=(0,10),ylim = (0,10))
        V_initial = 5.7
        theta = (np.pi)/4
        g = 9.8
        v_x = V_initial * np.cos(theta)
        v_y = V_initial * np.sin(theta)
        time = np.linspace(0,100,10000)
        r_x = 0
        r_y = 0
        lr_x = []
        lr_y = []
        for t in time:
            r_x = v_x * t
            r_y = (v_y * t) - 1/2 * g * (t ** 2) + 0.6
            if r_y >= 0:
                lr_x.append(t)
                lr_y.append(r_x)
            else:
                break
            plt.plot(lr_x, lr_y, color='b')
            plt.pause(0.01)
        plt.show()
    
    def yt(self):
        fig = plt.figure()
        ax = plt.axes(xlim=(0,10),ylim = (0,10))
        V_initial = 5.7
        theta = (np.pi)/4
        g = 9.8
        v_x = V_initial * np.cos(theta)
        v_y = V_initial * np.sin(theta)
        time = np.linspace(0,100,10000)
        r_x = 0
        r_y = 0
        lr_x = []
        lr_y = []
        for t in time:
            r_x = v_x * t
            r_y = (v_y * t) - 1/2 * g * (t ** 2) + 0.6
            if r_y >= 0:
                lr_x.append(t)
                lr_y.append(r_y)
            else:
                break
            plt.plot(lr_x, lr_y, color='b')
            plt.pause(0.01)
        plt.show()
    
    def vxt(self):
        fig = plt.figure()
        ax = plt.axes(xlim=(0, 2), ylim=(0, 10))
        V_initial = 5.7
        theta = (np.pi) / 4
        g = 9.8
        v_x = V_initial * np.cos(theta)
        v_y = V_initial * np.sin(theta)
        time = np.linspace(0, 100, 10000)
        r_x = 0
        r_y = 0
        lr_x = []
        lr_y = []
        for t in time:
            r_x = v_x * t
            r_y = (v_y * t) - 1 / 2 * g * (t ** 2) + 0.6
            if r_y >= 0:
                lr_x.append(t)
                lr_y.append(v_x)
            else:
                break
            plt.plot(lr_x, lr_y, color='b')
            plt.pause(0.01)
        plt.show()
    
    def vyt(self):
        fig = plt.figure()
        ax = plt.axes(xlim=(0, 2), ylim=(-10, 10))
        V_initial = 5.7
        theta = (np.pi) / 4
        g = 9.8
        v_x = V_initial * np.cos(theta)
        v_y = V_initial * np.sin(theta)
        time = np.linspace(0, 100, 10000)
        r_x = 0
        r_y = 0
        lr_x = []
        lr_y = []
        for t in time:
            r_y = (v_y * t) - 1 / 2 * g * (t ** 2) + 0.6
            abv = v_y - g * t
            if r_y >= 0:
                lr_x.append(t)
                lr_y.append(abv)
            else:
                break
            plt.plot(lr_x, lr_y, color='b')
            plt.pause(0.1)
        plt.show()
        
    def __str__():
        return 'konmongkol'

if __name__ == '__main__':
    m = G_xy()
    m.vyt()
    