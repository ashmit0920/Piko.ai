from manim import *

class stack_in_programming(Scene):
    def construct(self):
        stack_rects = []
        stack_values = []
        num_rects = 5

        for i in range(num_rects):
            rect = Rectangle(width=2, height=1, color=WHITE)
            rect.move_to(DOWN * i)
            stack_rects.append(rect)

            value = Text(str(i+1), font_size=36)
            stack_values.append(value)

        stack_group = VGroup(*stack_rects)
        self.play(Create(stack_group))

        text_push = Text("Pushing elements onto the stack", font_size=24)
        text_push.to_edge(UP)
        self.play(Write(text_push))

        for i in range(num_rects):
            self.play(Write(stack_values[i]))
            stack_values[i].move_to(stack_rects[i].get_center())
            self.wait(0.5)

        self.wait(1)
        self.play(FadeOut(text_push))

        text_pop = Text("Popping elements from the stack", font_size=24)
        text_pop.to_edge(UP)
        self.play(Write(text_pop))

        for i in reversed(range(num_rects)):
            self.play(FadeOut(stack_values[i]))
            self.wait(0.5)
        
        self.wait(1)
        self.play(FadeOut(text_pop))

        text_operations = Text("Stack Operations", font_size=36)
        text_operations.move_to(UP)
        self.play(Write(text_operations))

        push_operation = Text("1. Push: Add an element to the top", font_size=24)
        pop_operation = Text("2. Pop: Remove the top element", font_size=24)
        peek_operation = Text("3. Peek: View the top element", font_size=24)
        is_empty_operation = Text("4. IsEmpty: Check if the stack is empty", font_size=24)

        push_operation.move_to(DOWN * 1)
        pop_operation.move_to(DOWN * 2)
        peek_operation.move_to(DOWN * 3)
        is_empty_operation.move_to(DOWN * 4)

        self.play(Write(push_operation),Write(pop_operation),Write(peek_operation),Write(is_empty_operation))
        self.wait(2)

        self.play(FadeOut(text_operations),FadeOut(push_operation),FadeOut(pop_operation),FadeOut(peek_operation),FadeOut(is_empty_operation), FadeOut(stack_group))

        stack_rects = []
        stack_values = []
        num_rects = 3

        for i in range(num_rects):
            rect = Rectangle(width=2, height=1, color=WHITE)
            rect.move_to(DOWN * i)
            stack_rects.append(rect)

            value = Text(str(i+1), font_size=36)
            stack_values.append(value)

        stack_group = VGroup(*stack_rects)
        self.play(Create(stack_group))

        for i in range(num_rects):
            self.play(Write(stack_values[i]))
            stack_values[i].move_to(stack_rects[i].get_center())
            self.wait(0.5)
            
        text_peek = Text("Peeking the top element", font_size=24)
        text_peek.to_edge(UP)
        self.play(Write(text_peek))

        top_element = stack_values[num_rects - 1].copy()
        top_element.set_color(YELLOW)

        self.play(Transform(stack_values[num_rects - 1], top_element))
        self.wait(1)

        self.play(FadeOut(text_peek))

        text_is_empty = Text("Checking if the stack is empty (False)", font_size=24)
        text_is_empty.to_edge(UP)
        self.play(Write(text_is_empty))
        self.wait(2)

        self.play(FadeOut(text_is_empty))

        for i in reversed(range(num_rects)):
            self.play(FadeOut(stack_values[i]))
            self.wait(0.5)

        text_is_empty_true = Text("Checking if the stack is empty (True)", font_size=24)
        text_is_empty_true.to_edge(UP)
        self.play(Write(text_is_empty_true))
        
        self.wait(2)
        self.play(FadeOut(stack_group), FadeOut(text_is_empty_true))
        
        text_applications = Text("Applications of Stacks", font_size=36)
        text_applications.move_to(UP)
        self.play(Write(text_applications))

        app1 = Text("1. Expression Evaluation", font_size=24)
        app2 = Text("2. Function Calls", font_size=24)
        app3 = Text("3. Undo/Redo Operations", font_size=24)
        app4 = Text("4. Backtracking", font_size=24)

        app1.move_to(DOWN * 1)
        app2.move_to(DOWN * 2)
        app3.move_to(DOWN * 3)
        app4.move_to(DOWN * 4)

        self.play(Write(app1),Write(app2),Write(app3),Write(app4))
        self.wait(3)
        self.play(FadeOut(text_applications),FadeOut(app1),FadeOut(app2),FadeOut(app3),FadeOut(app4))
        
        end_text = Text("The End", font_size=48)
        self.play(Write(end_text))
        self.wait(2)
        self.play(FadeOut(end_text))
        self.wait(1)
