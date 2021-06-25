Installation
============

Step 1: Install a `Miniconda <https://conda.io/miniconda.html>`_  (or `Anaconda <https://www.anaconda.com/downloads>`_) environment
-----------------------------------------------------------------------------------------------------------------------------------

Any Linux, Mac OS X, or Windows computer with a web browser (preferably
Google Chrome) should be suitable. 16GB of RAM is required for some of
the examples, but most will run fine in 4GB.

If you don't already have conda on your machine, you can get it from
`conda.io <https://conda.io/miniconda.html>`_, and then open a terminal
window.

If you do have conda already, it's a good idea to update it (running it
twice to get the very latest) to ensure you have the latest version::

   > conda update conda
   > conda update conda

You should then make sure you have `anaconda-project` installed after
activating your chosen conda environment:

::

   > conda install anaconda-project


Step 2: Download and extract the tutorial project
-------------------------------------------------

The following steps will fetch and extract the latest version of the
tutorial project. *SciPy 2021 tutorial attendees should make sure to run
these steps the day before the tutorial to ensure they have the latest
version of the project.*

::

   > anaconda-project download pyviz/holoviz_tutorial

If you have already run this command in the current directory, you may
need to remove the existing `holoviz_tutorial` directory before the
command above will execute. Once the download is completed, change to
the tutorial directory with:

::

     > cd holoviz_tutorial


Step 3: Option A: Launch Jupyter Notebook
-----------------------------------------

You can then launch the classic Jupyter notebook server and client::

   > anaconda-project run


A browser window with a Jupyter Notebook instance should now open,
letting you navigate through subdirectories and select a notebook to work on.
In this case, look in the  ``tutorial`` subdirectory, and load ``index.ipynb``, which will let you launch each of the tutorials and exercises.

If you don't see the notebook appear as a new browser tab automatically, you 
may need to cut and paste the URL from the console output manually.

Step 3: Option B: Launch JupyterLab
-----------------------------------

If you prefer to use JupyterLab rather than classic (single-page) Jupyter, you can use the following command instead::

   > anaconda-project run jupyter lab

A browser window with a JupyterLab instance should open.

Step 4: Download data files and test that everything is working
---------------------------------------------------------------


You can see if everything has installed correctly by selecting the
``Setup`` notebook from the index and doing "Cell/Run All" in the
menus. There may be warnings on some platforms, but you'll know it is
working if you see the orange HoloViews logo after it runs
``hv.extension()``.

Running this notebook will also download the data files needed by the
tutorial.


Step 5: Run the tutorials
-------------------------

Now you can run through the `tutorials <tutorial/index.html>`_, learn
how to use all these tools, and apply them to anything you need to
visualize.  Have fun!
