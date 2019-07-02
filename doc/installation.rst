Installation
============

Step 1: Install a `Miniconda <https://conda.io/miniconda.html>`_  (or `Anaconda <https://www.anaconda.com/downloads>`_) environment
-----------------------------------------------------------------------------------------------------------------------------------

Any Linux, Mac OS X, or Windows computer with a web browser (preferably Google Chrome) should be suitable. 16GB of RAM is required for some of the examples, but most will run fine in 4GB.

If you don't already have conda on your machine, you can get it from `conda.io <https://conda.io/miniconda.html>`_, and then open a terminal window.

If you do have conda already, it's a good idea to update it (running it twice to get the very latest) to ensure you have the latest version::

   > conda update conda
   > conda update conda

You should then create a separate Conda environment to work in for this tutorial::

   > conda create -n holoviz-tutorial python=3.6
   > conda activate holoviz-tutorial

Depending on how your conda is set up, you may need to use "source" instead of "conda" activate, or sometimes just "activate" on Windows.


Step 2: Install ``holoviz`` and other required libraries
------------------------------------------------------

::

   > conda install -c pyviz holoviz


Step 3: Install the tutorials in your current working directory and download data
---------------------------------------------------------------------------------

::

   > holoviz examples

This will (a) create a copy of the notebooks and related files needed for the tutorial in a new subdirectory ``holoviz-examples/tutorial``, and (b) download larger sample datasets such as Earthqukes.

If you only want to get a copy of the examples, or only want to download the data, there are individual commands ``holoviz copy-examples1`` and ``holoviz fetch-data1``; run e.g. ``holoviz copy-examples --help`` for more info.

If you have an old version of the examples and are willing to overwrite it, use::

   > holoviz copy-examples --force


Step 4: Option A: Launch Jupyter Notebook
-----------------------------------------

You can then launch the notebook server and client::

   > cd holoviz-examples
   > jupyter notebook


A browser window with a Jupyter Notebook instance should now open, letting you select and execute each notebook.  You can start with the ones in the ``tutorial`` subdirectory, as these show how to use the others in ``tutorials/exercises``.  The first notebook to load is ``index.ipynb`` in ``tutorial/``, which makes it simple to subsequently load each of the others.

If you don't see the notebook appear (e.g. on some OS X versions), you may need to cut and paste the URL from the console output manually.

Step 4: Option B: Launch JupyterLab
-----------------------------------

We'll be using Jupyter Notebook, but if you prefer to use JupyterLab, you can install it and the extension::

   > conda install jupyterlab
   > jupyter labextension install @pyviz/jupyterlab_pyviz

Then change directory into the examples and launch as usual::

   > cd holoviz-examples
   > jupyter lab

A browser window with a JupyterLab instance should open.

Step 5: Test that everything is working
---------------------------------------

You can see if everything has installed correctly by selecting the ``Setup`` notebook from the index and doing "Cell/Run All" in the menus. There may be warnings on some platforms, but you'll know it is working if you see the orange HoloViews logo after it runs ``hv.extension()``.


Step 6: Run the tutorials
-------------------------
Now you can run through the `tutorials <tutorial/index.html>`_, learn how to use all these tools, and apply them to anything you need to visualize.  Have fun!
