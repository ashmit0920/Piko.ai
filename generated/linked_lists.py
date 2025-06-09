from manim import *

class linked_lists(Scene):
    def construct(self):
        class Node(VGroup):
            def __init__(self, data, next_node=None, **kwargs):
                super().__init__(**kwargs)
                self.data = data
                self.next_node = next_node
                self.box = Square(side_length=1)
                self.text = Text(str(data), font_size=24)
                self.add(self.box, self.text)

            def create_arrow(self):
                if self.next_node:
                    self.arrow = Arrow(self.get_right(), self.next_node.get_left(), buff=0.1)
                    return self.arrow
                return None

        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)

        node1.next_node = node2
        node2.next_node = node3

        node1.move_to(LEFT * 3)
        node2.move_to(ORIGIN)
        node3.move_to(RIGHT * 3)

        arrow1 = node1.create_arrow()
        arrow2 = node2.create_arrow()

        linked_list_group = VGroup(node1, node2, node3, arrow1, arrow2)
        
        self.play(Create(node1), Write(node1.text))
        self.play(Create(node2), Write(node2.text))
        self.play(Create(node3), Write(node3.text))
        self.wait(0.5)

        self.play(Create(arrow1))
        self.wait(0.3)
        self.play(Create(arrow2))
        self.wait(1)
        
        title = Text("Linked List", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        explanation = Text("A sequence of nodes where each node points to the next.", font_size=24)
        explanation.next_to(title, DOWN)
        self.play(Write(explanation))
        self.wait(2)
        
        self.play(FadeOut(title, explanation))
        
        new_node = Node(4)
        new_node.move_to(RIGHT * 6)
        
        self.play(Create(new_node), Write(new_node.text))
        self.wait(0.5)
        
        arrow3 = Arrow(node3.get_right(), new_node.get_left(), buff=0.1)
        self.play(Create(arrow3))
        self.wait(1)
        
        node3.next_node = new_node
        
        insert_text = Text("Insertion at the end", font_size=36)
        insert_text.move_to(UP*2)
        self.play(Write(insert_text))
        self.wait(2)
        
        self.play(FadeOut(insert_text))
        
        node0 = Node(0)
        node0.move_to(LEFT * 6)
        
        self.play(Create(node0), Write(node0.text))
        self.wait(0.5)
        
        arrow0 = Arrow(node0.get_right(), node1.get_left(), buff=0.1)
        self.play(Create(arrow0))
        self.wait(1)
        
        temp_node = node1
        self.play(temp_node.animate.move_to(LEFT * 3))
        arrow_temp = node2
        self.play(arrow_temp.animate.move_to(ORIGIN))
        self.play(Create(arrow1))
        node1 = node0
        self.wait(1)

        remove_text = Text("Insertion at the beginning", font_size=36)
        remove_text.move_to(UP*2)
        self.play(Write(remove_text))
        self.wait(2)
        
        self.play(FadeOut(remove_text))

        self.wait(2)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait(1)
