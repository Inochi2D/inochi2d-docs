=====================================
Welcome to the Inochi2D Documentation
=====================================

On this page, you will find documentation for the officially supported projects under the Inochi2D banner.
Use the sidebar on the left to select a project to get documentation from, and a topic you want to read about.

What is Inochi2D?
-----------------

Inochi2D is an open source specification for a 2D character animation system that allows characters to be animated in real-time for games and VTubing. Inochi2D achieves this by deforming textures in real time based on parameters the rigger sets in Inochi Creator.

This documentation page covers:
  - Inochi Creator
  - Inochi Session
  - Inochi2D Specification for implementers
  - Inochi2D SDK for developers

**Inochi Creator** is the official tooling to create animated rigs for use with Inochi2D compliant software and games.

**Inochi Session** is the official tooling to use Inochi2D models for VTubing, using various forms of body and face tracking.

**Inochi2D Specification** is meant for developers that want to implement Inochi2D in their preferred engine.

**Inochi2D SDK** is the official Software Development Kit that allows integrating Inochi2D in to your games and software.

--------

Meet Ada
________

..
   TOOD: commission some art of ada that goes here instead of the chibi hi
   Art should be non-chibi

.. image:: img/ada-hi.png
   :align: center
   :width: 50%

Ada is Inochi2D's mascot, an airheaded, friendly and helpful foxgirl. She will appear throughout the documentation with tips, warnings and other tidbits of information that may be useful.

.. admonition:: Hello, there!
   :class: custom

   .. container:: ada-block

      .. image:: img/ada-hi.png
         :class: ada
         :height: 128px
         :align: left
      
      Nice to meet ya! I'm Ada, local vertex engineer fox! Please don't mind me shedding a bit of fur on your experience 🦊

      Oh, and don't forget: If you have questions not covered here you can always reach out to us on `our Discord <https://discord.gg/invite/abnxwN6r9v>`__!


.. toctree::
   :maxdepth: 2
   :caption: Inochi Creator
   :name: sec-creator
   :hidden:

   creator/about
   creator/getting-started
   creator/first-model/index
   creator/nodes/index
   creator/video-export/index
   
.. toctree::
   :maxdepth: 2
   :caption: Inochi Session
   :name: sec-session
   :hidden:

   session/index
   
.. toctree::
   :maxdepth: 2
   :caption: Inochi2D SDK
   :name: sec-i2d
   :hidden:

   i2d/index



.. Indices and tables
.. ------------------
..
.. * :ref:`genindex`
.. * :ref:`modindex`
.. * :ref:`search`