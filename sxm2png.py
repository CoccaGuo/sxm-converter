# sxm2png.py by CoccaGuo at 2020/12/04 13:48
import pySPM
import matplotlib.pyplot as plt

def show(sxmpath, channel='Current'):
    sxm = pySPM.SXM(sxmpath)
    sxm.get_channel(channel).show(cmap='viridis')
    plt.show()

def save(sxmpath: str, savepath: str, channel='Current'):
    if not sxmpath.endswith(".sxm"): return
    print("working with : "+sxmpath)
    sxm = pySPM.SXM(sxmpath)
    sxm.get_channel(channel).show(cmap='viridis')
    plt.savefig(savepath)

