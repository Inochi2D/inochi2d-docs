=================
Installing FFMPEG
=================


Installing FFMPEG on Windows
----------------------------

Currently you'll need to manually install ffmpeg on your system on Windows, we plan to support an automatic installer within Inochi Creator eventually.

1. Go to http://ffmpeg.org/download.html, and find the Windows packages.
2. Follow the instructions on the page you are redirected to
3. Once you have the ZIP archive find the bin/ folder within it.
4. Put ffmpeg.exe next to inochi-creator.exe.


Installing FFMPEG on Linux
--------------------------

Download FFMPEG from your system's package manager, on Ubuntu and Debian based systems the following command will install ffmpeg

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