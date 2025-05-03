# Source: https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.TipableVMobject.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

TipableVMobject[¶](#tipablevmobject "Link to this heading")
===========================================================

Qualified name: `manim.mobject.geometry.arc.TipableVMobject`

*class* TipableVMobject(*tip\_length=0.35*, *normal\_vector=array([0., 0., 1.])*, *tip\_style={}*, *\*\*kwargs*)[[source]](../_modules/manim/mobject/geometry/arc.html#TipableVMobject)[¶](#manim.mobject.geometry.arc.TipableVMobject "Link to this definition")
:   Bases: [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject")

    Meant for shared functionality between Arc and Line.
    Functionality can be classified broadly into these groups:

    > * Adding, Creating, Modifying tips
    >   :   + add\_tip calls create\_tip, before pushing the new tip
    >         :   into the TipableVMobject’s list of submobjects
    >       + stylistic and positional configuration
    > * Checking for tips
    >   :   + Boolean checks for whether the TipableVMobject has a tip
    >         :   and a starting tip
    > * Getters
    >   :   + Straightforward accessors, returning information pertaining
    >         :   to the TipableVMobject instance’s tip(s), its length etc

    Methods

    |  |  |
    | --- | --- |
    | [`add_tip`](#manim.mobject.geometry.arc.TipableVMobject.add_tip "manim.mobject.geometry.arc.TipableVMobject.add_tip") | Adds a tip to the TipableVMobject instance, recognising that the endpoints might need to be switched if it's a 'starting tip' or not. |
    | `asign_tip_attr` |  |
    | [`create_tip`](#manim.mobject.geometry.arc.TipableVMobject.create_tip "manim.mobject.geometry.arc.TipableVMobject.create_tip") | Stylises the tip, positions it spatially, and returns the newly instantiated tip to the caller. |
    | `get_default_tip_length` |  |
    | [`get_end`](#manim.mobject.geometry.arc.TipableVMobject.get_end "manim.mobject.geometry.arc.TipableVMobject.get_end") | Returns the point, where the stroke that surrounds the [`Mobject`](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") ends. |
    | `get_first_handle` |  |
    | `get_last_handle` |  |
    | `get_length` |  |
    | [`get_start`](#manim.mobject.geometry.arc.TipableVMobject.get_start "manim.mobject.geometry.arc.TipableVMobject.get_start") | Returns the point, where the stroke that surrounds the [`Mobject`](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") starts. |
    | [`get_tip`](#manim.mobject.geometry.arc.TipableVMobject.get_tip "manim.mobject.geometry.arc.TipableVMobject.get_tip") | Returns the TipableVMobject instance's (first) tip, otherwise throws an exception. |
    | [`get_tips`](#manim.mobject.geometry.arc.TipableVMobject.get_tips "manim.mobject.geometry.arc.TipableVMobject.get_tips") | Returns a VGroup (collection of VMobjects) containing the TipableVMObject instance's tips. |
    | [`get_unpositioned_tip`](#manim.mobject.geometry.arc.TipableVMobject.get_unpositioned_tip "manim.mobject.geometry.arc.TipableVMobject.get_unpositioned_tip") | Returns a tip that has been stylistically configured, but has not yet been given a position in space. |
    | `has_start_tip` |  |
    | `has_tip` |  |
    | `pop_tips` |  |
    | `position_tip` |  |
    | `reset_endpoints_based_on_tip` |  |

    Attributes

    |  |  |
    | --- | --- |
    | `animate` | Used to animate the application of any method of `self`. |
    | `animation_overrides` |  |
    | `color` |  |
    | `depth` | The depth of the mobject. |
    | `fill_color` | If there are multiple colors (for gradient) this returns the first one |
    | `height` | The height of the mobject. |
    | `n_points_per_curve` |  |
    | `sheen_factor` |  |
    | `stroke_color` |  |
    | `width` | The width of the mobject. |

    Parameters:
    :   * **tip\_length** (*float*)
        * **normal\_vector** ([*Vector3D*](manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D"))
        * **tip\_style** (*dict*)
        * **kwargs** (*Any*)

    \_original\_\_init\_\_(*tip\_length=0.35*, *normal\_vector=array([0., 0., 1.])*, *tip\_style={}*, *\*\*kwargs*)[¶](#manim.mobject.geometry.arc.TipableVMobject._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **tip\_length** (*float*)
            * **normal\_vector** ([*Vector3D*](manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D"))
            * **tip\_style** (*dict*)
            * **kwargs** (*Any*)

        Return type:
        :   None

    add\_tip(*tip=None*, *tip\_shape=None*, *tip\_length=None*, *tip\_width=None*, *at\_start=False*)[[source]](../_modules/manim/mobject/geometry/arc.html#TipableVMobject.add_tip)[¶](#manim.mobject.geometry.arc.TipableVMobject.add_tip "Link to this definition")
    :   Adds a tip to the TipableVMobject instance, recognising
        that the endpoints might need to be switched if it’s
        a ‘starting tip’ or not.

        Parameters:
        :   * **tip** ([*tips.ArrowTip*](manim.mobject.geometry.tips.ArrowTip.html#manim.mobject.geometry.tips.ArrowTip "manim.mobject.geometry.tips.ArrowTip") *|* *None*)
            * **tip\_shape** (*type**[*[*tips.ArrowTip*](manim.mobject.geometry.tips.ArrowTip.html#manim.mobject.geometry.tips.ArrowTip "manim.mobject.geometry.tips.ArrowTip")*]* *|* *None*)
            * **tip\_length** (*float* *|* *None*)
            * **tip\_width** (*float* *|* *None*)
            * **at\_start** (*bool*)

        Return type:
        :   Self

    create\_tip(*tip\_shape=None*, *tip\_length=None*, *tip\_width=None*, *at\_start=False*)[[source]](../_modules/manim/mobject/geometry/arc.html#TipableVMobject.create_tip)[¶](#manim.mobject.geometry.arc.TipableVMobject.create_tip "Link to this definition")
    :   Stylises the tip, positions it spatially, and returns
        the newly instantiated tip to the caller.

        Parameters:
        :   * **tip\_shape** (*type**[*[*tips.ArrowTip*](manim.mobject.geometry.tips.ArrowTip.html#manim.mobject.geometry.tips.ArrowTip "manim.mobject.geometry.tips.ArrowTip")*]* *|* *None*)
            * **tip\_length** (*float* *|* *None*)
            * **tip\_width** (*float* *|* *None*)
            * **at\_start** (*bool*)

        Return type:
        :   [tips.ArrowTip](manim.mobject.geometry.tips.ArrowTip.html#manim.mobject.geometry.tips.ArrowTip "manim.mobject.geometry.tips.ArrowTip")

    get\_end()[[source]](../_modules/manim/mobject/geometry/arc.html#TipableVMobject.get_end)[¶](#manim.mobject.geometry.arc.TipableVMobject.get_end "Link to this definition")
    :   Returns the point, where the stroke that surrounds the [`Mobject`](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") ends.

        Return type:
        :   [*Point3D*](manim.typing.html#manim.typing.Point3D "manim.typing.Point3D")

    get\_start()[[source]](../_modules/manim/mobject/geometry/arc.html#TipableVMobject.get_start)[¶](#manim.mobject.geometry.arc.TipableVMobject.get_start "Link to this definition")
    :   Returns the point, where the stroke that surrounds the [`Mobject`](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") starts.

        Return type:
        :   [*Point3D*](manim.typing.html#manim.typing.Point3D "manim.typing.Point3D")

    get\_tip()[[source]](../_modules/manim/mobject/geometry/arc.html#TipableVMobject.get_tip)[¶](#manim.mobject.geometry.arc.TipableVMobject.get_tip "Link to this definition")
    :   Returns the TipableVMobject instance’s (first) tip,
        otherwise throws an exception.

        Return type:
        :   [*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject")

    get\_tips()[[source]](../_modules/manim/mobject/geometry/arc.html#TipableVMobject.get_tips)[¶](#manim.mobject.geometry.arc.TipableVMobject.get_tips "Link to this definition")
    :   Returns a VGroup (collection of VMobjects) containing
        the TipableVMObject instance’s tips.

        Return type:
        :   [*VGroup*](manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup")

    get\_unpositioned\_tip(*tip\_shape=None*, *tip\_length=None*, *tip\_width=None*)[[source]](../_modules/manim/mobject/geometry/arc.html#TipableVMobject.get_unpositioned_tip)[¶](#manim.mobject.geometry.arc.TipableVMobject.get_unpositioned_tip "Link to this definition")
    :   Returns a tip that has been stylistically configured,
        but has not yet been given a position in space.

        Parameters:
        :   * **tip\_shape** (*type**[*[*tips.ArrowTip*](manim.mobject.geometry.tips.ArrowTip.html#manim.mobject.geometry.tips.ArrowTip "manim.mobject.geometry.tips.ArrowTip")*]* *|* *None*)
            * **tip\_length** (*float* *|* *None*)
            * **tip\_width** (*float* *|* *None*)

        Return type:
        :   [tips.ArrowTip](manim.mobject.geometry.tips.ArrowTip.html#manim.mobject.geometry.tips.ArrowTip "manim.mobject.geometry.tips.ArrowTip") | [tips.ArrowTriangleFilledTip](manim.mobject.geometry.tips.ArrowTriangleFilledTip.html#manim.mobject.geometry.tips.ArrowTriangleFilledTip "manim.mobject.geometry.tips.ArrowTriangleFilledTip")