This python application provides an interface for generating a static image gallery in HTML.

It requires: PySide, Pillow, Moments, and Mako.

cxfreeze has been used for packaging as a stand alone executable.


Templates used to generate the static files are stored in the "templates" directory.  These can be customized to change the generated output.

The "static" directory contains files that should be transferred to the root of your web server for serving.  LESS can be used to generate the main CSS file: style.css:

lessc less/style.less > css/style.css 



After the script is working on a given machine (meaning you have installed all dependencies / requirements), you can package the application as a stand alone application so that others do not need to install all of those requirements separately.  This is done with cxfreeze with the following command:

cxfreeze generate.py --target-dir output --base-name Win32GUI --include-modules atexit

Copy over the templates and static directories to the output folder.

cd /c/shared/site_generator/
cp -r static output/static
cp -r templates output/templates
mv output site_generator
#make zip file of it.

There is a chance the target machine may need extra files to work:
http://cx_freeze.readthedocs.org/en/latest/overview.html

Get your users to install the Microsoft Visual C++ 2008 Redistributable Package (free download, for x86 (32 bit) Windows or for x64 (64 bit) Windows). It’s not uncommon for this to already be present on modern computers, but it’s not (as far as we know) part of a standard Windows installation. Note that the “SP1” version of this does not work – it has to exactly match the version which Python itself is compiled with.

32bit Windows:
http://www.microsoft.com/download/en/details.aspx?displaylang=en&id=29

64bit Windows:
http://www.microsoft.com/download/en/details.aspx?displaylang=en&id=15336



*2013.05.24 09:52:57 
after generating the static content, transfer it to your site as you normally would
