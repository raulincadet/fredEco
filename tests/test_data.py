from fredeco.fredData import fred_series, fred_multi_series, explore
from fredeco.fredSearch import fred_info_series



def test_series_is_dataframe():            # test if the output of fred_series is a data frame.
    import pandas as pd
    dtest=fred_series(series='GDP',fred_api=fred_api)
    assert type(dtest)==type(pd.DataFrame()), "The function fred_series() does not return a data frame, whereas it should!"


def test_multi_series_is_dataframe():      # test if the output of fred_multi_series is a data frame.
    import pandas as pd
    dtest=fred_multi_series(series=['GDP','FEDFUNDS','GDPCA'],fred_api=fred_api)
    assert type(dtest)==type(pd.DataFrame()), "The function fred_multi_series() does not return a data frame, whereas it should!"


###############################################

def test_series_correct_columnName():            # test if the column name is the same as the economic indicator provided by the user.
    dtest=fred_series(series='GDP',fred_api=fred_api)
    assert (dtest.columns.tolist())[0]=='GDP', "The data frame returns by fred_series() does not have the same column name as the indicator's ID provided by the user!"

##################

def test_multi_series_correct_columnsNames():      # test if the columns names are the same as the economic indicators provided by the user.
    dtest=fred_multi_series(series=['GDP','FEDFUNDS','GDPCA'],fred_api=fred_api)
    assert dtest.columns.tolist()==['GDP','FEDFUNDS','GDPCA'], "The data frame returns by fred_series() does not have the same columns names as the series indicated by the user!"

#####################


def test_explore_is_dataframe():      # test if the output of fred_multi_series is a data frame.
    import random
    import pandas as pd
    xx=[random.random() for i in range(300)]        # generate random data for the test
    yy=[random.random()*500000 for i in range(300)] # random data generated for the test
    df=pd.DataFrame({'GDP':yy,'FEDFUNDS':xx})   # used real FRED indicators IDs, to retreive their units of measure from FRED API
    assert type(explore(df))==type(pd.DataFrame()), "The function explore() does not return a data frame, whereas it should!"

#############

def test_explore_columnsNames():      # test if the columns names are the same as the economic indicators provided by the user.
    import random
    import pandas as pd
    xx=[random.random() for i in range(300)]        # generate random data for the test
    yy=[random.random()*500000 for i in range(300)] # random data generated for the test
    df=pd.DataFrame({'GDP':yy,'FEDFUNDS':xx})   # used real FRED indicators IDs, to retreive their units of measure from FRED API
    dexplore=explore(df)
    assert dexplore.columns.tolist()==['GDP','FEDFUNDS'], "The output of explore() does not have the same columns names as those of the data frame provided by the user!"