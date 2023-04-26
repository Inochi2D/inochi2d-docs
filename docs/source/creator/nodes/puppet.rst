==========
Puppet
==========

.. image:: img/puppet-content.png

The puppet node is a special node that you can not move. It contains properties for model information, model-wide settings such as physics system options and rendering options.

General Info & Licensing
------------------------

These sections stores general information that most software reading the model will show to the user.

As for licensing, note that unlike competing software, we do not claim any form of license or ownership over the models produced with our software.

As such you are free to specify any license you want and have to enforce said license yourself.

Physics Globals
---------------

This section stores settings related to the physics handling of the model

Pixels per meter
~~~~~~~~~~~~~~~~

How many pixels count as 1 meter in the physics system. You can adjust this value to match the physics to the canon height of the character, or otherwise to your liking.

Gravity
~~~~~~~~~~~~~~~~

How strong the gravity is for the model, by default it uses Earth gravity of 9.8 m/s squared.

Rendering Settings
------------------

This section stores settings related to the rendering of the model.

Use Point Filtering
~~~~~~~~~~~~~~~~~~~

If you're making a pixel art model, this setting will force the rendering to preserve the hard edges of pixels. This will allow you to save texture memory by requiring a lot less scaling of your model.

Competing packages such as Live2D normally requires a ~5000% (50x) scale-up of your model to look good, Inochi2D can get away with 200% (2x) if you turn this option on.
