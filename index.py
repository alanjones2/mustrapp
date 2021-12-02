##################################################
# Mustrapp - Multi-app Streamlit Application
#
# Do not change this code except for the message below
# which can be plain text or any markdown code and will
# be displayed above the selection box
#
# individual apps must be in the library folder 'stlib'
# all modules in the library will be imported unless their
# name begins with the _ character
#

message = """
        __Select an application from the list below__
        """

import streamlit as st
st.set_page_config(layout = "wide") # optional

import pkgutil
import importlib
import stlib    # default library name for apps

# Global arrays for holding the app names, modules and descriptions of the apps
names = []
modules = []
descriptions = [] 

package = stlib # default name for the library containg the apps

# Find the apps and import them
for importer, modname, ispkg in pkgutil.iter_modules(package.__path__):
    #print ("Found submodule %s (is a package: %s)" % (modname, ispkg))
    if modname.startswith('_'):
        pass  # ignore any modules beginning with _
    else:
        m = importlib.import_module('.'+modname,'stlib')
        names.append(modname)
        modules.append(m)
        # If the module has a description attribute use that in the select box
        # otherwise use the module name
        try:
            descriptions.append(m.description)
        except:
            descriptions.append(modname)

# The main app starts here

# Define a function to display the app
# descriptions instead of the module names
# in the selctbox, below
def format_func(name):
    return descriptions[names.index(name)]

# Display the sidebar with a menu of apps
with st.sidebar:
    st.markdown(message)
    page = st.selectbox('Select:',names, format_func=format_func) 

# Run the chosen app
modules[names.index(page)].run()
