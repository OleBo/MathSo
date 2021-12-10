from bokeh.io import output_notebook
from bokeh.io import show
from bokeh.layouts import column
from bokeh.models import ColumnDataSource, Slider
from bokeh.plotting import figure
from bokeh.sampledata.sea_surface_temperature import sea_surface_temperature

from pywebio import start_server
from pywebio.output import *
from pywebio.session import info as session_info


def bkapp(doc):
    df = sea_surface_temperature.copy()
    source = ColumnDataSource(data=df)

    plot = figure(x_axis_type='datetime', y_range=(0, 25),
                  y_axis_label='Temperature (Celsius)',
                  title="Sea Surface Temperature at 43.18, -70.43")
    plot.line('time', 'temperature', source=source)

    def callback(attr, old, new):
        if new == 0:
            data = df
        else:
            data = df.rolling('{0}D'.format(new)).mean()
        source.data = ColumnDataSource.from_df(data)

    slider = Slider(start=0, end=30, value=0, step=1, title="Smoothing by N Days")
    slider.on_change('value', callback)

    doc.add_root(column([slider, plot], sizing_mode='stretch_width'))


def bk_app():
    output_notebook(verbose=False, notebook_type='pywebio')

    put_markdown("""# Bokeh Applications in PyWebIO
    [Bokeh Applications](https://docs.bokeh.org/en/latest/docs/user_guide/server.html) can be built by starting the Bokeh server. The purpose of the Bokeh server is to make it easy for Python users to create interactive web applications that can connect front-end UI events to real, running Python code.
    In PyWebIO, you can also use bokeh.io.show() to display a Bokeh App.
    You can use `bokeh.io.output_notebook(notebook_type='pywebio')` in the PyWebIO session to setup Bokeh environment. Then you can use `bokeh.io.show()` to output a boken application.
    This is a demo of Bokeh App: 
    """)

    show(bkapp)


if __name__ == '__main__':
    start_server(bk_app, port=8080, debug=True)