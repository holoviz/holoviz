*****
PyViz
*****

**How to solve visualization problems with Python tools**


The PyViz website and corresponding GitHub repository provide
examples, demos, and training materials documenting how to solve
visualization problems using web-based Python tools supported by
`Anaconda <http://anaconda.com>`_, including `Bokeh
<http://bokeh.pydata.org>`_, `HoloViews <http://holoviews.org>`_,
`GeoViews <http://geo.holoviews.org>`_, `Datashader
<https://github.com/bokeh/datashader>`_, and `Param
<https://github.com/ioam/param>`_.

You can view the `Tutorial <tutorial/index>`_ online, or you can work
through it interactively yourself. The repository includes a shared
conda environment that ensures all these tools work together,
facilities for downloading sample data for use with these tools, and
provides starting points for solving your own visualization problems.


Installation
============

Step 1: Clone the `pyviz <https://github.com/pyviz/pyviz/blob/master/README.rst>`_ repository
-----------------------------------------------------------------

- Any Linux, Mac OS X, or Windows computer with a web browser should work.  We recommend Chrome, but other browsers should also work.
- 16GB of RAM is required for some of the examples, but most will run fine in 4GB.
- Clone this repository, e.g. using ``git clone https://github.com/pyviz/pyviz.git``
- Open a terminal window inside your clone of the repository.

Step 2: Create a conda environment from ``environment.yml``
-----------------------------------------------------------

If you don't already have it, install `conda
<https://www.continuum.io/downloads>`_, and then create the
``pyviz`` environment by executing::

   > conda env create --force -f environment.yml

When installation is complete you may activate the environment by writing::

   > activate pyviz

(for Windows) or::

   $ source activate pyviz

(for Linux and Mac). 

Later, when you are ready to exit the environment after the tutorial, you can type::

   > deactivate

If for some reason you want to remove the environment entirely, you can do so by writing::

   > conda env remove --name pyviz


Step 3: Downloading the sample data
---------------------------

In this tutorial we will be showing you how to work with some fairly
large datasets.  Unfortunately, that also means that you have to
download this data. To make this as easy as possible we have provided
a script that will download the data for you.  Simply execute in the
root of your clone of this repository::

  > python download_sample_data.py


Step 4: Launch Jupyter Notebook
-------------------------------

You can then launch the notebook server and client::

   (pyviz)> jupyter notebook

A browser window with a Jupyter Notebook instance should now open,
letting you select and execute each notebook.  You can start with the
ones in the "notebooks" subdirectory, as these show how to use the
others in the "exercises" directory along with the applications in the
"apps" directory.

If you don't see the notebook appear (e.g. on some OS X versions),
you'll need to cut and paste the URL from the console output manually.


Step 5: Test that everything is working
---------------------------------------

You can see if everything has installed correctly by selecting the
``00_Welcome.ipynb`` notebook and doing "Cell/Run All" in the menus.
There may be warnings on some platforms, but you'll know it is working
if you see the HoloViews logo after it runs ``hv.extension()``.



.. toctree::
   :hidden:
   :maxdepth: 2

   Introduction <self>
   Tutorial <tutorial/index>
   FAQ
   About <about>
