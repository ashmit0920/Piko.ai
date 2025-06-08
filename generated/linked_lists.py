from manim import *

class linked_lists(Scene):
    def construct(self):
        class Node(VGroup):
            def __init__(self, data, next_node=None, **kwargs):
                super().__init__(**kwargs)
                self.data = data
                self.square = Square(side_length=1)
                self.text = Text(str(data))
                self.add(self.square, self.text)
                self.next_node = next_node

            def create_arrow(self, next_node):
                self.arrow = Arrow(self.square.get_right(), next_node.square.get_left(), buff=0.1)
                return self.arrow

        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(4)

        node1.next_node = node2
        node2.next_node = node3
        node3.next_node = node4

        node1.move_to(LEFT * 3)
        node2.next_node = node3
        node2.move_to(LEFT)
        node3.next_node = node4
        node3.move_to(RIGHT)
        node4.move_to(RIGHT * 3)

        arrow1 = node1.create_arrow(node2)
        arrow2 = node2.create_arrow(node3)
        arrow3 = node3.create_arrow(node4)
        self.play(Create(node1), Create(node2), Create(node3), Create(node4))
        self.play(Create(arrow1), Create(arrow2), Create(arrow3))
        self.wait(2)

        new_node = Node(5)
        new_node.move_to(UP * 2)

        self.play(Create(new_node))
        self.wait(1)
        arrow4 = Arrow(node2.square.get_right(), new_node.square.get_left(), buff=0.1)
        self.play(Transform(arrow2, arrow4))

        new_arrow = Arrow(new_node.square.get_right(), node3.square.get_left(), buff=0.1)
        self.play(Create(new_arrow))
        self.wait(2)
        self.play(FadeOut(arrow1, arrow2, arrow3, new_arrow, node1, node2, node3, node4, new_node))
        self.wait(1)
