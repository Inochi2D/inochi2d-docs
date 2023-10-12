=================
Installing FFMPEG
=================


Installing FFMPEG on Windows
----------------------------

Currently you'll need to manually install ffmpeg on your system on Windows, we plan to support an automatic installer within Inochi Creator eventually.

Manual local installation
~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Go to http://ffmpeg.org/download.html, and find the Windows packages.
2. Follow the instructions on the page you are redirected to
3. Once you have the ZIP archive find the bin/ folder within it.
4. Put ffmpeg.exe next to inochi-creator.exe.

System-wide with Chocolatey
~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you have `Chocolatey <https://docs.chocolatey.org/en-us/choco/setup>`__ installed you can install ffmpeg system wide with it.

.. code-block:: 
    :linenos:
    
    choco install ffmpeg 

Installing FFMPEG on Linux
--------------------------

FFMPEG should work out of the box on the Flatpak. If not, run the following command:

.. code-block::
    :lineos:
    
    `flatpak install flathub org.freedesktop.Platform.ffmpeg-full
    
Install the latest two branches. as of May 2 2023, this is 21.08 and 22.08.

For zipped builds, download FFMPEG from your system's package manager, on Ubuntu and Debian based systems the following command will install ffmpeg

.. code-block:: 
    :linenos:

    sudo apt install ffmpeg

Installing FFMPEG on macOS
--------------------------
FFMPEG can be installed on macOS through homebrew, which you can install here https://brew.sh/

Once brew is setup you can run the following command to install ffmpeg to your system.

.. code-block:: 
    :linenos:

    brew install ffmpeg
