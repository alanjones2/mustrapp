# Mustrapp

A downloadable template for creating multiple Streamlit apps on the same web site.

The template is structured like this:


    /home
    |
    |-- index.py
    |
    |-- /stlib
        |
        |-- __init__.py
        |
        |-- app1.py
        |
        |-- app2.py

In the home directory the index.py is where it all starts. So, to run the multiple app you do this:

    streamlit run index.py

This will run a Streamlit app with a drop down menu in the sidebar which will contain the list of apps that can be run (in this skeleton template, _app1_ and _app2_).

```index.py``` does not need to be changed except to change the the variable ```message``` if you wish to.

Apps are stored in the ```stlib``` folder and have to adopt a simple structure. They should look like this:

description = "Example app 1"

    # Your app goes in the function run()
    def run():
            
        import streamlit as st

        st.header("Example app 1")
        st.write("Insert your own Streamlit code here")

    # end of app

    # This code allows you to run the app standalone
    # as well as part of a library of apps
    if __name__ == "__main__":
        run()

Essentially the app is contained in the function ```run()``` and has an optional ```description``` which will be displayed as an entry in the main drop down menu. If no description is given, the menu entry will be the name of the module.

That's about it.

If you use Git you can clone this app, if not download the zip file from the code page.

See the LICENCE for details of use.

---

If you find this content useful, please consider this... <br/><br/>
<a href='https://ko-fi.com/M4M64THKG' target='_blank'><img height='36' style='border:0px;height:36px;' src='https://cdn.ko-fi.com/cdn/kofi2.png?v=2' border='0' alt='Buy Me a Coffee at ko-fi.com' /></a>