# Load pandas
# Define preprocess(input_parquet, output_parquet)
#   read Parquet
#   drop rows where Price is missing or ≤ 0
#   drop Price above 99th percentile
#   fill BuildingArea nulls with median
#   write cleaned Parquet
# if __name__ == "__main__": call preprocess with paths
