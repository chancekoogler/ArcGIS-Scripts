# Chance Koogler
# Exercises 2: Question 1
# Ran each line in the Python Interactive Terminal and copied and pasted my code to this .py file.
import arcpy

feature_class = "c:/Users/Chance/Documents/ArcGIS/OSU_data/buildings.shp"
fields = arcpy.ListFields(feature_class)

for field in fields: 
    print("Field name:       {}".format(field.name))
    print("Field type:      {}".format(field.type))
    print("Field length:        {}".format(field.length))
    print("Field scale:     {}".format(field.scale))
    print("Field type:      {}".format(field.type))
    print("Field precision:     {}".format(field.precision))

# I know that docstrings are not best practice for comments but 
# wanted to save time by not commenting out every row. Thanks
'''
Field name:       FID
Field type:      OID
Field length:        4
Field scale:     0
Field type:      OID
Field precision:     0
Field name:       Shape
Field type:      Geometry
Field length:        0
Field scale:     0
Field type:      Geometry
Field precision:     0
Field name:       FACILITYID
Field type:      String
Field length:        50
Field scale:     0
Field type:      String
Field precision:     0
Field name:       SURFTYPE
Field type:      String
Field length:        50
Field scale:     0
Field type:      String
Field precision:     0
Field name:       SURFUSE
Field type:      String
Field length:        30
Field scale:     0
Field type:      String
Field precision:     0
Field name:       INSTALLDAT
Field type:      Date
Field length:        8
Field scale:     0
Field type:      Date
Field precision:     0
Field name:       CONDITION
Field type:      String
Field length:        50
Field scale:     0
Field type:      String
Field precision:     0
Field name:       ACCESSTYPE
Field type:      String
Field length:        50
Field scale:     0
Field type:      String
Field precision:     0
Field name:       OWNEDBY
Field type:      Integer
Field length:        5
Field scale:     0
Field type:      Integer
Field precision:     5
Field name:       MAINTBY
Field type:      Integer
Field length:        5
Field scale:     0
Field type:      Integer
Field precision:     5
Field name:       LASTUPDATE
Field type:      Date
Field length:        8
Field scale:     0
Field type:      Date
Field precision:     0
Field name:       LASTEDITOR
Field type:      String
Field length:        50
Field scale:     0
Field type:      String
Field precision:     0
Field name:       CURBHEIGHT
Field type:      String
Field length:        25
Field scale:     0
Field type:      String
Field precision:     0
Field name:       NOTES
Field type:      String
Field length:        200
Field scale:     0
Field type:      String
Field precision:     0
Field name:       Shape_STAr
Field type:      Double
Field length:        19
Field scale:     0
Field type:      Double
Field precision:     0
Field name:       Shape_STLe
Field type:      Double
Field length:        19
Field scale:     0
Field type:      Double
Field precision:     0
'''