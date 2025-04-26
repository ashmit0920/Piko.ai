from manim import *


class strings_in_programming(Scene):
    def construct(self):
        title = Text("Strings in Programming", font_size=48)
        self.play(Write(title), run_time=2)
        self.wait(1)
        self.play(FadeOut(title))

        string_def = Text("Strings: Sequences of characters.", font_size=36)
        self.play(Write(string_def), run_time=2)
        self.wait(1)
        self.play(FadeOut(string_def))

        example_title = Text("Example:", font_size=40)
        code_example = Code(code_string="my_string = 'Hello, World!'",
                            language="python", tab_width=4)

        self.play(Write(example_title))
        self.play(Write(code_example))
        self.wait(2)
        self.play(FadeOut(example_title), FadeOut(code_example))

        indexing_title = Text("String Indexing", font_size=40)
        indexing_example = Code(
            code_string="my_string[0]  # 'H'\nmy_string[7]  # 'W'\nmy_string[-1] # '!'", language="python", tab_width=4)

        self.play(Write(indexing_title))
        self.play(Write(indexing_example))
        self.wait(2)
        self.play(FadeOut(indexing_title), FadeOut(indexing_example))

        slicing_title = Text("String Slicing", font_size=40)
        slicing_example = Code(
            code_string="my_string[0:5]   # 'Hello'\nmy_string[7:]    # 'World!'\nmy_string[:5]    # 'Hello'", language="python", tab_width=4)

        self.play(Write(slicing_title))
        self.play(Write(slicing_example))
        self.wait(2)
        self.play(FadeOut(slicing_title), FadeOut(slicing_example))

        concatenation_title = Text("String Concatenation", font_size=40)
        concatenation_example = Code(
            code_string="str1 = 'Hello'\nstr2 = 'World'\nresult = str1 + ', ' + str2 + '!'  # 'Hello, World!'", language="python", tab_width=4)

        self.play(Write(concatenation_title))
        self.play(Write(concatenation_example))
        self.wait(2)
        self.play(FadeOut(concatenation_title), FadeOut(concatenation_example))

        methods_title = Text("Common String Methods", font_size=40)
        methods_example = Code(code_string="my_string.upper()   # 'HELLO, WORLD!'\nmy_string.lower()   # 'hello, world!'\nmy_string.replace('World', 'Manim') # 'Hello, Manim!'",
                               language="python", tab_width=4)

        self.play(Write(methods_title))
        self.play(Write(methods_example))
        self.wait(2)
        self.play(FadeOut(methods_title), FadeOut(methods_example))

        immutability_title = Text("String Immutability", font_size=40)
        immutability_text = Text(
            "Strings are immutable. You cannot change a string in place.", font_size=30)
        immutability_example = Code(
            code_string="my_string[0] = 'j' #This will raise an error", language="python", tab_width=4)
        immutability_group = VGroup(
            immutability_text, immutability_example).arrange(DOWN)

        self.play(Write(immutability_title))
        self.play(Write(immutability_group))
        self.wait(3)
        self.play(FadeOut(immutability_title), FadeOut(immutability_group))

        conclusion = Text(
            "Strings are fundamental for data manipulation!", font_size=36)
        self.play(Write(conclusion), run_time=2)
        self.wait(2)
        self.play(FadeOut(conclusion))
