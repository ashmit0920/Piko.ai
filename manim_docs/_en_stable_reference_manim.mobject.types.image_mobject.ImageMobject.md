# Source: https://docs.manim.community/en/stable/reference/manim.mobject.types.image_mobject.ImageMobject.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

ImageMobject[¶](#imagemobject "Link to this heading")
=====================================================

Qualified name: `manim.mobject.types.image\_mobject.ImageMobject`

*class* ImageMobject(*filename\_or\_array*, *scale\_to\_resolution=1080*, *invert=False*, *image\_mode='RGBA'*, *\*\*kwargs*)[[source]](../_modules/manim/mobject/types/image_mobject.html#ImageMobject)[¶](#manim.mobject.types.image_mobject.ImageMobject "Link to this definition")
:   Bases: [`AbstractImageMobject`](manim.mobject.types.image_mobject.AbstractImageMobject.html#manim.mobject.types.image_mobject.AbstractImageMobject "manim.mobject.types.image_mobject.AbstractImageMobject")

    Displays an Image from a numpy array or a file.

    Parameters:
    :   * **scale\_to\_resolution** (*int*) – At this resolution the image is placed pixel by pixel onto the screen, so it
          will look the sharpest and best.
          This is a custom parameter of ImageMobject so that rendering a scene with
          e.g. the `--quality low` or `--quality medium` flag for faster rendering
          won’t effect the position of the image on the screen.
        * **filename\_or\_array** ([*StrPath*](manim.typing.html#manim.typing.StrPath "manim.typing.StrPath") *|* *npt.NDArray*)
        * **invert** (*bool*)
        * **image\_mode** (*str*)
        * **kwargs** (*Any*)

    Example

    Example: ImageFromArray [¶](#imagefromarray)

    ![../_images/ImageFromArray-1.png](../_images/ImageFromArray-1.png)

    ```
    from manim import *

    class ImageFromArray(Scene):
        def construct(self):
            image = ImageMobject(np.uint8([[0, 100, 30, 200],
                                           [255, 0, 5, 33]]))
            image.height = 7
            self.add(image)

    ```

    ```

    class ImageFromArray(Scene):
        def construct(self):
            image = ImageMobject(np.uint8([[0, 100, 30, 200],
                                           [255, 0, 5, 33]]))
            image.height = 7
            self.add(image)


    ```

    Changing interpolation style:

    Example: ImageInterpolationEx [¶](#imageinterpolationex)

    ![../_images/ImageInterpolationEx-1.png](../_images/ImageInterpolationEx-1.png)

    ```
    from manim import *

    class ImageInterpolationEx(Scene):
        def construct(self):
            img = ImageMobject(np.uint8([[63, 0, 0, 0],
                                            [0, 127, 0, 0],
                                            [0, 0, 191, 0],
                                            [0, 0, 0, 255]
                                            ]))

            img.height = 2
            img1 = img.copy()
            img2 = img.copy()
            img3 = img.copy()
            img4 = img.copy()
            img5 = img.copy()

            img1.set_resampling_algorithm(RESAMPLING_ALGORITHMS["nearest"])
            img2.set_resampling_algorithm(RESAMPLING_ALGORITHMS["lanczos"])
            img3.set_resampling_algorithm(RESAMPLING_ALGORITHMS["linear"])
            img4.set_resampling_algorithm(RESAMPLING_ALGORITHMS["cubic"])
            img5.set_resampling_algorithm(RESAMPLING_ALGORITHMS["box"])
            img1.add(Text("nearest").scale(0.5).next_to(img1,UP))
            img2.add(Text("lanczos").scale(0.5).next_to(img2,UP))
            img3.add(Text("linear").scale(0.5).next_to(img3,UP))
            img4.add(Text("cubic").scale(0.5).next_to(img4,UP))
            img5.add(Text("box").scale(0.5).next_to(img5,UP))

            x= Group(img1,img2,img3,img4,img5)
            x.arrange()
            self.add(x)

    ```

    ```

    class ImageInterpolationEx(Scene):
        def construct(self):
            img = ImageMobject(np.uint8([[63, 0, 0, 0],
                                            [0, 127, 0, 0],
                                            [0, 0, 191, 0],
                                            [0, 0, 0, 255]
                                            ]))

            img.height = 2
            img1 = img.copy()
            img2 = img.copy()
            img3 = img.copy()
            img4 = img.copy()
            img5 = img.copy()

            img1.set_resampling_algorithm(RESAMPLING_ALGORITHMS["nearest"])
            img2.set_resampling_algorithm(RESAMPLING_ALGORITHMS["lanczos"])
            img3.set_resampling_algorithm(RESAMPLING_ALGORITHMS["linear"])
            img4.set_resampling_algorithm(RESAMPLING_ALGORITHMS["cubic"])
            img5.set_resampling_algorithm(RESAMPLING_ALGORITHMS["box"])
            img1.add(Text("nearest").scale(0.5).next_to(img1,UP))
            img2.add(Text("lanczos").scale(0.5).next_to(img2,UP))
            img3.add(Text("linear").scale(0.5).next_to(img3,UP))
            img4.add(Text("cubic").scale(0.5).next_to(img4,UP))
            img5.add(Text("box").scale(0.5).next_to(img5,UP))

            x= Group(img1,img2,img3,img4,img5)
            x.arrange()
            self.add(x)


    ```

    Methods

    |  |  |
    | --- | --- |
    | [`fade`](#manim.mobject.types.image_mobject.ImageMobject.fade "manim.mobject.types.image_mobject.ImageMobject.fade") | Sets the image's opacity using a 1 - alpha relationship. |
    | [`get_pixel_array`](#manim.mobject.types.image_mobject.ImageMobject.get_pixel_array "manim.mobject.types.image_mobject.ImageMobject.get_pixel_array") | A simple getter method. |
    | `get_style` |  |
    | [`interpolate_color`](#manim.mobject.types.image_mobject.ImageMobject.interpolate_color "manim.mobject.types.image_mobject.ImageMobject.interpolate_color") | Interpolates the array of pixel color values from one ImageMobject into an array of equal size in the target ImageMobject. |
    | [`set_color`](#manim.mobject.types.image_mobject.ImageMobject.set_color "manim.mobject.types.image_mobject.ImageMobject.set_color") | Condition is function which takes in one arguments, (x, y, z). |
    | [`set_opacity`](#manim.mobject.types.image_mobject.ImageMobject.set_opacity "manim.mobject.types.image_mobject.ImageMobject.set_opacity") | Sets the image's opacity. |

    Attributes

    |  |  |
    | --- | --- |
    | `animate` | Used to animate the application of any method of `self`. |
    | `animation_overrides` |  |
    | `depth` | The depth of the mobject. |
    | `height` | The height of the mobject. |
    | `width` | The width of the mobject. |

    \_original\_\_init\_\_(*filename\_or\_array*, *scale\_to\_resolution=1080*, *invert=False*, *image\_mode='RGBA'*, *\*\*kwargs*)[¶](#manim.mobject.types.image_mobject.ImageMobject._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **filename\_or\_array** ([*StrPath*](manim.typing.html#manim.typing.StrPath "manim.typing.StrPath") *|* *npt.NDArray*)
            * **scale\_to\_resolution** (*int*)
            * **invert** (*bool*)
            * **image\_mode** (*str*)
            * **kwargs** (*Any*)

        Return type:
        :   None

    fade(*darkness=0.5*, *family=True*)[[source]](../_modules/manim/mobject/types/image_mobject.html#ImageMobject.fade)[¶](#manim.mobject.types.image_mobject.ImageMobject.fade "Link to this definition")
    :   Sets the image’s opacity using a 1 - alpha relationship.

        Parameters:
        :   * **darkness** (*float*) – The alpha value of the object, 1 being transparent and 0 being
              opaque.
            * **family** (*bool*) – Whether the submobjects of the ImageMobject should be affected.

        Return type:
        :   Self

    get\_pixel\_array()[[source]](../_modules/manim/mobject/types/image_mobject.html#ImageMobject.get_pixel_array)[¶](#manim.mobject.types.image_mobject.ImageMobject.get_pixel_array "Link to this definition")
    :   A simple getter method.

    interpolate\_color(*mobject1*, *mobject2*, *alpha*)[[source]](../_modules/manim/mobject/types/image_mobject.html#ImageMobject.interpolate_color)[¶](#manim.mobject.types.image_mobject.ImageMobject.interpolate_color "Link to this definition")
    :   Interpolates the array of pixel color values from one ImageMobject
        into an array of equal size in the target ImageMobject.

        Parameters:
        :   * **mobject1** ([*ImageMobject*](#manim.mobject.types.image_mobject.ImageMobject "manim.mobject.types.image_mobject.ImageMobject")) – The ImageMobject to transform from.
            * **mobject2** ([*ImageMobject*](#manim.mobject.types.image_mobject.ImageMobject "manim.mobject.types.image_mobject.ImageMobject")) – The ImageMobject to transform into.
            * **alpha** (*float*) – Used to track the lerp relationship. Not opacity related.

        Return type:
        :   None

    set\_color(*color*, *alpha=None*, *family=True*)[[source]](../_modules/manim/mobject/types/image_mobject.html#ImageMobject.set_color)[¶](#manim.mobject.types.image_mobject.ImageMobject.set_color "Link to this definition")
    :   Condition is function which takes in one arguments, (x, y, z).
        Here it just recurses to submobjects, but in subclasses this
        should be further implemented based on the the inner workings
        of color

    set\_opacity(*alpha*)[[source]](../_modules/manim/mobject/types/image_mobject.html#ImageMobject.set_opacity)[¶](#manim.mobject.types.image_mobject.ImageMobject.set_opacity "Link to this definition")
    :   Sets the image’s opacity.

        Parameters:
        :   **alpha** (*float*) – The alpha value of the object, 1 being opaque and 0 being
            transparent.

        Return type:
        :   Self