#search for records with values that contain val
# def locator (df,col,val):
#     '''
#     This is used a function to create unique
#     filters to return all records where a column
#     has a matching val for any passed dataframe.
#     Use the returned list as the .iloc filter
#     '''
#     a_list=[]
#     for i in range(len(df[col])):
#         if type(df[col].iloc[i])==list:
#             if val in df[col].iloc[i]:
#                 a_list.append(i)
#         else:
#             if val == df[col].iloc[i]:
#                 a_list.append(i)
    #return the list of locations to be used as a .iloc filter
    # return a_list

#create a list of unique possible values based on a column
#with lists or not
def locator(df, col, val):
    a_list = []
    for i in range(len(df[col])):
        if isinstance(df[col].iloc[i], list):
            if str(val) in [str(x) for x in df[col].iloc[i]]:
                a_list.append(i)
        else:
            if str(val) == str(df[col].iloc[i]):
                a_list.append(i)
    return a_list

def pos_values(df, col):
    p_list = []
    for i in range(len(df[col])):
        if type(df[col].iloc[i]) == list:
            s = df[col].iloc[i]
            for j in s:
                p_list.append(j)
        else:
            p_list.append(df[col].loc[i])

    p_list = [str(x) for x in p_list]  # Convert all elements to strings
    p_list = list(set(p_list))  # Remove duplicates
    p_list.sort()  # Sort the list
    return p_list

# def pos_values(df,col):
#     '''
#     This will reveal to you all relevant or possible values
#     from a data frame (a distinct function) for cols with lists
#     and non list items mixed.
#     '''
#     p_list=[]
#     for i in range(len(df[col])):
#         if type(df[col].iloc[i])==list:
#             s=df[col].iloc[i]
#             for j in s:
#                 p_list.append(j)
#         else:
#             p_list.append(df[col].loc[i])
            
#     p_list=list(set(p_list))
#     p_list.sort()
#     return p_list

# def stringConvert (df,col):
#     '''
#     This is utilized to call a df frame and column
#     and is useful for creating string dummy columns
#     that play nice for streamlit in there crisp dataframe box
#     '''
#     a_list=[]
#     for i in range(len(df[col])):
#         if type(df[col].iloc[i])==list:
#             a_list.append(', '.join(j for j in df[col].iloc[i]))
#         else:
#             a_list.append(str(df[col].iloc[i]))
#     #return the list of locations to be used as a .iloc filter
#     return a_list

def stringConvert(df, col):
    a_list = []
    for i in range(len(df[col])):
        if isinstance(df[col].iloc[i], list):
            a_list.append(', '.join(str(j) for j in df[col].iloc[i]))
        else:
            a_list.append(str(df[col].iloc[i]))
    return a_list


