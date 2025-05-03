from manim import *

class rotational_motion(Scene):
    def construct(self):
        circle = Circle(radius=2, color=BLUE)
        self.play(Create(circle))
        
        dot = Dot(circle.point_from_proportion(0), color=RED)
        self.play(Create(dot))
        
        line = Line(circle.get_center(), dot.get_center(), color=GREEN)
        self.play(Create(line))
        
        def update_dot(mob, alpha):
            mob.move_to(circle.point_from_proportion(alpha % 1))
            return mob
        
        def update_line(mob):
            mob.become(Line(circle.get_center(), dot.get_center(), color=GREEN))
            return mob
        
        self.play(
            UpdateFromAlphaFunc(dot, update_dot),
            UpdateFromFunc(line, update_line),
            rate_func=linear,
            run_time=5,
        )
        
        angular_velocity = ValueTracker(0)
        angular_velocity_text = Text("Angular Velocity: 0 rad/s").to_edge(UP)
        self.add(angular_velocity_text)
        
        def update_angular_velocity_text(mob):
            mob.become(Text("Angular Velocity: " + str(round(angular_velocity.get_value(), 2)) + " rad/s").to_edge(UP))
            return mob
        
        self.play(angular_velocity.animate.set_value(1), UpdateFromFunc(angular_velocity_text, update_angular_velocity_text), run_time=3)
        
        self.wait(2)
        
        self.play(FadeOut(circle, dot, line, angular_velocity_text))
