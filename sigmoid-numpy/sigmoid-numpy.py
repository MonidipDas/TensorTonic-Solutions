
import numpy as np

def sigmoid(x: list | float) -> np.ndarray | float:
    x = np.asarray(x)
    ans = 1 / (1 + np.exp(-x))
    return float(ans) if ans.ndim == 0 else ans
