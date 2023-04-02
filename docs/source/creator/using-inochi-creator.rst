Using Inochi Creator
====================

After `First Time Setup <https://docs.inochi2d.com/en/latest/creator/getting-started.html#first-time-setup>`__, on launch, a new Welcome Screen will pop up. This screen gives you quick access to project management and Inochi2D related links.

Panels
------

With the default settings, there are 3 Panels enabled in the Inochi Creator Window. These 3 Panels are:

.. list-table::
    :header-rows: 1

    * - Name
      - Contains
    * - Parameters
      - All parameters
    * - Nodes
      - The Node Tree 
    * - Inspector
      - Selected Node or Puppet information

.. note::

    Some Panels are only usable in a certain modes.

------

Canvas
------

The Canvas is an infinite space that contains the model and context specific buttons.

To move around the Canvas you hold right-click on any space and drag towards the direction you want to move. At the bottom of the Canvas, there is a bar that displays the zoom value as well as the current X and Y values on the Canvas. After a change, these values can both be reset with the reset button to the right.

Gizmos
^^^^^^

When no parameters are in Arming Mode, the Canvas will have a Gizmo Button on the top-right, allowing you to hide certain visual guides on nodes and change the Canvas' background color. These are the 4 options:


.. list-table::
    :header-rows: 1

    * - Label
      - Action
    * - Vertices
      - Show/Hide Toggle
    * - Bounds
      - Show/Hide Toggle
    * - Orientation
      - Show/Hide Toggle
    * - Color
      - Change background color

-----

Nodes
-----

Nodes are the fundamental building blocks to connecting the cuts of a model.

Node Options
^^^^^^^^^^^^

.. list-table::
    :header-rows: 1

    * - Label
      - Action
    * - Enable Physics
      - Enables Physics on the model.
    * - Enable Post-Processing
      - Enables Post-Processing on nodes with an Emissive. Useful for making nodes glow.
    * - Reset Physics
      - ?
    * - Configure Flip Pairings
      - ?

Selecting Nodes
^^^^^^^^^^^^^^^

You can select nodes either by left-clicking them in the Node Tree or by right-clicking the model, opening a popup menu to select between nearby nodes. To select more than one node, you can hold ``Ctrl`` and click other nodes using either selection method.

If a Gizmo is toggled on, upon selection, the node will show the respective Gizmo.

------

Meshes
------

Meshes are the shapes given to nodes that allow the nodes to be morphed as though they are 3D with depth rather than 2D. This shape is made out of vertices around and inside the node.

Editing Meshes
^^^^^^^^^^^^^^

While a node is selected, an Edit Mesh Button will appear in the bottom-left of the Canvas. Clicking this button will enter Vertex Edit Mode, focusing on the selected node.

Vertex Mode
^^^^^^^^^^^

While in Vertex Mode, you can create, edit, or delete meshes. 

----------

Parameters
----------

Parameters are tools that allow for creating the movement and physics of your nodes. To create a new parameter, you must click the plus button on the bottom right of the Parameters Panel. This opens a popup menu with the 5 types of parameters:

Parameter Types
^^^^^^^^^^^^^^^

.. list-table::
    :header-rows: 1

    * - Name
      - Description
    * - 1D Parameter (0..1)
      - A one-dimensional parameter with 2 axes points, one on each end.
    * - 1D Parameter (-1..1)
      - A one-dimensional parameter with 3 axes points, one on each each with an axes point in the middle.
    * - 2D Parameter (0..1)
      - A two-dimensional parameter with 4 axes points, one on each of the 4 corners.
    * - 2D Parameter (-1..+1)
      - A two-dimensional parameter with 9 axes points, one on each of the 4 corners, one in the middle, and one in between each corner axis point.
    * - Mouth Shape
      - ?

Axes Points
^^^^^^^^^^^

Axes Points are used for arming parameters within the parameter's constraints. When a parameter is newly added, the axes points are grey and lack Bindings.

When more than one axis point has Bindings, the points in between will automatically interpolate the model's movements accordingly. The axes points will change from grey to yellow when their Bindings will be interpolated. Otherwise, they will be green when they have Bindings.

Arming Parameters
^^^^^^^^^^^^^^^^^

In order to rig the movement or physics for the model, you must arm parameters' axes points with the values of the tranformations and deformations of the selected node(s). The list of nodes with changed values at an axis point are called *Bindings*. 

To begin arming, click the Arm Parameter Button below the Cog Wheel Button of the parameter. The Arm Parameter Button should now be red, signifying which parameter is currently selected for recording movement.

It is important to understand that the currently selected axis point is the only point in the parameter that receives new Bindings. From here, you can choose the appropriate axis point and begin rigging the model using the *Parameter Tools*, the Inspector, and on-Canvas tranformation buttons to add Bindings.

---------------

Parameter Tools
---------------

Once a parameter is armed and at least 1 node is selected, the Gizmo Button will be hidden and instead two new buttons on the top-left will be shown on the Canvas; the Vertex Tool and the Path Deform Tool.

Vertex Tool
^^^^^^^^^^^

The Vertex Tool is used for selecting vertices to transform them, allowing for finer-tuned movement of meshes. The Vertex Tool Button has a pencil icon.

While the Vertex Tool is selected, you can select a vertex by left-clicking it, or you can hold left-click to drag select multiple vertices. When selected, you can transform the vertices accordingly. 

You can either manually drag vertices to transform them, or use the Inspector for more precise tranformations.

Path Deform Tool
^^^^^^^^^^^^^^^^

The Path Deform Tool is used for deforming meshes, different from simply transforming meshes. This is helpful for movements that are at an angle or curved, such as rotating the model's body parts or leg movement.

To use the Path Deform Tool, click the Path Deform Tool Button with the zig-zagging arrow icon. Next, double-click a space past the two ends of the node. To delete a point, double-click the point again. If you want the path to be curved, add another point in between the path and move that point with a left-click drag. 

To lock a point in place, hold ``Ctrl`` and click it. If you wish to move a point between the end points, shift-click and drag it along the path.

When the path is satisfactory, press ``Tab`` to switch to Deform Mode. The path becomes green indicating that moving the unlocked points will now deform the node. To switch back to Path Editing Mode, press ``Tab`` again.

.. note::

    You must extend the path from the Path Deform Tool past the end points of the selected node to ensure all vertices will be properly deformed.