entity_unit_map = {
    'width': {'centimetre', 'foot', 'inch', 'metre', 'millimetre', 'yard'},
    'depth': {'centimetre', 'foot', 'inch', 'metre', 'millimetre', 'yard'},
    'height': {'centimetre', 'foot', 'inch', 'metre', 'millimetre', 'yard'},
    'item_weight': {'gram',
        'kilogram',
        'microgram',
        'milligram',
        'ounce',
        'pound',
        'ton'},
    'maximum_weight_recommendation': {'gram',
        'kilogram',
        'microgram',
        'milligram',
        'ounce',
        'pound',
        'ton'},
    'voltage': {'kilovolt', 'millivolt', 'volt'},
    'wattage': {'kilowatt', 'watt'},
    'item_volume': {'centilitre',
        'cubic foot',
        'cubic inch',
        'cup',
        'decilitre',
        'fluid ounce',
        'gallon',
        'imperial gallon',
        'litre',
        'microlitre',
        'millilitre',
        'pint',
        'quart'}
}

allowed_units = {unit for entity in entity_unit_map for unit in entity_unit_map[entity]}
#print(allowed_units)
unit_abbreviations = {
    # For 'item_weight' and 'maximum_weight_recommendation'
    'gram': ['g', 'gr', 'gm', 'grams', 'grm'],
    'kilogram': ['kg', 'kilograms', 'kgs'],
    'milligram': ['mg', 'milligrams', 'mgs'],
    'microgram': ['µg', 'mcg', 'micrograms'],
    'ounce': ['oz', 'ounces', 'ozs'],
    'pound': ['lb', 'lbs', 'pounds'],
    'ton': ['t', 'tons', 'tonne', 'tonnes'],

    # For 'item_volume'
    'millilitre': ['ml', 'milliliters', 'millilitres'],
    'litre': ['l', 'lit', 'liters', 'litres'],
    'cubic_centimetre': ['cc', 'cm³', 'cubic centimeters', 'cubic centimetres'],
    'cubic_metre': ['m³', 'cubic meters', 'cubic metres'],
    'gallon': ['gal', 'gallons'],
    'quart': ['qt', 'quarts'],
    'pint': ['pt', 'pints'],
    'cup': ['c', 'cups'],

    # For 'voltage'
    'volt': ['v', 'volts'],
    'kilovolt': ['kv', 'kilovolts'],
    'millivolt': ['mv', 'millivolts'],

    # For 'wattage'
    'watt': ['w', 'watts'],
    'kilowatt': ['kw', 'kilowatts'],
    'megawatt': ['mw', 'megawatts'],
    'gigawatt': ['gw', 'gigawatts'],

    # For 'height', 'depth', and 'width'
    'millimetre': ['mm', 'millimeters', 'millimetres'],
    'centimetre': ['cm', 'centimeters', 'centimetres'],
    'metre': ['m', 'meters', 'metres'],
    'kilometre': ['km', 'kilometers', 'kilometres'],
    'inch': ['in', 'inches'],
    'foot': ['ft', 'feet'],
    'yard': ['yd', 'yards'],
    'mile': ['mi', 'miles'],

    # Other common units
    'degree_celsius': ['°C', 'C', 'degrees Celsius'],
    'degree_fahrenheit': ['°F', 'F', 'degrees Fahrenheit'],
    'calorie': ['cal', 'calories'],
    'kilocalorie': ['kcal', 'kcals'],
    'joule': ['j', 'joules'],
    'pascal': ['Pa', 'pascals'],
    'bar': ['bar', 'bars'],
    'psi': ['psi', 'pounds per square inch'],
    'newton': ['N', 'newtons'],
    'fluid_ounce': ['fl oz', 'fluid ounces'],
}