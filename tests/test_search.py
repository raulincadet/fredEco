from fredeco.fredSearch import fred_list_series, fred_info_series, fred_search, fred_vintagedates


def test_list_series_returns_dataframe():
    import pandas as pd
    dtest=fred_list_series(category_id=125,fred_api=fred_api)
    assert type(dtest)==type(pd.DataFrame()), "fred_list_series() does not return a data frame, whereas it should!"

#############

def test_info_series_is_dictionnary():
    import pandas as pd
    dtest=fred_info_series(series='GDP',fred_api=fred_api)
    assert type(dtest)==type(dict()), "fred_info_series() does not return a dictionnary, whereas it should!"
    
################

def test_search_returns_dataframe():
    import pandas as pd
    dtest=fred_search(fred_api=fred_api,text='Price index')
    assert type(dtest)==type(pd.DataFrame()), "fred_search() does not return a data frame, whereas it should!"
    
################

def test_search_returns_dataframe():
    import pandas as pd
    dtest=fred_vintagedates(series='GDP')
    assert type(dtest)==type(list()), "The function fred_vintagedates() does not return a list, whereas it should!"

######################

def test_search_outpus_isNot_empty():
    import pandas as pd
    dtest=fred_vintagedates(series='GDP')
    assert len(dtest)!=0, "The function fred_vintagedates() returns an empty output, whereas it should not!"