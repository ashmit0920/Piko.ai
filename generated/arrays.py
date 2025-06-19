from manim import *

class Arrays(Scene):
    def construct(self):
        array_data = [5, 2, 8, 1, 9, 4, 7, 3, 6]
        num_elements = len(array_data)
        cell_size = 1.0
        array_start = LEFT * (num_elements * cell_size / 2)

        array_rects = []
        array_texts = []

        for i in range(num_elements):
            rect = Rectangle(width=cell_size, height=cell_size)
            rect.move_to(array_start + RIGHT * (i * cell_size))
            array_rects.append(rect)

            text = Text(str(array_data[i]))
            text.scale(0.7)
            text.move_to(rect.get_center())
            array_texts.append(text)

        array_group = VGroup(*array_rects, *array_texts)
        self.play(Create(array_group))

        self.wait(1)

        index_labels = []
        for i in range(num_elements):
            index_label = Text(str(i), font_size=24)
            index_label.next_to(array_rects[i], DOWN)
            index_labels.append(index_label)

        index_group = VGroup(*index_labels)
        self.play(Create(index_group))
        self.wait(1)

        highlight_rect = Rectangle(width=cell_size, height=cell_size, color=YELLOW, stroke_width=3)

        def highlight_element(index):
            highlight_rect.move_to(array_rects[index].get_center())
            return FadeIn(highlight_rect)

        def unhighlight_element(index):
            highlight_rect.move_to(array_rects[index].get_center())
            return FadeOut(highlight_rect)

        access_text = Text("Accessing element at index 3", font_size=36)
        access_text.to_edge(UP)
        self.play(Write(access_text))
        self.wait(0.5)

        self.play(highlight_element(3))
        self.wait(1)

        value_text = Text("Value: " + str(array_data[3]), font_size=36)
        value_text.next_to(access_text, DOWN)
        self.play(Write(value_text))
        self.wait(1)

        self.play(FadeOut(access_text), FadeOut(value_text), unhighlight_element(3))
        self.wait(0.5)

        update_text = Text("Updating element at index 1 to 10", font_size=36)
        update_text.to_edge(UP)
        self.play(Write(update_text))
        self.wait(0.5)

        self.play(highlight_element(1))
        self.wait(0.5)

        new_value = 10
        new_text = Text(str(new_value))
        new_text.scale(0.7)
        new_text.move_to(array_rects[1].get_center())

        self.play(Transform(array_texts[1], new_text))
        array_data[1] = new_value
        self.wait(1)
        self.play(FadeOut(update_text), unhighlight_element(1))

        insert_text = Text("Inserting element 12 at index 2", font_size=36)
        insert_text.to_edge(UP)
        self.play(Write(insert_text))
        self.wait(1)

        self.play(FadeOut(array_group), FadeOut(index_group))

        new_array_data = array_data[:2] + [12] + array_data[2:]
        num_elements = len(new_array_data)
        array_start = LEFT * (num_elements * cell_size / 2)

        array_rects = []
        array_texts = []

        for i in range(num_elements):
            rect = Rectangle(width=cell_size, height=cell_size)
            rect.move_to(array_start + RIGHT * (i * cell_size))
            array_rects.append(rect)

            text = Text(str(new_array_data[i]))
            text.scale(0.7)
            text.move_to(rect.get_center())
            array_texts.append(text)

        array_group = VGroup(*array_rects, *array_texts)
        self.play(Create(array_group))

        index_labels = []
        for i in range(num_elements):
            index_label = Text(str(i), font_size=24)
            index_label.next_to(array_rects[i], DOWN)
            index_labels.append(index_label)

        index_group = VGroup(*index_labels)
        self.play(Create(index_group))

        self.wait(2)
        self.play(FadeOut(insert_text), FadeOut(array_group), FadeOut(index_group))
        self.wait(1)
