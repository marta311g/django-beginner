CREATE($request_name:Request {datetime: $datetime, timezone: $timezone, method: $method, url: $url, status_code: $status_code}), request_name=request_name
CREATE($param_name:Parameter {left: $left, right: $right})
CREATE($ip_name:IP_Address {address: $address, ip_type: $ip_type})
CREATE($isp_name:ISP {name = $isp_name})
CREATE($as_name:AS {as_number: $as_number})
CREATE($city:City {name: $city_name, postal_code: $postal_code})
CREATE($region:Region {name: $region_name})
CREATE($country:Country {name: $country_name, iso_id: $iso_id})

CREATE($param_name)-[:HAS_PARAMETERS]->($request_name)
CREATE($ip_name)-[:HAS_SENT]->($request_name)
CREATE($isp_name)-[:PROVIDES]->($ip_name)
CREATE($isp_name)-[:HAS_AS]->($as_number)
CREATE($ip_name)-[:LOCATED_IN {latitude: $latitude, longitude: $longitude}]->($city)
CREATE($city)-[:IN]->($region)
CREATE($region)-[:PART_OF]->($country)

