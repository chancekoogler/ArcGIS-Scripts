import arcpy

# Load and select building where FID = 4.
arcpy.env.workspace = r"C:/Users/Chance/Documents/ArcGIS/OSU_data"
in_features = "buildings.shp"
out_feature_class = "D:/temp/buildingsSelect.shp"
where = '"FID" = 4'


# Execute
arcpy.Select_analysis(in_features, out_feature_class, where)
