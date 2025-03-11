# Wichtiger Hinweis:
# Die Tickers wurden durch ChatGpt generiert
def run_tickers(asset_type):
    # Liste der Tickers
    tickers = []
    big_four_tickers = []

    # Aktien
    if asset_type == 'Aktien':
        import pandas as pd
        url_26P_500_companies = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
        table_url_26P_500_companies = pd.read_html(url_26P_500_companies)
        tickers = table_url_26P_500_companies[0]["Symbol"].tolist()
        big_four_tickers = ['AAPL','MSFT','AMZN','GOOGL']

    # Kryptowährungen
    elif asset_type == 'Kryptowährungen':
        tickers = [
            "BTC",  # Bitcoin
            "ETH",  # Ethereum
            "BNB",  # Binance Coin
            "XRP",  # Ripple
            "USDT",  # Tether (Stablecoin)
            "USDC",  # USD Coin (Stablecoin)
            "ADA",  # Cardano
            "DOGE",  # Dogecoin
            "SOL",  # Solana
            "TRX",  # TRON
            "DOT",  # Polkadot
            "MATIC",  # Polygon
            "LTC",  # Litecoin
            "AVAX",  # Avalanche
            "SHIB",  # Shiba Inu
            "WBTC",  # Wrapped Bitcoin
            "DAI",  # Dai (Stablecoin)
            "UNI",  # Uniswap
            "ATOM",  # Cosmos
            "LINK",  # Chainlink
            "ETC",  # Ethereum Classic
            "XMR",  # Monero
            "ALGO",  # Algorand
            "BCH",  # Bitcoin Cash
            "ICP",  # Internet Computer
            "APT",  # Aptos
            "QNT",  # Quant
            "ARB",  # Arbitrum
            "VET",  # VeChain
            "FIL",  # Filecoin
            "EOS",  # EOS.IO
            "AAVE",  # Aave
            "STX",  # Stacks
            "NEAR",  # Near Protocol
            "FTM",  # Fantom
            "XLM",  # Stellar
            "GRT",  # The Graph
            "CRV",  # Curve DAO Token
            "MKR",  # Maker
            "SAND",  # The Sandbox
            "AXS",  # Axie Infinity
            "IMX",  # Immutable X
            "RUNE",  # THORChain
            "LDO",  # Lido DAO
            "CHZ",  # Chiliz
            "GALA",  # Gala
            "KSM",  # Kusama
            "EGLD",  # MultiversX (ehemals Elrond)
            "ZIL",  # Zilliqa
            "ENJ",  # Enjin Coin
            "BAT",  # Basic Attention Token
            "CAKE",  # PancakeSwap
        ]
        big_four_tickers = [ "BTC",  # Bitcoin
            "ETH",  # Ethereum
            "BNB",  # Binance Coin
            "XRP"  # Ripple
         ]

    # Währungen
    elif asset_type == 'Währungen':
        tickers = [
            'EUR', 'AFN', 'ALL', 'AMD', 'AOA', 'ARS', 'AWG', 'AZN', 'BAM',
            'BBD', 'BDT', 'BMD', 'BND', 'BOB', 'BRL', 'BSD', 'BTN', 'BWP', 'BYN',
            'BZD', 'CAD', 'CDF', 'CHF', 'CLP', 'CNY', 'COP', 'CRC', 'CUP', 'CVE',
            'CZK', 'DJF', 'DKK', 'DOP', 'DZD', 'EGP', 'ERN', 'ETB', 'FJD', 'FKP',
            'GBP', 'GEL', 'GHS', 'GIP', 'GMD', 'GNF', 'GTQ', 'GYD', 'HKD', 'HNL',
            'HRK', 'HTG', 'HUF', 'IDR', 'ILS', 'IMP', 'INR', 'IQD', 'IRR', 'ISK',
            'JMD', 'JOD', 'JPY', 'KES', 'KGS', 'KHR', 'KMF', 'KRW', 'KWD', 'KYD',
            'KZT', 'LAK', 'LBP', 'LKR', 'LRD', 'LSL', 'LTL', 'LVL', 'LYD', 'MAD',
            'MDL', 'MGA', 'MKD', 'MMK', 'MNT', 'MOP', 'MUR', 'MVR', 'MWK', 'MXN',
            'MYR', 'MZN', 'NAD', 'NGN', 'NIO', 'NOK', 'NPR', 'NZD', 'OMR', 'PAB',
            'PEN', 'PGK', 'PHP', 'PKR', 'PLN', 'PRB', 'PYG', 'QAR', 'RON', 'RSD',
            'RUB', 'RWF', 'SAR', 'SBD', 'SCR', 'SDG', 'SEK', 'SGD', 'SHP', 'SLL',
            'SOS', 'SRD', 'SSP', 'STN', 'SYP', 'SZL', 'THB', 'TJS', 'TMT', 'TND',
            'TOP', 'TRY', 'TTD', 'TWD', 'TZS', 'UAH', 'UGX', 'UYU', 'UZS', 'VEF',
            'VND', 'VUV', 'WST', 'XAF', 'XCD', 'XOF', 'XPF', 'YER', 'ZAR'
        ]
        big_four_tickers = ['EUR', 'AFN', 'ALL', 'AMD']



    # Rohstoffe
    elif asset_type == 'Rohstoffe':
        tickers = [
            "GC", "SI", "CL", "NG", "PL", "HG", "ZC", "ZS", "ZM", "ZW",
            "KC", "CT", "LB", "CC", "OJ", "SB", "LBS", "PA", "LE", "HE",
            "BO", "SM", "RR", "NR", "DX", "ED", "FF", "FV", "TU", "TY",
            "US", "RX", "FB", "DX", "A1", "CO", "B0", "QS", "QC", "RB",
            "HO", "PG", "QC", "AL", "ZN", "PB", "AU", "AG", "CU", "NI",
            "SN", "SR", "CF", "RM", "MA", "TA", "ZC", "FG", "T", "TF",
            "JD", "AP", "CJ", "UR", "EG", "SA", "PK", "WH", "PM", "RI",
            "LR", "SM", "SF", "IC", "IH", "IF", "IM", "AU", "AG", "SP",
            "NR", "WT", "WS", "EX", "FX", "GX", "QG", "YM", "ES", "NQ",
            "HG", "CT", "GF", "HO", "HU", "LB", "MG", "PB", "RB", "RU",
            "LE", "MW", "OE", "PA", "PX", "SB", "SI", "SP", "SR", "SU",
            "SV", "WA", "XR", "YC", "YT", "ZW", "ZN", "ZS", "ZR", "ZR",
            "ZM", "ZL", "ZF", "ZT", "ZA", "ZH", "ZI", "FNG", "LG", "SPG",
            "IP", "LP", "MP", "NP", "QP", "RP", "TP", "BP", "YP", "GG",
            "RR", "BB", "TT", "UU", "VV", "WW", "XX", "YY", "ZZ", "AA",
            "BB", "CC", "DD", "EE", "FF", "GG", "HH", "II", "JJ", "KK",
            "LL", "MM", "NN", "OO", "PP", "QQ", "RR", "SS", "TT", "UU",
            "VV", "WW", "XX", "YY", "ZZ", "AAA", "BBB", "CCC", "DDD", "EEE"
        ]
        big_four_tickers = ["GC", "SI", "CL", "NG"]
    # Fonds
    elif asset_type == 'Fonds':
        tickers = [
            "VOO", "SPY", "IVV", "QQQ", "VTI", "IWM", "DIA", "VEA", "EFA", "VWO",
            "AGG", "BND", "LQD", "HYG", "SHY", "TLT", "TIP", "IEF", "BNDX", "VNQ",
            "IYR", "SCHX", "SCHB", "SPAB", "VTV", "VO", "VB", "VNQI", "SDY", "SCHD",
            "ARKK", "ARKG", "ARKW", "ARKF", "ARKQ", "XLK", "XLF", "XLY", "XLV", "XLP",
            "XLE", "XLC", "XLI", "XLB", "XLU", "SPHD", "SPYG", "SPYD", "VYM", "VIG",
            "IVW", "IUSV", "IJH", "IJS", "ITOT", "MDY", "SLY", "MGK", "MGV", "MTUM",
            "QUAL", "SCHM", "SCHA", "SCHP", "SCHF", "SCHV", "SCHG", "SPGP", "SPHQ", "SPMV",
            "ACWI", "VXUS", "VEU", "URTH", "RSP", "SPHB", "SPTL", "SPTM", "VTHR", "VTIP",
            "SPLV", "SPDW", "SPXN", "EEM", "EWJ", "EWZ", "EWA", "EWQ", "EWP", "EWI",
            "VGK", "FEZ", "IEFA", "ACWX", "SPGM", "FNDE", "FNDF", "SCHC", "SCZ", "RWO",
            "REET", "RWX", "VNAM", "VNM", "EWT", "EWY", "INDA", "FM", "AFK", "ASHS",
            "ASHR", "GXC", "KWEB", "EMXC", "QQQM", "FTEC", "VGT", "XNTK", "SOXX", "SMH",
            "XLRE", "IEMG", "IWV", "VXF", "VBK", "IJR", "VT", "VUG", "IVW", "SPMO",
            "VCR", "XRT", "XHB", "PKB", "ITB", "XPH", "XBI", "IBB", "XHE", "PJP",
            "XLFS", "KIE", "FXO", "IXC", "XES", "TAN", "ICLN", "PBW", "QCLN", "FAN",
            "GRID", "XME", "PICK", "COPX", "REMX", "LIT", "BATT", "KRBN", "NUBD", "HYLB",
            "PDBC", "DBC", "USCI", "GSG", "BCI", "COMT", "FTGC", "UNG", "USO", "GLD",
            "IAU", "SLV", "PALL", "PPLT", "SGOL", "BAR", "OUNZ", "UGL", "USLV", "NUGT",
            "DUST", "SOIL", "DBA", "CORN", "WEAT", "SOYB", "CANE", "JO", "NIB", "BAL",
            "WOOD", "CUT", "GUNR", "MOO", "VEGI", "PAVE", "IDRV", "FDRV", "DRIV", "LERN",
            "GENY", "MILN", "HERO", "BLOK", "BUG", "HACK", "CIBR", "BOTZ", "ROBO", "KOIN"
        ]
        big_four_tickers = ["VOO", "SPY", "IVV", "QQQ"]

    return tickers,big_four_tickers