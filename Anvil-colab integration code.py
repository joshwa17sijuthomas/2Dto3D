from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def image1_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    result = anvil.server.call("save",file,file.name)

  def image3_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    result = anvil.server.call("save",file,file.name)

  def image2_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    result = anvil.server.call("save",file,file.name)

  def image4_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    result = anvil.server.call("save",file,file.name)

  def image5_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    result = anvil.server.call("save",file,file.name)

  def image6_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    result = anvil.server.call("save",file,file.name)

  def image7_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    result = anvil.server.call("save",file,file.name)

  def image8_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    result = anvil.server.call("save",file,file.name)

  def button_click(self, **event_args):
    """This method is called when the button is clicked"""
    out = anvil.server.call("Generator")
    self.message.visible = True
    self.message.text = out
