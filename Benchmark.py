def run_benchmark(language_index, app_title):
    import streamlit as st
    import datetime
    from dateutil.relativedelta import relativedelta
    import plotly.express as px
    import Tickers as tic
    import yfinance as yf
    import Process_Button_Styling
    import Select_Store_Location
    import Centred_Title
    import Background_Style
    import Footer as ft
    Background_Style.run_background_styl()

    # Erstelle eine dicke Linie Funktion
    def draw_line(groesse):
        st.markdown(f"<hr style='border: {groesse}px solid black;'>", unsafe_allow_html=True)

    # Erstelle eine dicke Linie Funktion (Sidebar)
    def draw_line_sidebar(width):
        st.sidebar.markdown(f"<hr style='border: {width}px dashed #009999;'>",
                            unsafe_allow_html=True)

    def make_metric_benchmark(title, value):

        if title == 'Rendite':
            value = value * 100
            value = f'{value:.1f} %'

        else:
            value = f'{value:.2f}'
        st.markdown(
            f"""
            <div style='border: 1px solid black; box-shadow: 0px 0px 25px 3px black; padding: 10px; background-color: #f8f8f8; height: 100%; display: flex; flex-direction: column; justify-content: center;'>
                 <h1 style='text-align: center; background-color:#d5d5d5; margin: 0; padding: 5px; height: 50%;'>{title}</h1>
                <h1 style='text-align: center; background-color:#eeeeee; margin: 0; padding: 5px; height: 50%;'>
                    <span style='color:black; '>
                    <span style='color:black; '> ‎ </span>
                    {value} 
                    </span>
                </h1>
            </div>
            """, unsafe_allow_html=True
        )

        st.write('')
        st.write('')

    @st.cache_data
    def benchmark_load_data(benchmark_asset_type, start_date, end_date, benchmark_selected_ticker, benchmark_selected_index, selected_interval):
        import streamlit as st

        selected_ticker_dummy = benchmark_selected_ticker
        # Aktien
        if benchmark_asset_type == 'Aktien':
            benchmark_selected_ticker = benchmark_selected_ticker
            benchmark_selected_index = benchmark_selected_index
            title = benchmark_selected_ticker

        # Kryptowährungen
        elif benchmark_asset_type == 'Kryptowährungen':
            benchmark_selected_ticker = str(benchmark_selected_ticker).upper() + '-USD'
            benchmark_selected_index = str(benchmark_selected_index).upper() + '-USD'
            title = selected_ticker_dummy + '-USD'

        # Währungen
        elif benchmark_asset_type == 'Währungen':
            benchmark_selected_ticker = str(benchmark_selected_ticker).upper() + 'USD=X'
            benchmark_selected_index = str(benchmark_selected_index).upper() + 'USD=X'
            title = selected_ticker_dummy + ' / USD'

        # Rohstoffe
        elif benchmark_asset_type == 'Rohstoffe':
            benchmark_selected_ticker = str(benchmark_selected_ticker).upper() + '=F'
            benchmark_selected_index = str(benchmark_selected_index).upper() + '=F'
            title = selected_ticker_dummy + ' / USD'

        # Fonds
        elif benchmark_asset_type == 'Fonds':
            benchmark_selected_ticker = str(benchmark_selected_ticker).upper()
            benchmark_selected_index = str(benchmark_selected_index).upper()
            title = selected_ticker_dummy + ' / USD'

        # Lade die Daten des aktuellen Tickers
        data_ticker = yf.download(tickers=benchmark_selected_ticker,
                                  interval=selected_interval,
                                  start=start_date,
                                  end=end_date)

        # Lade die Daten des aktuellen Index
        data_index = yf.download(tickers=benchmark_selected_index,
                                  interval=selected_interval,
                                  start=start_date,
                                  end=end_date)



        # Lösche die Ticker-Level aus den Daten
        data_ticker.columns = data_ticker.columns.droplevel(1)

        # Index Spalte zurücksetzen
        data_ticker = data_ticker.reset_index()

        # Umbennen der Spalte 'Date' zu 'Datetime'
        data_ticker = data_ticker.rename(columns={"Date": "Datetime"})

        # Datetime format anpasse
        data_ticker["Datetime"] = data_ticker["Datetime"].dt.tz_localize(None)

        # Füge eine neue Spalte mit Tickernamen als erste Spalte im DataFrame
        data_ticker.insert(0, 'Ticker', benchmark_selected_ticker)



        ######
        ######
        #####
        #####
        # Lösche die Ticker-Level aus den Daten
        data_index.columns = data_index.columns.droplevel(1)

        # Index Spalte zurücksetzen
        data_index = data_index.reset_index()

        # Umbennen der Spalte 'Date' zu 'Datetime'
        data_index = data_index.rename(columns={"Date": "Datetime"})

        # Datetime format anpasse
        data_index["Datetime"] = data_index["Datetime"].dt.tz_localize(None)

        # Füge eine neue Spalte mit Tickernamen als erste Spalte im DataFrame
        data_index.insert(0, 'Ticker', benchmark_selected_index)




        return data_ticker,data_index,  title

    def create_line_chart_benchmark(data,benchmark_date_from,benchmark_date_to,benchmark_selected_ticker):

        # Gesamte Rendite Berechnen
        opening_price= data['Close'].iloc[0]
        closing_price  = data['Close'].iloc[-1]
        return_on_investment  = (closing_price-opening_price)/opening_price

        return_on_investment_title = return_on_investment * 100
        return_on_investment_title = f'{return_on_investment_title:.1f} %'
        # Tägliche Rendite berechnen
        data['Daily Return'] = data['Close'].pct_change()

        #  Tägliche Rendite berechnen
        data['Cumulative Return'] = (1 + data['Daily Return']).cumprod() - 1





        # Interaktives Liniendiagramm mit Plotly und Streamlit
        fig = px.line(data,
                      x='Datetime',
                      y='Daily Return',
                      title='Tägliche Rendite',
                      )

        # Change the line color
        fig.update_traces(name='Tägliche Rendite')

        # Hintergrund und Layout anpassen
        fig.update_layout(
            plot_bgcolor='#eeeeee',  # Hintergrundfarbe des Plots
            paper_bgcolor='#d5d5d5',  # Hintergrundfarbe der gesamten Figur
            font=dict(color='#009999'),  # Schriftfarbe

            title=dict(
                text=f'Rendite zwischen {benchmark_date_from} und {benchmark_date_to} für {benchmark_selected_ticker} beträgt {return_on_investment_title}',
                # Titeltext
                x=0.5,  # Zentriert den Titel
                xanchor='center',  # Verankert den Titel in der Mitte
                font=dict(size=25)  # Schriftgröße des Titels
            )


        )

        # Achsenfarben anpassen
        fig.update_xaxes(title_font=dict(color='black'), tickfont=dict(color='black'))
        fig.update_yaxes(title_font=dict(color='black'), tickfont=dict(color='black'))



        fig.add_scatter(x=data['Datetime'],
                        y=data['Cumulative Return'],
                        mode='lines',
                        name=f'Kum. Rendite',
                        line=dict(color='#8b0000', width=2))

        # Diagramm in Streamlit anzeigen
        st.plotly_chart(fig, use_container_width=True)

        # Gesamte Rendite Berechnen
        opening_price_col, closing_price_col, return_on_investment_col = st.columns(3)
        with opening_price_col:
            make_metric_benchmark('Anfangskurs',opening_price)


        with closing_price_col:
            make_metric_benchmark('Schlusskurs',closing_price)


        with return_on_investment_col:
            make_metric_benchmark('Rendite',return_on_investment)

    # Logo sidebar
    st.sidebar.image("Images/FinGraph Logo.png",
                     use_column_width=True)

    # Draw Line for the sidebar (3 Pixel)
    draw_line_sidebar(3)

    benchmark_asset_type_col, selected_interval_col = st.sidebar.columns(2)

    with benchmark_asset_type_col:
        benchmark_asset_type_options = ['Aktien', 'Kryptowährungen', 'Währungen', 'Rohstoffe', 'Fonds']
        benchmark_asset_type = st.selectbox(label='Asset-Typ:',
                                                       options=benchmark_asset_type_options)

    with selected_interval_col:
        # Liste der Intervalle für yfinance
        intervals = [

            "1d",  # 1 day
            "5d",  # 5 days
            "1wk",  # 1 week
            "1mo",  # 1 month
            "3mo"  # 3 months
        ]

        # Liste umkehren
        intervals.reverse()

        # Dropdown-Liste in Streamlit zur Auswahl des Intervalls
        selected_interval = st.selectbox("Intervall:",
                                         options=intervals,
                                         index=4
                                         )

    selected_ticker_col, selected_index_col = st.sidebar.columns(2)

    with selected_ticker_col:
        tickers_ticker, big_four_tickers = tic.run_tickers(asset_type=benchmark_asset_type)

        # Einfachauswahl für Ticker
        benchmark_selected_ticker = st.selectbox(
            label="Ticker:",
            options=tickers_ticker
        )

    with selected_index_col:
        tickers_index = tickers_ticker.copy()

        tickers_index.remove(str(benchmark_selected_ticker))

        # Einfachauswahl für Ticker
        benchmark_selected_index = st.selectbox(
            label="Index:",
            options= tickers_index
        )




    benchmark_date_from_col, benchmark_date_to_col = st.sidebar.columns(2)

    today = datetime.datetime.today().date()

    benchmark_today_minus_two_years = today - relativedelta(years=2)
    benchmark_today_minus_twenty_years = today - relativedelta(years=20)
    with benchmark_date_from_col:
        benchmark_date_from = st.date_input(label='Von-Datum:',
                                               min_value=benchmark_today_minus_twenty_years,
                                               value=benchmark_today_minus_two_years,
                                               key='benchmark_date_from')

    benchmark_date_from_plus_one_month = benchmark_date_from + relativedelta(months=1)

    with benchmark_date_to_col:
        benchmark_date_to = st.date_input(label='Bis-Datum:',
                                             value=today,
                                             min_value=benchmark_date_from_plus_one_month,
                                             max_value=today,
                                             key='benchmark_date_to')






    # Page Title
    Centred_Title.run_centred_title(app_title)

    # Daten abrufen aus yfinance
    ticker_data, index_data, title = benchmark_load_data(
        benchmark_asset_type=benchmark_asset_type,
        start_date=benchmark_date_from,
        end_date=benchmark_date_to,
        benchmark_selected_ticker=benchmark_selected_ticker,
        benchmark_selected_index=benchmark_selected_index,
        selected_interval=selected_interval
    )





    ## Rendite Line Chart
    create_line_chart_benchmark(ticker_data,
                                benchmark_date_from,
                                benchmark_date_to,
                                benchmark_selected_ticker
                                )

    # Eine horizontale zwei Pixel Linie hinzufügen
    draw_line(2)

    ## Rendite Line Chart
    create_line_chart_benchmark(index_data,
                                benchmark_date_from,
                                benchmark_date_to,
                                benchmark_selected_index
                                )

    # Eine horizontale zwei Pixel Linie hinzufügen
    draw_line(2)

    store_location_path = Select_Store_Location.run_select_store_location(language_index=language_index)

    # Eine horizontale drei Pixel Linie hinzufügen
    draw_line(3)
    # Daten speichern
    process_button_dummy_one, process_button, process_button_dummy_two = st.columns([1.5, 1, 1.5])
    with process_button_dummy_one:
        pass
    with process_button:
        Process_Button_Styling.run_process_button_style()
        if st.button("Daten lokal speichern"):
            if len(store_location_path) > 0:
                store_columns = ['Datetime', 'Close', 'Daily Return','Cumulative Return']
                ticker_data = ticker_data[store_columns]
                ticker_data.insert(0, 'Ticker', title)
                ticker_data.to_excel(rf'{store_location_path}/Ticker Data.xlsx',
                                           sheet_name='Ticker Data',
                                           index=False)

                index_data = index_data[store_columns]
                index_data.insert(0, 'Ticker', title)
                index_data.to_excel(rf'{store_location_path}/Index Data.xlsx',
                                     sheet_name='Index Data',
                                     index=False)

                st.success('Alles geklappt')
            else:
                st.warning(
                    # "Please complete your details and check them for accuracy"
                    f'Bitte vervollständigen')
    with process_button_dummy_two:
        pass

    # Footer importieren
    ft.run_footer(language_index=language_index)

