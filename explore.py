# explorer stuff for zillow

def plot_variable_pairs(dfi):
    dfi = dfi.drop(columns = ['fips'])
    sns.pairplot(dfi.sample(1000), kind="reg", plot_kws={'line_kws':{'color':'red'}})
    plt.show()
    return dfi

def plot_categorical_and_continuous(dfi, cat, cont):
    datain = dfi.sample(1000)
    sns.boxplot(x= dfi[cat], y= dfi[cont], data=datain)
    plt.show()
    sns.violinplot(x= dfi[cat], y= dfi[cont], data=datain)
    plt.show()
    sns.barplot(x= dfi[cat], y= dfi[cont], data=datain)
    plt.show()
    return dfi