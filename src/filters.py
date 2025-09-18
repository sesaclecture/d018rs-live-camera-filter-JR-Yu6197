import cv2
import numpy as np


class Filters:
    # TODO: Image kernels
    Kernels = {
        "original" : np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]], dtype=np.float32),
        "blur" : np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]], dtype=np.float32) / 9,
        "gaussian blur" : np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]], dtype=np.float32) / 16,
        "sharpen" : np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], dtype=np.float32),
        "sobel (x)" : np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], dtype=np.float32),
        "sobel (y)" : np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]], dtype=np.float32),
        "edge detection": np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]], dtype=np.float32),          
        "emboss": np.array([[-2, -1, 0], [-1, 1, 1], [0, 1, 2]], dtype=np.float32)
    }

    def __init__(self, kernels=Kernels):
        self.kernels = kernels
        # TODO: Implement internal variables
        self.kernels = kernels
        self._kernel_names = list(self.kernels.keys())
        self._current_kernel_index = 0

    def apply_filter(self, frame, filter_name) -> np.array:
        # TODO: Apply the selected filter kernel to the frame
        kernel = self.kernels.get(filter_name)
        if kernel is not None:
            return cv2.filter2D(frame, -1, kernel)
        return frame

        
    
    def get_current_filter_name(self) -> str:
        # TODO: Return currently set kernels's name
        return self._kernel_names[self._current_kernel_index]
        

    def switch_next_filter(self):
        # TODO: Update currently selected kernel to the next
        self._current_kernel_index = (self._current_kernel_index + 1) % len(self._kernel_names)

    def switch_previous_filter(self):
        # TODO: Update currently selected kernel to the previous
        self._current_kernel_index = (self._current_kernel_index - 1 + len(self._kernel_names)) % len(self._kernel_names)
