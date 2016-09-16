import pubchempy as pcp

def search_compound(name):
    response = []
    results = pcp.get_compounds(name, 'name')
    for result in results:
        response.append(
                dict(formula = result.molecular_formula,
                    name = result.synonyms[0],
                    cid = result.cid
                    ))
    return response

