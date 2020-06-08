from flask import Flask, render_template

app=Flask(__name__)

@app.route('/google/')
def google():
    from pandas_datareader import data
    import datetime
    from bokeh.plotting import figure, show, output_file
    from bokeh.embed import components
    from bokeh.resources import CDN

    start=datetime.datetime(2020,1,1)
    end=datetime.datetime(2020,5,10)

    df = data.DataReader(name="GOOG",data_source="yahoo",start=start,end=end)

    def inc_dec(c,o):
        if c > o:
            value="Increase"
        elif c < o:
            value="Decrease"
        else:
            value="Equal"
        return value

    df["Status"] = [inc_dec(c,o) for c, o in zip(df.Close,df.Open)]
    df

    df["Middle"] = (df.Open+df.Close)/2
    df

    df["Height"] = abs(df.Close-df.Open)
    df

    p=figure(x_axis_type='datetime', width=1000, height=300, sizing_mode="scale_width")
    p.title.text = "Candlestick Chart"
    p.grid.grid_line_alpha = 0.3

    hours_12 = 12*60*60*1000

    # To add vertical lines we use segment method
    p.segment(df.index, df.High, df.index, df.Low, color="Black")

    p.rect(df.index[df.Status=="Increase"], df.Middle[df.Status=="Increase"], hours_12, df.Height[df.Status=="Increase"], fill_color="green",line_color="black")

    p.rect(df.index[df.Status=="Decrease"], df.Middle[df.Status=="Decrease"], hours_12, df.Height[df.Status=="Decrease"], fill_color="red",line_color="black")


    script1, div1 = components(p)
    cdn_js = CDN.js_files[0]

    return render_template("google.html",
    script1=script1,
    div1=div1,
    cdn_js=cdn_js )



@app.route('/')
def apple():
    from pandas_datareader import data
    import datetime
    from bokeh.plotting import figure, show, output_file
    from bokeh.embed import components
    from bokeh.resources import CDN

    start=datetime.datetime(2020,1,1)
    end=datetime.datetime(2020,5,10)

    df = data.DataReader(name="AAPL",data_source="yahoo",start=start,end=end)

    def inc_dec(c,o):
        if c > o:
            value="Increase"
        elif c < o:
            value="Decrease"
        else:
            value="Equal"
        return value

    df["Status"] = [inc_dec(c,o) for c, o in zip(df.Close,df.Open)]
    df

    df["Middle"] = (df.Open+df.Close)/2
    df

    df["Height"] = abs(df.Close-df.Open)
    df

    p=figure(x_axis_type='datetime', width=1000, height=300, sizing_mode="scale_width")
    p.title.text = "Candlestick Chart"
    p.grid.grid_line_alpha = 0.3

    hours_12 = 12*60*60*1000

    # To add vertical lines we use segment method
    p.segment(df.index, df.High, df.index, df.Low, color="Black")

    p.rect(df.index[df.Status=="Increase"], df.Middle[df.Status=="Increase"], hours_12, df.Height[df.Status=="Increase"], fill_color="green",line_color="black")

    p.rect(df.index[df.Status=="Decrease"], df.Middle[df.Status=="Decrease"], hours_12, df.Height[df.Status=="Decrease"], fill_color="red",line_color="black")


    script1, div1 = components(p)
    cdn_js = CDN.js_files[0]

    return render_template("apple.html",
    script1=script1,
    div1=div1,
    cdn_js=cdn_js )

@app.route('/coca_cola/')
def coca_cola():
    from pandas_datareader import data
    import datetime
    from bokeh.plotting import figure, show, output_file
    from bokeh.embed import components
    from bokeh.resources import CDN

    start=datetime.datetime(2020,1,1)
    end=datetime.datetime(2020,5,10)

    df = data.DataReader(name="KO",data_source="yahoo",start=start,end=end)

    def inc_dec(c,o):
        if c > o:
            value="Increase"
        elif c < o:
            value="Decrease"
        else:
            value="Equal"
        return value

    df["Status"] = [inc_dec(c,o) for c, o in zip(df.Close,df.Open)]
    df

    df["Middle"] = (df.Open+df.Close)/2
    df

    df["Height"] = abs(df.Close-df.Open)
    df

    p=figure(x_axis_type='datetime', width=1000, height=300, sizing_mode="scale_width")
    p.title.text = "Candlestick Chart"
    p.grid.grid_line_alpha = 0.3

    hours_12 = 12*60*60*1000

    # To add vertical lines we use segment method
    p.segment(df.index, df.High, df.index, df.Low, color="Black")

    p.rect(df.index[df.Status=="Increase"], df.Middle[df.Status=="Increase"], hours_12, df.Height[df.Status=="Increase"], fill_color="green",line_color="black")

    p.rect(df.index[df.Status=="Decrease"], df.Middle[df.Status=="Decrease"], hours_12, df.Height[df.Status=="Decrease"], fill_color="red",line_color="black")


    script1, div1 = components(p)
    cdn_js = CDN.js_files[0]

    return render_template("coca_Cola.html",
    script1=script1,
    div1=div1,
    cdn_js=cdn_js )

if __name__=="__main__":
    app.run(debug=True)
