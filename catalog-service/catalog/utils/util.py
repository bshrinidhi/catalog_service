from catalog.models.catalog import Catalog


def toCatalog(catalog_json):
    catalog = Catalog(catalog_json['name'])
    catalog.description = catalog_json['description']
    catalog.ic_subset = catalog_json['icSubset']
    catalog.status = catalog_json['status']
    catalog.tags = catalog_json['tags'] or []
    catalog.owner = catalog_json['owner']
    catalog.visibility = catalog_json['visibility']

def getcollecteddata(row):
    prevdata = {}
    prevdata["name"] = row.name
    prevdata["description"] = row.description
    prevdata["ic_subset"] = row.ic_subset
    prevdata["owner"] = row.owner
    prevdata["status"] = row.status
    prevdata["version"] = row.version
    prevdata["visibility"] = row.visibility
    prevdata["tags"] = row.tags
    return prevdata