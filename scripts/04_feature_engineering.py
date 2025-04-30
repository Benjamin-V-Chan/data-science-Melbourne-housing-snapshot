# Load pandas, os
# Define engineer(input_parquet, output_parquet)
#   read Parquet
#   extract Year, Month from Date
#   compute PricePerRoom and PricePerSqm
#   one‐hot encode Type, Method, Regionname, CouncilArea
#   write features to Parquet
# if __name__ == "__main__": call engineer with paths
