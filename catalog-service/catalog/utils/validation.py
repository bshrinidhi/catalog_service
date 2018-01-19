from catalog.common.errors import BadRequest


def validate_create_catalog(catalog_json):
    validation_errors = []
    if 'catalog' not in catalog_json:
        raise BadRequest('CATALOG_ATTRS_MISSING')
    catalog_data = catalog_json['catalog']
    if 'name' not in catalog_data or str(catalog_data['name']) is '':
        validation_errors.append('CATALOG_NAME_MANDATORY')
    if 'description' not in catalog_data or str(catalog_data['description']) is '':
        validation_errors.append('CATALOG_DESCRIPTION_MANDATORY')
    if 'ic_subset' not in catalog_data or not catalog_data['ic_subset']:
        validation_errors.append('CATALOG_IC_SUBSET_MANDATORY')
    if 'visibility' not in catalog_data or str(catalog_data['visibility']) is '':
        validation_errors.append('CATALOG_VISIBILITY_MANDATORY')
    return validation_errors
def validate_update_catalog(catalog_json):
    validation_errors = []
    if 'catalog' not in catalog_json:
        raise BadRequest('CATALOG_ATTRS_MISSING')
    catalog_data = catalog_json['catalog']
    if 'name'  in catalog_data and str(catalog_data['name']) is '':
        validation_errors.append('CATALOG_NAME_MANDATORY')
    if 'ic_subset'  in catalog_data and not catalog_data['ic_subset']:
        validation_errors.append('CATALOG_IC_SUBSET_MANDATORY')
    if 'visibility'  in catalog_data and str(catalog_data['visibility']) is '':
        validation_errors.append('CATALOG_VISIBILITY_UNSPECIFIED')
    if 'owner' in catalog_data and  str(catalog_data['owner']) is '':
            validation_errors.append('CATALOG_OWNER_UNSPECIFIED')
    return validation_errors

