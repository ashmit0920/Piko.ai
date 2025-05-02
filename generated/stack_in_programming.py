from manim import *

class stack_in_programming(Scene):
    def construct(self):
        stack_rects = []
        stack_values = []
        num_rects = 5
        rect_width = 1
        rect_height = 0.7
        spacing = 0.1
        colors = [BLUE_D, GREEN_D, YELLOW_D, RED_D, PURPLE_D]

        for i in range(num_rects):
            rect = Rectangle(width=rect_width, height=rect_height, color=colors[i], fill_opacity=1)
            rect.move_to(DOWN * (i * (rect_height + spacing)))
            stack_rects.append(rect)
            value = Text(str(i + 1), font_size=30).move_to(rect.get_center())
            stack_values.append(value)

        stack_group = VGroup(*stack_rects, *stack_values).move_to(LEFT * 3)

        self.play(Create(stack_group))
        self.wait(0.5)

        push_label = Text("Push(6)", font_size=36).move_to(UP * 2 + RIGHT * 3)
        new_rect = Rectangle(width=rect_width, height=rect_height, color=ORANGE, fill_opacity=1)
        new_rect.move_to(DOWN * (num_rects * (rect_height + spacing))).shift(LEFT * 3)
        new_value = Text("6", font_size=30).move_to(new_rect.get_center())

        self.play(Write(push_label))
        self.play(Create(new_rect), Create(new_value))
        self.wait(0.3)
        self.play(new_rect.animate.move_to(DOWN * (num_rects * (rect_height + spacing))),
                  new_value.animate.move_to(DOWN * (num_rects * (rect_height + spacing))))

        stack_rects.append(new_rect)
        stack_values.append(new_value)

        self.wait(1)
        self.play(FadeOut(push_label))

        pop_label = Text("Pop()", font_size=36).move_to(UP * 2 + RIGHT * 3)
        self.play(Write(pop_label))

        removed_rect = stack_rects.pop()
        removed_value = stack_values.pop()

        self.play(removed_rect.animate.shift(RIGHT * 5), removed_value.animate.shift(RIGHT * 5), run_time=0.5)
        self.play(FadeOut(removed_rect), FadeOut(removed_value))

        self.wait(1)
        self.play(FadeOut(pop_label))

        stack_concept = Tex(r"Stack: LIFO (Last In, First Out)", font_size=48).move_to(UP * 2)
        self.play(Write(stack_concept))
        self.wait(2)

        stack_uses = Tex(r"Uses: Function Calls, Undo/Redo, Expression Evaluation", font_size=36).move_to(DOWN * 2 + RIGHT * 3)
        self.play(Write(stack_uses))
        self.wait(3)

        self.play(FadeOut(stack_group, stack_concept, stack_uses))
        self.wait(1)
