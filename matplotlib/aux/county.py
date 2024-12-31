import database as db

import requests

from aux.database import inserts
from models import County


def get_key(json, key):
    if key in json:
        return json[key]
    raise KeyError('key %s not found' % key)


def get_id(json):
    if 'id' in json:
        return json['id']
    raise KeyError('key id not found')


def get_county_name(json):
    if 'nome' in json:
        return json['nome']
    raise KeyError('key nome not found')


def get_region_name(json):
    return json['microrregiao']['mesorregiao']['UF']['regiao']['nome']


def get_uf(json):
    if 'microrregiao' in json:
        if 'mesorregiao' in json['microrregiao']:
            if 'UF' in json['microrregiao']['mesorregiao']:
                return get_acronym_state(json), get_name_state(json), get_region_name(json)
            raise KeyError('key UF not found')
        raise KeyError('key mesorregiao not found')
    raise KeyError('key microrregiao not found')


def get_name_state(json):
    return json['microrregiao']['mesorregiao']['UF']['nome']


def get_acronym_state(json):
    return json['microrregiao']['mesorregiao']['UF']['sigla']


def count_in_county_table(session):
    try:
        return session.query(County).count()
    except Exception as e:
        print(e)
        session.flush()


def parse_json(json):
    return County(id=get_id(json), county=get_acronym_state(json), uf=get_uf(json), state=get_name_state(json), regiao=get_region_name(json))


def get_municipios():
    try:
        response = requests.get('http://servicodados.ibge.gov.br/api/v1/localidades/municipios')
        return response
    except Exception as e:
        print(e)


def insert_counties(session):
    # pip install pyopenssl cryptography
    response = get_municipios()
    query = count_in_county_table(session)
    if not db.table_is_empty(query):
        return

    counties = [parse_json(j) for j in response.json()]
    inserts(session, counties)


