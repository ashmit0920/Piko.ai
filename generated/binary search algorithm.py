from manim import *

class BinarySearchAlgorithm(Scene):
    def construct(self):
        arr = [2, 5, 7, 8, 11, 12]
        target = 11
        n = len(arr)

        title = Text("Binary Search Algorithm", font_size=48)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))

        array_text = Text(f"Array: {arr}", font_size=36)
        target_text = Text(f"Target: {target}", font_size=36).shift(DOWN)
        self.play(Write(array_text), Write(target_text))
        self.wait(1)

        boxes = VGroup(*[Square(side_length=0.7) for _ in range(n)])
        boxes.arrange(RIGHT, buff=0.1)
        boxes.shift(DOWN * 1.5)

        numbers = VGroup(*[Text(str(num), font_size=36) for num in arr])
        for i in range(n):
            numbers[i].move_to(boxes[i].get_center())

        self.play(Create(boxes), Write(numbers))
        self.wait(1)

        low = 0
        high = n - 1

        low_pointer = Triangle(color=GREEN, fill_opacity=1).scale(0.2).rotate(PI).move_to(boxes[low].get_center() + UP * 0.8)
        low_text = Text("Low", color=GREEN, font_size=24).next_to(low_pointer, UP)

        high_pointer = Triangle(color=RED, fill_opacity=1).scale(0.2).rotate(PI).move_to(boxes[high].get_center() + UP * 0.8)
        high_text = Text("High", color=RED, font_size=24).next_to(high_pointer, UP)

        self.play(Create(low_pointer), Write(low_text), Create(high_pointer), Write(high_text))
        self.wait(1)

        while low <= high:
            mid = (low + high) // 2
            mid_pointer = Triangle(color=BLUE, fill_opacity=1).scale(0.2).rotate(PI).move_to(boxes[mid].get_center() + UP * 0.8)
            mid_text = Text("Mid", color=BLUE, font_size=24).next_to(mid_pointer, UP)

            self.play(Create(mid_pointer), Write(mid_text))
            self.wait(0.5)

            if arr[mid] == target:
                found_text = Text(f"Found {target} at index {mid}", color=YELLOW, font_size=36).shift(UP * 2)
                self.play(Write(found_text))
                self.play(boxes[mid].animate.set_fill(YELLOW, opacity=0.5))
                self.wait(2)
                self.play(FadeOut(array_text, target_text, boxes, numbers, low_pointer, low_text, high_pointer, high_text, mid_pointer, mid_text, found_text))
                return

            elif arr[mid] < target:
                self.play(
                    Transform(low_pointer, Triangle(color=GREEN, fill_opacity=1).scale(0.2).rotate(PI).move_to(boxes[mid + 1].get_center() + UP * 0.8)),
                    Transform(low_text, Text("Low", color=GREEN, font_size=24).next_to(Triangle(color=GREEN, fill_opacity=1).scale(0.2).rotate(PI).move_to(boxes[mid + 1].get_center() + UP * 0.8), UP)),
                )
                low = mid + 1
            else:
                self.play(
                    Transform(high_pointer, Triangle(color=RED, fill_opacity=1).scale(0.2).rotate(PI).move_to(boxes[mid - 1].get_center() + UP * 0.8)),
                    Transform(high_text, Text("High", color=RED, font_size=24).next_to(Triangle(color=RED, fill_opacity=1).scale(0.2).rotate(PI).move_to(boxes[mid - 1].get_center() + UP * 0.8), UP))
                )
                high = mid - 1

            self.wait(1)
            self.play(FadeOut(mid_pointer, mid_text))

        not_found_text = Text(f"{target} not found in array", color=RED, font_size=36).shift(UP * 2)
        self.play(Write(not_found_text))
        self.wait(2)

        self.play(FadeOut(array_text, target_text, boxes, numbers, low_pointer, low_text, high_pointer, high_text, not_found_text))
        self.wait(1)
