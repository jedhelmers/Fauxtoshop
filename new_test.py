import cv2
import numpy as np
from typing import List, Optional


class Layer:
    def __init__(self, show: bool = True, name: str = "Layer", width: int = 0, height: int = 0, channels: int = 4) -> None:
        self.show: bool = show
        self.name: str = name
        self.width: int = width
        self.height: int = height
        self.channels: int = channels
        self.image: np.ndarray = np.zeros((height, width, channels), dtype=np.uint8)
        self.mask: np.ndarray = np.ones((height, width), dtype=np.float32)  # Default mask is a matrix of ones with the same dimensions as the image
        self.mode: str = 'Normal'
        self.locked: bool = False

    def draw_random_circle(self) -> None:
        center_x = np.random.randint(0, self.width)
        center_y = np.random.randint(0, self.height)
        radius = np.random.randint(10, min(self.width, self.height) // 2)
        color = np.random.randint(0, 256, self.channels).tolist()

        cv2.circle(self.image, (center_x, center_y), radius, color, -1)

    def resize_image(self, new_width: int, new_height: int) -> None:
        self.image = cv2.resize(self.image, (new_width, new_height))

    def move_image(self, x: int, y: int) -> None:
        if self.locked:
            return

        M = np.float32([[1, 0, x], [0, 1, y]])
        self.image = cv2.warpAffine(self.image, M, (self.width, self.height))

    def rotate_image(self, angle: float) -> None:
        center = (self.width // 2, self.height // 2)
        M = cv2.getRotationMatrix2D(center, angle, 1.0)
        self.image = cv2.warpAffine(self.image, M, (self.width, self.height))

    def apply_mask(self) -> None:
        self.image = cv2.multiply(self.image, self.mask)


class Artboard:
    def __init__(self) -> None:
        self.width: int = 800
        self.height: int = 800
        self.layers: List[Layer] = []
        self.current_layer_index: int = 0
        self.initialize()

    def initialize(self) -> None:
        self.create_checkerboard()
        for _ in range(9):
            layer = Layer(show=True, width=self.width, height=self.height)
            layer.draw_random_circle()
            self.layers.append(layer)

    def create_checkerboard(self) -> None:
        checkerboard_size = 80
        rows = self.height // checkerboard_size
        cols = self.width // checkerboard_size
        checkerboard = np.zeros((rows * checkerboard_size, cols * checkerboard_size, 4), dtype=np.uint8)
        for r in range(rows):
            for c in range(cols):
                if (r + c) % 2 == 0:
                    checkerboard[r * checkerboard_size: (r + 1) * checkerboard_size,
                                 c * checkerboard_size: (c + 1) * checkerboard_size] = [192, 192, 192, 25]
        checkerboard_layer = Layer(show=True, name="Checkerboard", width=self.width, height=self.height)
        checkerboard_layer.image = checkerboard
        checkerboard_layer.locked = True
        self.layers.insert(0, checkerboard_layer)

    def compile_layers(self) -> Optional[np.ndarray]:
        layers_to_render = [layer for layer in self.layers if layer.show]
        if len(layers_to_render) == 0:
            return None

        compiled_image = np.zeros((self.height, self.width, 3), dtype=np.uint8)

        for layer in layers_to_render:
            layer_image = layer.image[:, :, :3]
            compiled_image = cv2.add(compiled_image, layer_image)

        return compiled_image


# Displaying the compiled layers
if __name__ == "__main__":
    artboard = Artboard()

    while True:
        compiled_layers = artboard.compile_layers()
        if compiled_layers is not None:
            cv2.imshow("Artboard", compiled_layers)

        key = cv2.waitKey(0)
        if key == 27:  # ESC key to exit
            break
        elif ord('0') <= key <= ord('9'):
            index = key - ord('0')
            if index < len(artboard.layers):
                artboard.current_layer_index = index
        elif key == 13:  # Enter key
            if artboard.current_layer_index < len(artboard.layers):
                layer = artboard.layers[artboard.current_layer_index]
                layer.show = not layer.show
        elif key == 0:  # Up arrow key
            layer = artboard.layers[artboard.current_layer_index]
            layer.move_image(0, -10)
            compiled_layers = artboard.compile_layers()  # Recompile after moving
        elif key == 1:  # Down arrow key
            layer = artboard.layers[artboard.current_layer_index]
            layer.move_image(0, 10)
            compiled_layers = artboard.compile_layers()  # Recompile after moving
        elif key == 2:  # Left arrow key
            layer = artboard.layers[artboard.current_layer_index]
            layer.move_image(-10, 0)
            compiled_layers = artboard.compile_layers()  # Recompile after moving
        elif key == 3:  # Right arrow key
            layer = artboard.layers[artboard.current_layer_index]
            layer.move_image(10, 0)
            compiled_layers = artboard.compile_layers()  # Recompile after moving
        elif key == ord('l'):  # L key
            layer = artboard.layers[artboard.current_layer_index]
            layer.locked = not layer.locked
            print(f"Layer {artboard.current_layer_index} is locked: {layer.locked}")
        elif key == ord('r'):  # R key
            layer = artboard.layers[artboard.current_layer_index]
            layer.rotate_image(45)
            compiled_layers = artboard.compile_layers()  # Recompile after rotating

    cv2.destroyAllWindows()
