# Source: https://docs.manim.community/en/stable/reference/manim.utils.space_ops.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

space\_ops[¶](#module-manim.utils.space_ops "Link to this heading")
===================================================================

Utility functions for two- and three-dimensional vectors.

Functions

R3\_to\_complex(*point*)[[source]](../_modules/manim/utils/space_ops.html#R3_to_complex)[¶](#manim.utils.space_ops.R3_to_complex "Link to this definition")
:   Parameters:
    :   **point** (*Sequence**[**float**]*)

    Return type:
    :   *ndarray*

angle\_axis\_from\_quaternion(*quaternion*)[[source]](../_modules/manim/utils/space_ops.html#angle_axis_from_quaternion)[¶](#manim.utils.space_ops.angle_axis_from_quaternion "Link to this definition")
:   Gets angle and axis from a quaternion.

    Parameters:
    :   **quaternion** (*Sequence**[**float**]*) – The quaternion from which we get the angle and axis.

    Returns:
    :   Gives the angle and axis

    Return type:
    :   Sequence[float]

angle\_between\_vectors(*v1*, *v2*)[[source]](../_modules/manim/utils/space_ops.html#angle_between_vectors)[¶](#manim.utils.space_ops.angle_between_vectors "Link to this definition")
:   Returns the angle between two vectors.
    This angle will always be between 0 and pi

    Parameters:
    :   * **v1** (*ndarray*) – The first vector.
        * **v2** (*ndarray*) – The second vector.

    Returns:
    :   The angle between the vectors.

    Return type:
    :   float

angle\_of\_vector(*vector*)[[source]](../_modules/manim/utils/space_ops.html#angle_of_vector)[¶](#manim.utils.space_ops.angle_of_vector "Link to this definition")
:   Returns polar coordinate theta when vector is projected on xy plane.

    Parameters:
    :   **vector** (*Sequence**[**float**]* *|* *ndarray*) – The vector to find the angle for.

    Returns:
    :   The angle of the vector projected.

    Return type:
    :   float

cartesian\_to\_spherical(*vec*)[[source]](../_modules/manim/utils/space_ops.html#cartesian_to_spherical)[¶](#manim.utils.space_ops.cartesian_to_spherical "Link to this definition")
:   Returns an array of numbers corresponding to each
    polar coordinate value (distance, phi, theta).

    Parameters:
    :   **vec** (*Sequence**[**float**]*) – A numpy array `[x, y, z]`.

    Return type:
    :   *ndarray*

center\_of\_mass(*points*)[[source]](../_modules/manim/utils/space_ops.html#center_of_mass)[¶](#manim.utils.space_ops.center_of_mass "Link to this definition")
:   Gets the center of mass of the points in space.

    Parameters:
    :   **points** ([*PointNDLike\_Array*](manim.typing.html#manim.typing.PointNDLike_Array "manim.typing.PointNDLike_Array")) – The points to find the center of mass from.

    Returns:
    :   The center of mass of the points.

    Return type:
    :   np.ndarray

compass\_directions(*n=4*, *start\_vect=array([1., 0., 0.])*)[[source]](../_modules/manim/utils/space_ops.html#compass_directions)[¶](#manim.utils.space_ops.compass_directions "Link to this definition")
:   Finds the cardinal directions using tau.

    Parameters:
    :   * **n** (*int*) – The amount to be rotated, by default 4
        * **start\_vect** (*ndarray*) – The direction for the angle to start with, by default RIGHT

    Returns:
    :   The angle which has been rotated.

    Return type:
    :   np.ndarray

complex\_func\_to\_R3\_func(*complex\_func*)[[source]](../_modules/manim/utils/space_ops.html#complex_func_to_R3_func)[¶](#manim.utils.space_ops.complex_func_to_R3_func "Link to this definition")
:   Parameters:
    :   **complex\_func** (*Callable**[**[**complex**]**,* *complex**]*)

    Return type:
    :   *Callable*[[[*Point3DLike*](manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike")], [*Point3D*](manim.typing.html#manim.typing.Point3D "manim.typing.Point3D")]

complex\_to\_R3(*complex\_num*)[[source]](../_modules/manim/utils/space_ops.html#complex_to_R3)[¶](#manim.utils.space_ops.complex_to_R3 "Link to this definition")
:   Parameters:
    :   **complex\_num** (*complex*)

    Return type:
    :   *ndarray*

cross(*v1*, *v2*)[[source]](../_modules/manim/utils/space_ops.html#cross)[¶](#manim.utils.space_ops.cross "Link to this definition")
:   Parameters:
    :   * **v1** ([*Vector3D*](manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D"))
        * **v2** ([*Vector3D*](manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D"))

    Return type:
    :   [*Vector3D*](manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D")

cross2d(*a*, *b*)[[source]](../_modules/manim/utils/space_ops.html#cross2d)[¶](#manim.utils.space_ops.cross2d "Link to this definition")
:   Compute the determinant(s) of the passed
    vector (sequences).

    Parameters:
    :   * **a** ([*Vector2D*](manim.typing.html#manim.typing.Vector2D "manim.typing.Vector2D") *|* [*Vector2D\_Array*](manim.typing.html#manim.typing.Vector2D_Array "manim.typing.Vector2D_Array")) – A vector or a sequence of vectors.
        * **b** ([*Vector2D*](manim.typing.html#manim.typing.Vector2D "manim.typing.Vector2D") *|* [*Vector2D\_Array*](manim.typing.html#manim.typing.Vector2D_Array "manim.typing.Vector2D_Array")) – A vector or a sequence of vectors.

    Returns:
    :   The determinant or sequence of determinants
        of the first two components of the specified
        vectors.

    Return type:
    :   Sequence[float] | float

    Examples

    ```
    >>> cross2d(np.array([1, 2]), np.array([3, 4]))
    np.int64(-2)
    >>> cross2d(
    ...     np.array([[1, 2, 0], [1, 0, 0]]),
    ...     np.array([[3, 4, 0], [0, 1, 0]]),
    ... )
    array([-2,  1])

    ```

earclip\_triangulation(*verts*, *ring\_ends*)[[source]](../_modules/manim/utils/space_ops.html#earclip_triangulation)[¶](#manim.utils.space_ops.earclip_triangulation "Link to this definition")
:   Returns a list of indices giving a triangulation
    of a polygon, potentially with holes.

    Parameters:
    :   * **verts** (*ndarray*) – verts is a numpy array of points.
        * **ring\_ends** (*list*) – ring\_ends is a list of indices indicating where
          the ends of new paths are.

    Returns:
    :   A list of indices giving a triangulation of a polygon.

    Return type:
    :   list

find\_intersection(*p0s*, *v0s*, *p1s*, *v1s*, *threshold=1e-05*)[[source]](../_modules/manim/utils/space_ops.html#find_intersection)[¶](#manim.utils.space_ops.find_intersection "Link to this definition")
:   Return the intersection of a line passing through p0 in direction v0
    with one passing through p1 in direction v1 (or array of intersections
    from arrays of such points/directions).
    For 3d values, it returns the point on the ray p0 + v0 \* t closest to the
    ray p1 + v1 \* t

    Parameters:
    :   * **p0s** ([*Point3DLike\_Array*](manim.typing.html#manim.typing.Point3DLike_Array "manim.typing.Point3DLike_Array"))
        * **v0s** ([*Vector3D\_Array*](manim.typing.html#manim.typing.Vector3D_Array "manim.typing.Vector3D_Array"))
        * **p1s** ([*Point3DLike\_Array*](manim.typing.html#manim.typing.Point3DLike_Array "manim.typing.Point3DLike_Array"))
        * **v1s** ([*Vector3D\_Array*](manim.typing.html#manim.typing.Vector3D_Array "manim.typing.Vector3D_Array"))
        * **threshold** (*float*)

    Return type:
    :   list[[*Point3D*](manim.typing.html#manim.typing.Point3D "manim.typing.Point3D")]

get\_unit\_normal(*v1*, *v2*, *tol=1e-06*)[[source]](../_modules/manim/utils/space_ops.html#get_unit_normal)[¶](#manim.utils.space_ops.get_unit_normal "Link to this definition")
:   Gets the unit normal of the vectors.

    Parameters:
    :   * **v1** ([*Vector3D*](manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D")) – The first vector.
        * **v2** ([*Vector3D*](manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D")) – The second vector
        * **tol** (*float*) – [description], by default 1e-6

    Returns:
    :   The normal of the two vectors.

    Return type:
    :   np.ndarray

get\_winding\_number(*points*)[[source]](../_modules/manim/utils/space_ops.html#get_winding_number)[¶](#manim.utils.space_ops.get_winding_number "Link to this definition")
:   Determine the number of times a polygon winds around the origin.

    The orientation is measured mathematically positively, i.e.,
    counterclockwise.

    Parameters:
    :   **points** (*Sequence**[**ndarray**]*) – The vertices of the polygon being queried.

    Return type:
    :   float

    Examples

    ```
    >>> from manim import Square, get_winding_number
    >>> polygon = Square()
    >>> get_winding_number(polygon.get_vertices())
    np.float64(1.0)
    >>> polygon.shift(2 * UP)
    Square
    >>> get_winding_number(polygon.get_vertices())
    np.float64(0.0)

    ```

line\_intersection(*line1*, *line2*)[[source]](../_modules/manim/utils/space_ops.html#line_intersection)[¶](#manim.utils.space_ops.line_intersection "Link to this definition")
:   Returns the intersection point of two lines, each defined by
    a pair of distinct points lying on the line.

    Parameters:
    :   * **line1** (*Sequence**[**ndarray**]*) – A list of two points that determine the first line.
        * **line2** (*Sequence**[**ndarray**]*) – A list of two points that determine the second line.

    Returns:
    :   The intersection points of the two lines which are intersecting.

    Return type:
    :   np.ndarray

    Raises:
    :   **ValueError** – Error is produced if the two lines don’t intersect with each other
        or if the coordinates don’t lie on the xy-plane.

midpoint(*point1*, *point2*)[[source]](../_modules/manim/utils/space_ops.html#midpoint)[¶](#manim.utils.space_ops.midpoint "Link to this definition")
:   Gets the midpoint of two points.

    Parameters:
    :   * **point1** (*Sequence**[**float**]*) – The first point.
        * **point2** (*Sequence**[**float**]*) – The second point.

    Returns:
    :   The midpoint of the points

    Return type:
    :   [Union](manim.mobject.geometry.boolean_ops.Union.html#manim.mobject.geometry.boolean_ops.Union "manim.mobject.geometry.boolean_ops.Union")[float, np.ndarray]

norm\_squared(*v*)[[source]](../_modules/manim/utils/space_ops.html#norm_squared)[¶](#manim.utils.space_ops.norm_squared "Link to this definition")
:   Parameters:
    :   **v** (*float*)

    Return type:
    :   float

normalize(*vect*, *fall\_back=None*)[[source]](../_modules/manim/utils/space_ops.html#normalize)[¶](#manim.utils.space_ops.normalize "Link to this definition")
:   Parameters:
    :   * **vect** (*ndarray* *|* *tuple**[**float**]*)
        * **fall\_back** (*ndarray* *|* *None*)

    Return type:
    :   *ndarray*

normalize\_along\_axis(*array*, *axis*)[[source]](../_modules/manim/utils/space_ops.html#normalize_along_axis)[¶](#manim.utils.space_ops.normalize_along_axis "Link to this definition")
:   Normalizes an array with the provided axis.

    Parameters:
    :   * **array** (*ndarray*) – The array which has to be normalized.
        * **axis** (*ndarray*) – The axis to be normalized to.

    Returns:
    :   Array which has been normalized according to the axis.

    Return type:
    :   np.ndarray

perpendicular\_bisector(*line*, *norm\_vector=array([0., 0., 1.])*)[[source]](../_modules/manim/utils/space_ops.html#perpendicular_bisector)[¶](#manim.utils.space_ops.perpendicular_bisector "Link to this definition")
:   Returns a list of two points that correspond
    to the ends of the perpendicular bisector of the
    two points given.

    Parameters:
    :   * **line** (*Sequence**[**ndarray**]*) – a list of two numpy array points (corresponding
          to the ends of a line).
        * **norm\_vector** ([*Vector3D*](manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D")) – the vector perpendicular to both the line given
          and the perpendicular bisector.

    Returns:
    :   A list of two numpy array points that correspond
        to the ends of the perpendicular bisector

    Return type:
    :   list

quaternion\_conjugate(*quaternion*)[[source]](../_modules/manim/utils/space_ops.html#quaternion_conjugate)[¶](#manim.utils.space_ops.quaternion_conjugate "Link to this definition")
:   Used for finding the conjugate of the quaternion

    Parameters:
    :   **quaternion** (*Sequence**[**float**]*) – The quaternion for which you want to find the conjugate for.

    Returns:
    :   The conjugate of the quaternion.

    Return type:
    :   np.ndarray

quaternion\_from\_angle\_axis(*angle*, *axis*, *axis\_normalized=False*)[[source]](../_modules/manim/utils/space_ops.html#quaternion_from_angle_axis)[¶](#manim.utils.space_ops.quaternion_from_angle_axis "Link to this definition")
:   Gets a quaternion from an angle and an axis.
    For more information, check [this Wikipedia page](https://en.wikipedia.org/wiki/Conversion_between_quaternions_and_Euler_angles).

    Parameters:
    :   * **angle** (*float*) – The angle for the quaternion.
        * **axis** (*ndarray*) – The axis for the quaternion
        * **axis\_normalized** (*bool*) – Checks whether the axis is normalized, by default False

    Returns:
    :   Gives back a quaternion from the angle and axis

    Return type:
    :   list[float]

quaternion\_mult(*\*quats*)[[source]](../_modules/manim/utils/space_ops.html#quaternion_mult)[¶](#manim.utils.space_ops.quaternion_mult "Link to this definition")
:   Gets the Hamilton product of the quaternions provided.
    For more information, check [this Wikipedia page](https://en.wikipedia.org/wiki/Quaternion).

    Returns:
    :   Returns a list of product of two quaternions.

    Return type:
    :   [Union](manim.mobject.geometry.boolean_ops.Union.html#manim.mobject.geometry.boolean_ops.Union "manim.mobject.geometry.boolean_ops.Union")[np.ndarray, List[[Union](manim.mobject.geometry.boolean_ops.Union.html#manim.mobject.geometry.boolean_ops.Union "manim.mobject.geometry.boolean_ops.Union")[float, np.ndarray]]]

    Parameters:
    :   **quats** (*Sequence**[**float**]*)

regular\_vertices(*n*, *\**, *radius=1*, *start\_angle=None*)[[source]](../_modules/manim/utils/space_ops.html#regular_vertices)[¶](#manim.utils.space_ops.regular_vertices "Link to this definition")
:   Generates regularly spaced vertices around a circle centered at the origin.

    Parameters:
    :   * **n** (*int*) – The number of vertices
        * **radius** (*float*) – The radius of the circle that the vertices are placed on.
        * **start\_angle** (*float* *|* *None*) –

          The angle the vertices start at.

          If unspecified, for even `n` values, `0` will be used.
          For odd `n` values, 90 degrees is used.

    Returns:
    :   * **vertices** (`numpy.ndarray`) – The regularly spaced vertices.
        * **start\_angle** (`float`) – The angle the vertices start at.

    Return type:
    :   tuple[*ndarray*, float]

rotate\_vector(*vector*, *angle*, *axis=array([0., 0., 1.])*)[[source]](../_modules/manim/utils/space_ops.html#rotate_vector)[¶](#manim.utils.space_ops.rotate_vector "Link to this definition")
:   Function for rotating a vector.

    Parameters:
    :   * **vector** (*ndarray*) – The vector to be rotated.
        * **angle** (*float*) – The angle to be rotated by.
        * **axis** (*ndarray*) – The axis to be rotated, by default OUT

    Returns:
    :   The rotated vector with provided angle and axis.

    Return type:
    :   np.ndarray

    Raises:
    :   **ValueError** – If vector is not of dimension 2 or 3.

rotation\_about\_z(*angle*)[[source]](../_modules/manim/utils/space_ops.html#rotation_about_z)[¶](#manim.utils.space_ops.rotation_about_z "Link to this definition")
:   Returns a rotation matrix for a given angle.

    Parameters:
    :   **angle** (*float*) – Angle for the rotation matrix.

    Returns:
    :   Gives back the rotated matrix.

    Return type:
    :   np.ndarray

rotation\_matrix(*angle*, *axis*, *homogeneous=False*)[[source]](../_modules/manim/utils/space_ops.html#rotation_matrix)[¶](#manim.utils.space_ops.rotation_matrix "Link to this definition")
:   Rotation in R^3 about a specified axis of rotation.

    Parameters:
    :   * **angle** (*float*)
        * **axis** (*ndarray*)
        * **homogeneous** (*bool*)

    Return type:
    :   *ndarray*

rotation\_matrix\_from\_quaternion(*quat*)[[source]](../_modules/manim/utils/space_ops.html#rotation_matrix_from_quaternion)[¶](#manim.utils.space_ops.rotation_matrix_from_quaternion "Link to this definition")
:   Parameters:
    :   **quat** (*ndarray*)

    Return type:
    :   *ndarray*

rotation\_matrix\_transpose(*angle*, *axis*)[[source]](../_modules/manim/utils/space_ops.html#rotation_matrix_transpose)[¶](#manim.utils.space_ops.rotation_matrix_transpose "Link to this definition")
:   Parameters:
    :   * **angle** (*float*)
        * **axis** (*ndarray*)

    Return type:
    :   *ndarray*

rotation\_matrix\_transpose\_from\_quaternion(*quat*)[[source]](../_modules/manim/utils/space_ops.html#rotation_matrix_transpose_from_quaternion)[¶](#manim.utils.space_ops.rotation_matrix_transpose_from_quaternion "Link to this definition")
:   Converts the quaternion, quat, to an equivalent rotation matrix representation.
    For more information, check [this page](https://in.mathworks.com/help/driving/ref/quaternion.rotmat.html).

    Parameters:
    :   **quat** (*ndarray*) – The quaternion which is to be converted.

    Returns:
    :   Gives back the Rotation matrix representation, returned as a 3-by-3
        matrix or 3-by-3-by-N multidimensional array.

    Return type:
    :   List[np.ndarray]

shoelace(*x\_y*)[[source]](../_modules/manim/utils/space_ops.html#shoelace)[¶](#manim.utils.space_ops.shoelace "Link to this definition")
:   2D implementation of the shoelace formula.

    Returns:
    :   Returns signed area.

    Return type:
    :   `float`

    Parameters:
    :   **x\_y** ([*Point2D\_Array*](manim.typing.html#manim.typing.Point2D_Array "manim.typing.Point2D_Array"))

shoelace\_direction(*x\_y*)[[source]](../_modules/manim/utils/space_ops.html#shoelace_direction)[¶](#manim.utils.space_ops.shoelace_direction "Link to this definition")
:   Uses the area determined by the shoelace method to determine whether
    the input set of points is directed clockwise or counterclockwise.

    Returns:
    :   Either `"CW"` or `"CCW"`.

    Return type:
    :   `str`

    Parameters:
    :   **x\_y** ([*Point2D\_Array*](manim.typing.html#manim.typing.Point2D_Array "manim.typing.Point2D_Array"))

spherical\_to\_cartesian(*spherical*)[[source]](../_modules/manim/utils/space_ops.html#spherical_to_cartesian)[¶](#manim.utils.space_ops.spherical_to_cartesian "Link to this definition")
:   Returns a numpy array `[x, y, z]` based on the spherical
    coordinates given.

    Parameters:
    :   **spherical** (*Sequence**[**float**]*) –

        A list of three floats that correspond to the following:

        r - The distance between the point and the origin.

        theta - The azimuthal angle of the point to the positive x-axis.

        phi - The vertical angle of the point to the positive z-axis.

    Return type:
    :   *ndarray*

thick\_diagonal(*dim*, *thickness=2*)[[source]](../_modules/manim/utils/space_ops.html#thick_diagonal)[¶](#manim.utils.space_ops.thick_diagonal "Link to this definition")
:   Parameters:
    :   * **dim** (*int*)
        * **thickness** (*int*)

    Return type:
    :   [*MatrixMN*](manim.typing.html#manim.typing.MatrixMN "manim.typing.MatrixMN")

z\_to\_vector(*vector*)[[source]](../_modules/manim/utils/space_ops.html#z_to_vector)[¶](#manim.utils.space_ops.z_to_vector "Link to this definition")
:   Returns some matrix in SO(3) which takes the z-axis to the
    (normalized) vector provided as an argument

    Parameters:
    :   **vector** (*ndarray*)

    Return type:
    :   *ndarray*