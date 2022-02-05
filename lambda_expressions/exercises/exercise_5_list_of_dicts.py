"""
LIST OF DICTS

Naszym zadaniem jest przeprowadzenie szeregu dzialań na liście dictow:
* sorted - posortowanie listy dictow rosnaco po atrybucie 'priority'
* min - wyciagniecie obiektu z listy dictow o minimalnej wartosc 'priority'
* max - wyciagniecie obiektu z listy dictow o maksymalnej wartosc 'priority'
"""
if __name__ == '__main__':
    dicts = [
        {
            'id': 3,
            'priority': 4,
        },
        {
            'id': 4,
            'priority': 5,
        },
        {
            'id': 5,
            'priority': 3,
        },
        {
            'id': 6,
            'priority': 1,
        }
    ]

    sorted_expected = [
        {
            'id': 6,
            'priority': 1,
        },
        {
            'id': 5,
            'priority': 3,
        },
        {
            'id': 3,
            'priority': 4,
        },
        {
            'id': 4,
            'priority': 5,
        }
    ]

    sorted_dicts = sorted(dicts, key=lambda x: x['priority'])
    sorted_dicts = sorted(dicts, key=lambda x: x.get('priority'))
    print(sorted_dicts)
    assert sorted_expected == sorted_dicts

    minimum = min(dicts, key=lambda x: x['priority'])
    assert minimum == {'id': 6, 'priority': 1}

    maximum = max(dicts, key=lambda x: x['priority'])
    assert maximum == {'id': 4, 'priority': 5}
