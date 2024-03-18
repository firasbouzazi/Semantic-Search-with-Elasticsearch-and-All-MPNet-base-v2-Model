indexMapping = {
    "properties":{
        "ProductID":{
            "type":"long"
        },
        "ProductName":{
            "type":"text"
        },
        "ProductBrand":{
            "type":"text"
        },
        "Gender":{
            "type":"text"
        },
        "Price (INR)":{
            "type":"long"
        },
        "Description":{
            "type":"text"
        },
        "PrimaryColor":{
            "type":"text"
        },
        "DescriptionVector":{
            "type":"dense_vector",
            "dims":768,
            "index":True,## Column is searchable
            "similarity":"l2_norm"

             
        }

    }
}