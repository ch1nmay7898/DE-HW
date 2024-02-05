import re
if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    bad_row_condition = (data['passenger_count'] == 0) | (data['trip_distance'] == 0)
    data = data[~bad_row_condition]
    data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date
    data.columns = [re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', col).lower() for col in data.columns]
    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert 'vendor_id' in output.columns, 'vendor_id does not exist or is improperly named.'
    assert output['passenger_count'].isin([0]).sum() == 0, 'records with passenger_count = 0, exists'
    assert output['trip_distance'].isin([0]).sum() == 0, 'records with trip_distance = 0, exists'
