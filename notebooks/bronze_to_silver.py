# Databricks notebook source
# MAGIC %python
# MAGIC display(dbutils.fs.ls("/mnt/dados/bronze"))
# MAGIC

# COMMAND ----------

# MAGIC %python
# MAGIC path = "/mnt/dados/bronze/dataset_imoveis/"
# MAGIC df = spark.read.format("delta").load(path)
# MAGIC df.show()

# COMMAND ----------



# COMMAND ----------

# MAGIC %python
# MAGIC from pyspark.sql.functions import col
# MAGIC
# MAGIC sf = df.select(col("anuncio.*"), col("anuncio.endereco.*"))
# MAGIC
# MAGIC sf.show()
# MAGIC

# COMMAND ----------

# MAGIC %python
# MAGIC
# MAGIC val_path = "/mnt/dados/silver/dataset_imoveis"
# MAGIC sf.write.format("delta").mode("Overwrite").save(val_path)

# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------


