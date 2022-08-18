from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import *

spark = SparkSession.builder.appName("TCC ai bro").getOrCreate()


df_ibova = spark.read.option("header", True).csv("ibova.csv")
df_ibova = df_ibova.select(
    col("Open").alias("open_ibova"), col("Date").alias("date_ibova")
)

df_oil = spark.read.option("header", True).csv("oil.csv")
df_oil = df_oil.select(col("Open").alias("open_oil"), col("Date").alias("date_oil"))

df_usdbrl = spark.read.option("header", True).csv("usdbrl.csv")
df_usdbrl = df_usdbrl.select(
    col("Open").alias("open_usd"), col("Date").alias("date_usd")
)

df_abev = spark.read.option("header", True).csv("Open_ABEV3.SA.csv")
df_abev = df_abev.select(col("Open").alias("open_abev"), col("Date").alias("date_abev"))

df_jbs = spark.read.option("header", True).csv("Open_JBSAY.csv")
df_jbs = df_jbs.select(col("Open").alias("open_jbs"), col("Date").alias("date_jbs"))

df_petr4 = spark.read.option("header", True).csv("Open_PETR4.csv")
df_petr4 = df_petr4.select(
    col("Open").alias("open_petr4"), col("Date").alias("date_petr4")
)

df_vale = spark.read.option("header", True).csv("Open_PETR4.csv")
df_vale = df_vale.select(col("Open").alias("open_vale"), col("Date").alias("date_vale"))

ibova = df_ibova.count()
oil = df_oil.count()
sp500 = df_sp500.count()
us10y = df_us10y.count()
usdbrl = df_usdbrl.count()
abev = df_abev.count()
jbs = df_jbs.count()
petr4 = df_petr4.count()
vale = df_vale.count()

print(
    f"""\b Controle:
	ibova = {ibova}
	oil = {oil}
	sp500 = {sp500}
	us10y = {us10y}
	usdbrl = {usdbrl}
	abev = {abev}
	jbs = {jbs}
	petr4 = {petr4}
	vale = {vale}
"""
)

df = df_ibova.join(df_oil, df_oil.date_oil == df_ibova.date_ibova)
df = df.join(df_usdbrl, df_usdbrl.date_usd == df_ibova.date_ibova)
df = df.join(df_abev, df_abev.date_abev == df_ibova.date_ibova)
df = df.join(df_jbs, df_jbs.date_jbs == df_ibova.date_ibova)
df = df.join(df_petr4, df_petr4.date_petr4 == df_ibova.date_ibova)
df = df.join(df_vale, df_vale.date_vale == df_ibova.date_ibova)

df = df.select(
    col("date_ibova").alias("date"),
    col("open_ibova").alias("open_ibova"),
    col("open_oil").alias("open_oil"),
    col("open_usd").alias("open_usd"),
    col("open_abev").alias("open_abev"),
    col("open_jbs").alias("open_jbs"),
    col("open_petr4").alias("open_petr4"),
    col("open_vale").alias("open_vale"),
)

# df.write.format('csv').save('ibova_oil_usd.csv',header = 'true')
df.repartition(1).write.format("com.databricks.spark.csv").save(
    "myfile.csv", header="true"
)
