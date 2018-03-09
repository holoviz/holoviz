Installation
============

Step 1: Install a `Miniconda <http://conda.pydata.org/miniconda.html>`_  (or `Anaconda <https://www.continuum.io/downloads>`_) environment
------------------------------------------------------------------------------------------------------------------------------------------

Any Linux, Mac OS X, or Windows computer with a web browser (preferably Google Chrome) should be suitable. 16GB of RAM is required for some of the examples, but most will run fine in 4GB.

If you don't already have conda on your machine, you can get it from `Anaconda.com <http://conda.pydata.org/miniconda.html>`_, and then open a terminal window.

If you do have conda already, it's a good idea to update it (running it twice to get the very latest) to ensure you have the latest version::

   > conda update conda
   > conda update conda

[OPTIONAL] If you want to keep things organized, you can then create a separate Conda environment to work in for this tutorial::

   > conda create -n pyviz-tutorial python=3.6
   > source activate pyviz-tutorial

(omitting "source" if you are on Windows).


Step 2: Install ``pyviz`` and other required libraries
----------------------------------------------------

::

   > conda install -c pyviz pyviz


Step 3: Install the tutorials in your home directory
----------------------------------------------------

::

   > pyviz --install-examples pyviz-tutorial
   > cd pyviz-tutorial

This will create a copy of the notebooks and related files needed for the tutorial in a new subdirectory ``pyviz-tutorial/``.


Step 4: Download the sample data
--------------------------------

::

   > pyviz --download-sample-data

(Small datasets come with the examples, but large ones like the NYC Taxi dataset have to be downloaded separately, which can take some time.)

Step 5: Launch Jupyter Notebook
-------------------------------

You can then launch the notebook server and client::

   > jupyter notebook

A browser window with a Jupyter Notebook instance should now open, letting you select and execute each notebook.  You can start with the ones in the "notebooks" subdirectory, as these show how to use the others in the "exercises" directory along with the applications in the "apps" directory. 

If you don't see the notebook appear (e.g. on some OS X versions), you may need to cut and paste the URL from the console output manually. 


Step 6: Test that everything is working
---------------------------------------

You can see if everything has installed correctly by selecting the ``00_Welcome.ipynb`` notebook and doing "Cell/Run All" in the menus. There may be warnings on some platforms, but you'll know it is working if you see the orange HoloViews logo after it runs ``hv.extension()``. 

Step 7: Run the tutorials
-------------------------
Now you can run through the `tutorials <tutorial/index.html>`_, learn how to use all these tools, and apply them to anything you need to visualize.  Have fun!
