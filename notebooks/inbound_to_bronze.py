# Databricks notebook source
# MAGIC %python
# MAGIC display(dbutils.fs.ls("/mnt/dados/inbount"))

# COMMAND ----------

# MAGIC %python
# MAGIC val_path = 'dbfs:/mnt/dados/inbount/dados_brutos_imoveis.json'
# MAGIC val_dados = spark.read.json(val_path)
# MAGIC
# MAGIC display(val_dados)

# COMMAND ----------

# MAGIC %python
# MAGIC val_dados = val_dados.drop("imagens", "usuario")
# MAGIC display(val_dados)

# COMMAND ----------

# MAGIC %python
# MAGIC from pyspark.sql.functions import col
# MAGIC
# MAGIC val_dados = val_dados.withColumn("id", col("anuncio.id"))
# MAGIC
# MAGIC display(val_dados)

# COMMAND ----------



# COMMAND ----------

# MAGIC %python
# MAGIC
# MAGIC val_path = "/mnt/dados/bronze/dataset_imoveis"
# MAGIC val_dados.write.format("delta").mode("Overwrite").save(val_path)

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


