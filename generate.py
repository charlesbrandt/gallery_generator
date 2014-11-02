#!/usr/bin/env python
"""
#
# By: Charles Brandt [code at charlesbrandt dot com]
# On: *2013.05.22 20:52:50 
# License: MIT 

# Requires:
# PySide, Pillow, Moments, Mako
# cxfreeze for packaging as a stand alone executable

# Description:
#
# interface for generating a static image gallery in HTML

"""

import os, codecs, re, shutil

from moments.path import Path

from mako.template import Template
from mako.lookup import TemplateLookup

from PySide import QtCore, QtGui
    
class Generator(QtGui.QWidget):
    """
    """
 
    def __init__(self):
        """Constructor"""
        super(Generator, self).__init__()
 
        grid = QtGui.QGridLayout()
        grid.setSpacing(10)        

        #http://www.blog.pythonlibrary.org/2013/04/16/pyside-standard-dialogs-and-message-boxes/
        dirDialogBtn =  QtGui.QPushButton("Choose Directory")
        dirDialogBtn.clicked.connect(self.openDirectoryDialog)
        grid.addWidget(dirDialogBtn, 2, 0)

        self.cur_dir = QtGui.QLabel("")
        grid.addWidget(self.cur_dir, 2, 1)

        siteLabel = QtGui.QLabel("Site Name:")        
        grid.addWidget(siteLabel, 3, 0)
        self.siteEdit = QtGui.QLineEdit()
        grid.addWidget(self.siteEdit, 3, 1)

        titleLabel = QtGui.QLabel("Page Title:")        
        grid.addWidget(titleLabel, 4, 0)
        self.titleEdit = QtGui.QLineEdit()
        grid.addWidget(self.titleEdit, 4, 1)
         
        self.status = QtGui.QLabel("")
        grid.addWidget(self.status, 5, 0, 1, 2)

        generate = QtGui.QPushButton('Generate', self)
        generate.clicked.connect(self.make_page)
        grid.addWidget(generate, 6, 1)
        
        self.setLayout(grid)
 
        self.setWindowTitle("Static Gallery Generator")

 
    def openDirectoryDialog(self):
        """
        Opens a dialog to allow user to choose a directory
        """
        flags = QtGui.QFileDialog.DontResolveSymlinks | QtGui.QFileDialog.ShowDirsOnly
        d = directory = QtGui.QFileDialog.getExistingDirectory(self, "Open Directory", os.getcwd(), flags)
        self.cur_dir.setText(d)


    def make_page(self):
        #print "Making Page here!!!!"

        button = self.sender()
        if isinstance(button, QtGui.QPushButton):
            #self.status.setText("You pressed %s!" % button.text())
            pass

        #print source directory:
        #print self.cur_dir.text()
        root = self.cur_dir.text()
        
        #print title:
        #print self.titleEdit.text()
        site_name = self.siteEdit.text()
        page_title = self.titleEdit.text()

        #get current working directory
        #print os.getcwd()
        #this will help locate templates
        
        #check if page / thumbs have already been generated
        index = os.path.join(root, "index.html")
        if os.path.exists(index):
            #prompt "are you sure" if so
            response = QtGui.QMessageBox.question(self, 'Warning:',
                "Generated files already exist. \n\n Are you sure you want to delete and regenerate them?", QtGui.QMessageBox.Yes | 
                QtGui.QMessageBox.No, QtGui.QMessageBox.No)

            if response == QtGui.QMessageBox.Yes:
                #if existing and ok, remove existing
                print "Removing index file: %s" % index
                #shutil.rmtree(output_dir)
                os.remove(index)

                #once deleted, call this:
                self.generate_page(root, page_title, site_name)
            else:
                pass
        else:
            #ok to generate here without deleting first:
            self.generate_page(root, page_title, site_name)
            
    def generate_page(self, root, page_title, site_name="cbrandt.com"):
        #this is needed on windows to make relative_path work:
        #root = root + '\\'
        root = root + os.sep

        base_dir = os.getcwd()
        template_dir = os.path.join(base_dir, 'templates')
        #content_dir = os.path.join(base_dir, 'content')
        #output_dir = os.path.join(base_dir, 'output')

        #print "Creating thumbs dir:"
        #os.mkdir(output_dir)

        mylookup = TemplateLookup(directories=[template_dir], output_encoding='utf-8', encoding_errors='replace')

        image_template = mylookup.get_template("image.mako")
        images_template = mylookup.get_template("image_list.mako")
        mytemplate = mylookup.get_template("site.mako")

        root_path = Path(root)
        root_dir = root_path.load()

        rotate = False

        if rotate:
            root_dir.auto_rotate_images(update_thumbs=False)        

        print "generating thumbs for directory: %s" % root_dir.path

        #this does everything at once,
        #but it prevents keeping the interface updated (looks stalled)
        #root_dir.make_thumbs()

        #scan for all images
        root_dir.scan_filetypes()

        images = []
        if len(root_dir.images):
            for i in root_dir.images:
                #keep Interface happy
                self.status.setText("Processing: %s" % i.name)
                QtCore.QCoreApplication.processEvents()
                #generate thumbnails
                i.load().make_thumbs(['large', 'small', 'tiny'])

        self.status.setText("Thumbnails created.")


        #generate various pages as needed for images
        images_p = []
        for i in root_dir.images:
            #print "loading: %s" % i
            img_path = Path(i, relative_prefix=root)
            relative_img = img_path.load()
            images_p.append(relative_img)
            #print str(relative_img)


        #print "found %s images to use for image pages" % len(images_p)

        count = 0
        prev = []
        #number of items to look forward and backward:
        extend = 3
        for i in images_p:
            #generate individual image page
            if count > extend:
                prev_i = images_p[count-extend:count]
            elif count == 0:
                prev_i = []
            else:
                prev_i = images_p[:count]

            if count+2+extend < len(images_p) :
                next_i = images_p[count+1:count+1+extend]
            elif count+2 > len(images_p):
                next_i = []
            else:
                next_i = images_p[count+1:]

            if count == 0:
                p = None
            else:
                p = images_p[count-1]

            if count == len(images_p) - 1:
                n = None
            else:
                n = images_p[count+1]

            #print "i: %s, nexts: %s, prevs: %s, p: %s, n: %s" % (i, next_i, prev_i, p, n)
            #print i.dimensions()

            (w, h) = i.size_path('large', square=False).load().dimensions()
            half = w / 2
            
            page = image_template.render(
                image=i, nexts=next_i, prevs=prev_i, p=p, n=n, size=half)
                #album=root_path.to_relative(), p=p, n=n)
            item_out = os.path.join(root, i.path.name+".html")
            #print "Saving page to: %s" % item_out
            f = codecs.open(item_out, 'w', encoding='utf8')
            title = "%s : %s" % (page_title, i.time())
            f.write(mytemplate.render(body=page, title=title, site=site_name))
            f.close()

            count += 1

        #print "Saving index.html"
        #generate index list
        index = images_template.render(images=images_p, title=page_title, site=site_name)
        #print index
        item_out = os.path.join(root, "index.html")
        #print "creating: %s" % item_out
        f = codecs.open(item_out, 'w', encoding='utf8')
        f.write(mytemplate.render(body=index, title=page_title, site=site_name))
        f.close()

        self.status.setText("All done generating!")

                   
if __name__ == "__main__":
    app = QtGui.QApplication([])
    form = Generator()
    form.show()
    app.exec_()
