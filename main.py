from manim import *


class ArrayExplanation(Scene):
    def construct(self):
        # Title
        title = Text("What is an Array?", font_size=48).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Introduction text
        intro_text = Text(
            "An array is a collection of items stored at contiguous memory locations.",
            font_size=28
        ).next_to(title, DOWN)
        self.play(Write(intro_text))
        self.wait(2)

        # Create the array representation
        array_size = 5
        cell_width = 1.5
        cell_height = 1
        array_cells = VGroup(*[
            Square(side_length=cell_width, stroke_color=WHITE,
                   fill_opacity=0.2, fill_color=BLUE)
            for _ in range(array_size)
        ]).arrange(RIGHT, buff=0)  # Arrange cells horizontally with no buffer

        # Add indices below the array
        indices = VGroup(*[
            Text(str(i), font_size=24).next_to(array_cells[i], DOWN, buff=0.1)
            for i in range(array_size)
        ])

        # Group the array and indices
        array_group = VGroup(
            array_cells, indices).center().to_edge(DOWN, buff=1)

        self.play(FadeIn(array_group))
        self.wait(1)

        # Explain storage
        storage_text = Text(
            "Items are stored in sequence.",
            font_size=28
        ).next_to(intro_text, DOWN, buff=0.5)
        self.play(Write(storage_text))
        self.wait(1)

        # Add elements to the array
        elements = ["A", "B", "C", "D", "E"]
        element_mobjects = VGroup()

        for i in range(array_size):
            element_text = Text(elements[i], font_size=36, color=YELLOW)
            element_text.move_to(array_cells[i].get_center())
            element_mobjects.add(element_text)
            self.play(FadeIn(element_text, shift=UP))
            self.wait(0.5)

        self.wait(1)

        # Explain indexing
        indexing_text = Text(
            "Each item can be accessed using an index.",
            font_size=28
        ).next_to(storage_text, DOWN, buff=0.5)
        self.play(Write(indexing_text))
        self.wait(1)

        # Highlight an element using its index
        highlight_index = 2  # Highlight the element at index 2 (which is "C")
        highlight_box = SurroundingRectangle(
            array_cells[highlight_index], color=RED, stroke_width=4)
        index_arrow = Arrow(indices[highlight_index].get_bottom(
        ), array_cells[highlight_index].get_bottom(), color=RED)
        access_text = Text(f"Accessing element at index {highlight_index}", font_size=28, color=RED).next_to(
            array_group, UP, buff=0.5)

        self.play(
            Create(highlight_box),
            GrowArrow(index_arrow),
            Write(access_text)
        )
        self.wait(2)

        # Clean up and end
        self.play(
            FadeOut(title),
            FadeOut(intro_text),
            FadeOut(storage_text),
            FadeOut(indexing_text),
            FadeOut(array_group),
            FadeOut(element_mobjects),
            FadeOut(highlight_box),
            FadeOut(index_arrow),
            FadeOut(access_text)
        )
        self.wait(1)
