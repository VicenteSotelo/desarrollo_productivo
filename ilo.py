
# ====================================
# Project : Desarrollo Productivo 
# Creators: VS
# Date     :06.10.23
# Goal     :new leader indicators: indicadores del futuro
# source: https://www.ilo.org/shinyapps/bulkexplorer13/?lang=en&id=SDG_0831_SEX_ECO_RT_A	
 # ====================================

# A) Informalidad

# setting path

# path="/Users/luisvicentesotelofarfan/My\Drive(vicente@thewhyhub.com)/second_brain🧠/python🐍/projects/ilo"

#I. setting dev

#setting tools
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import os

#setting dir
# cwd=os.getcwd()
# print (cwd)

#II. import data

df_ilo= pd.read_csv('SDG_0831_SEX_ECO_RT_A-filtered-2023-06-11.csv', sep=',')

#rename column name
df_ilo=df_ilo.rename(columns={'ref_area.label':'País'})


#explore data
# print(df_ilo.types)

print(df_ilo['País'].value_counts())

# #setting condions
cond=df_ilo['País'].isin(['Argentina','Colombia','Peru','Chile','Mexico','Uruguay','Brasil'])

# #pull data
df_1=df_ilo[cond]
# print(df_1.head(20))


# # drawing

# #setting backroung style, context (deliver)

sns.set_style('white')
sns.set_context('talk')


#set up palette dict

# resource: https://colorhunt.co/palette/f7f1e5e7b10a8981214c4b16
palette= 'deep'
sns.set_palette(palette)
pal= {'Argentina':'#B4E4FF','Colombia':'#F5EFE7','Peru':'#dd1c1a','Chile':'#DDFFBB','Mexico':'#C4DFDF','Uruguay':'#FFF8DE'}

# # plot data
plot=sns.relplot(data=df_1,x='time',y='obs_value',kind='line',hue='País',palette=pal)
# plot=sns.scatterplot(data=df_1,x='time',y='obs_value',hue='País',palette=pal)



# set up caption
# cap='source:https://github.com/VicenteSotelo/desarrollo_productivo'



caption_text = "Source: https://github.com/VicenteSotelo/desarrollo_productivo"
caption_x =-0.2
caption_y =-0.2
plt.annotate(caption_text, (caption_x, caption_y), xycoords='axes fraction', fontsize=8, color='gray')


# title, label
plt.title('Porcentaje del Empleo Informal en el Empleo Total')
plt.xlabel('año')
plt.ylabel('Porcentaje (%)')


# deliver plot
plt.show()



