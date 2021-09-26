
import itertools
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.stats.api as sms
from scipy.stats import ttest_1samp, shapiro, levene, ttest_ind, mannwhitneyu, pearsonr, spearmanr, kendalltau, \
    f_oneway, kruskal
from statsmodels.stats.proportion import proportions_ztest

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 10)
pd.set_option('display.float_format', lambda x: '%.5f' % x)


#GÖREV1: hipotezi kuralım
####HİPOTEZ####
#Hipotez
#H0: Maximum Bidding ile Average Bidding arasinda istatistiksel olarak anlamli bir farklilik yoktur
#H1: Maximum Bidding ile Average Bidding arasinda istatistiksel olarak anlamli bir farklilik vardir

####KONTROL GRUBU####
df_cont = pd.read_excel("ab_testing.xlsx",sheet_name="Control Group")
df_cont = df_cont.drop(['Unnamed: 4','Unnamed: 5', 'Unnamed: 6','Unnamed: 7', 'Unnamed: 8', 'Unnamed: 9','Unnamed: 10', 'Unnamed: 11','Unnamed: 12','Unnamed: 13'], axis=1)
df_cont.head()
df_cont.info()

#####TEST GRUBU#######
df_tst = pd.read_excel("ab_testing.xlsx", sheet_name="Test Group")
df_tst = df_tst.drop(['Unnamed: 4','Unnamed: 5', 'Unnamed: 6','Unnamed: 7', 'Unnamed: 8', 'Unnamed: 9','Unnamed: 10', 'Unnamed: 11','Unnamed: 12','Unnamed: 13'], axis=1)
df_tst.head()
df_tst.info()


#Görev 2: Hipotez testini gerçekleştiriniz. Çıkan sonuçların istatistiksel olarak anlamlı olup olmadığını yorumlayınız.
#varsayım kontrolü

# H0: Normal dağılım varsayımı sağlanmaktadır.
# H1:..sağlanmamaktadır.

test_stat, pvalue = shapiro(df_cont["Purchase"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

#Test Stat = 0.9773, p-value = 0.5891  H0 reddedilemez. Normallik varsayımı sağlanıyor

#varsayım kontrolü
test_stat, pvalue = shapiro(df_tst["Purchase"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))
#Test Stat = 0.9589, p-value = 0.1541 Ho reddedilemez. Normallik Varsayımı sağlanıyor.

#GÖREV 3: Hangi testi kullandınız, sebeplerini belirtiniz.
#Bağımsız iki örneklem T testi yapıyoruz.  çünkü test grubunun da kontrol grubun da pvalue değeri 0.05'ten büyük çıktı.
#H0 reddedilmedi. Varyans kontolünü yaparak varyans homojenliği ve normallik varsayımını karşıladığını gördük.


####HİPOTEZ####
#Hipotez
#H0: Maximum Bidding ile Average Bidding arasinda istatistiksel olarak anlamli bir farklilik yoktur
#H1: Maximum Bidding ile Average Bidding arasinda istatistiksel olarak anlamli bir farklilik vardir

test_stat, pvalue = ttest_ind(df_cont["Purchase"], df_tst["Purchase"], equal_var=True)
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

#Test Stat = -0.9416, p-value = 0.3493. H0 reddedilmez. yani ikisi arasında anlamlı bir farklılık yoktur.


#Gorev 4:Görev 2’de verdiğiniz cevaba göre, müşteriye tavsiyeniz nedir?
#yapılan geliştirmenin kullanmaya gerek yoktur. Çünkü anlamlı olarak bir fark olmadığını gördük

