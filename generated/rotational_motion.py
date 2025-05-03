from manim import *

class rotational_motion(Scene):
    def construct(self):
        circle = Circle(radius=2, color=BLUE)
        dot = Dot(color=RED)
        dot.move_to(circle.point_from_proportion(0))

        self.play(Create(circle))
        self.play(Create(dot))

        number_of_rotations = 2
        time_for_complete_rotation = 3

        self.play(
            Rotate(
                dot,
                angle=number_of_rotations * 2 * PI,
                about_point=circle.get_center(),
                run_time=number_of_rotations * time_for_complete_rotation,
                rate_func=linear
            )
        )

        angular_velocity = number_of_rotations * 2 * PI / (number_of_rotations * time_for_complete_rotation)
        angular_velocity_text = MathTex(r"\omega = " + str(round(angular_velocity,2)) + " \ rad/s")
        angular_velocity_text.to_edge(UL)

        self.play(Write(angular_velocity_text))
        self.wait(2)
        self.play(FadeOut(angular_velocity_text))

        arrow = Arrow(start=circle.get_center(), end=circle.get_center() + RIGHT * 2, color=GREEN)
        arrow_label = MathTex(r"r").next_to(arrow, UP)

        self.play(Create(arrow), Create(arrow_label))

        tangential_velocity = angular_velocity * 2
        tangential_velocity_text = MathTex(r"v = r\omega = " + str(round(tangential_velocity, 2)) + " \ m/s")
        tangential_velocity_text.to_edge(UL)

        self.play(Write(tangential_velocity_text))
        self.wait(2)

        self.play(FadeOut(circle, dot, arrow, arrow_label, tangential_velocity_text))
        self.wait(1)
