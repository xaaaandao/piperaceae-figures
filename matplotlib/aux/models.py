import sqlalchemy as sa
import sqlalchemy.ext.declarative

Base = sa.ext.declarative.declarative_base()


def get_base():
    return Base


class DataSP(Base):
    __tablename__ = 'data_sp'

    seq = sa.Column(sa.BigInteger, primary_key=True)
    modified = sa.Column(sa.DateTime, nullable=True)
    institution_code = sa.Column(sa.String, nullable=True)
    collection_code = sa.Column(sa.String, nullable=True)
    catalog_number = sa.Column(sa.String, nullable=True)
    basis_of_record = sa.Column(sa.String, nullable=True)
    kingdom = sa.Column(sa.String, nullable=True)
    phylum = sa.Column(sa.String, nullable=True)
    classe = sa.Column(sa.String, nullable=True)
    order = sa.Column(sa.String, nullable=True)
    family = sa.Column(sa.String, nullable=True)
    genus = sa.Column(sa.String, nullable=True)
    specific_epithet = sa.Column(sa.String, nullable=True)
    infraspecific_epithet = sa.Column(sa.String, nullable=True)
    scientific_name = sa.Column(sa.String, nullable=True)
    scientific_name_authorship = sa.Column(sa.String, nullable=True)
    identified_by = sa.Column(sa.String, nullable=True)
    year_identified = sa.Column(sa.String, nullable=True)
    month_identified = sa.Column(sa.String, nullable=True)
    day_identified = sa.Column(sa.String, nullable=True)
    type_status = sa.Column(sa.String, nullable=True)
    recorded_by = sa.Column(sa.String, nullable=True)
    record_number = sa.Column(sa.String, nullable=True)
    field_number = sa.Column(sa.String, nullable=True)
    year = sa.Column(sa.BigInteger, nullable=True)
    month = sa.Column(sa.BigInteger, nullable=True)
    day = sa.Column(sa.BigInteger, nullable=True)
    event_time = sa.Column(sa.String, nullable=True)
    continent_ocean = sa.Column(sa.String, nullable=True)
    country = sa.Column(sa.String, nullable=True)
    state_province = sa.Column(sa.String, nullable=True)
    county = sa.Column(sa.String, nullable=True)
    locality = sa.Column(sa.String, nullable=True)
    decimal_longitude = sa.Column(sa.String, nullable=True)
    decimal_latitude = sa.Column(sa.String, nullable=True)
    verbatim_longitude = sa.Column(sa.String, nullable=True)
    verbatim_latitude = sa.Column(sa.String, nullable=True)
    coordinate_precision = sa.Column(sa.String, nullable=True)
    bounding_box = sa.Column(sa.String, nullable=True)
    minimum_elevation_in_meters = sa.Column(sa.BigInteger, nullable=True)
    maximum_elevation_in_meters = sa.Column(sa.BigInteger, nullable=True)
    minimum_depth_in_meters = sa.Column(sa.BigInteger, nullable=True)
    maximum_depth_in_meters = sa.Column(sa.BigInteger, nullable=True)
    sex = sa.Column(sa.String, nullable=True)
    preparation_type = sa.Column(sa.String, nullable=True)
    individual_count = sa.Column(sa.BigInteger, nullable=True)
    previous_catalog_number = sa.Column(sa.String, nullable=True)
    relationship_type = sa.Column(sa.String, nullable=True)
    related_catalog_item = sa.Column(sa.String, nullable=True)
    occurrence_remarks = sa.Column(sa.String, nullable=True)
    barcode = sa.Column(sa.String, nullable=True)
    imagecode = sa.Column(sa.String, nullable=True)
    geo_flag = sa.Column(sa.String, nullable=True)
    george = sa.Column(sa.Boolean, nullable=True)

    def __repr__(self):
        return 'DataSP(seq=%s, modified=%s, institution_code=%s, collection_code=%s, catalog_number=%s, ' \
               'basis_of_record=%s, kingdom=%s, phylum=%s, classe=%s, order=%s, family=%s, genus=%s, ' \
               'specific_epithet=%s, infraspecific_epithet=%s, scientific_name=%s, scientific_name_authorship=%s, ' \
               'identified_by=%s, year_identified=%s, month_identified=%s, day_identified=%s, type_status=%s, ' \
               'recorded_by=%s, record_number=%s, field_number=%s, year=%s, month=%s, day=%s, event_time=%s, ' \
               'continent_ocean=%s, country=%s, state_province=%s, county=%s, locality=%s, decimal_longitude=%s, ' \
               'decimal_latitude=%s, verbatim_longitude=%s, verbatim_latitude=%s, coordinate_precision=%s, ' \
               'bounding_box=%s, minimum_elevation_in_meters=%s, maximum_elevation_in_meters=%s, ' \
               'minimum_depth_in_meters=%s, maximum_depth_in_meters=%s, sex=%s, preparation_type=%s, ' \
               'individual_count=%s, previous_catalog_number=%s, relationship_type=%s, related_catalog_item=%s, ' \
               'occurrence_remarks=%s, barcode=%s, imagecode=%s, geo_flag=%s)'


# County is muncipio, condado
class County(Base):
    __tablename__ = 'county'

    id = sa.Column(sa.Integer, primary_key=True)
    county = sa.Column(sa.String, nullable=True)
    uf = sa.Column(sa.String, nullable=True)
    state = sa.Column(sa.String, nullable=True)
    regiao = sa.Column(sa.String, nullable=True)

    def __repr__(self):
        return 'County(id=%s, county=%s, uf=%s, state=%s, regiao=%s)'
