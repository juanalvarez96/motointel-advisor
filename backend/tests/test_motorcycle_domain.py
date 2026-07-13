from app.domain.motorcycle import Motorcycle, MotorcycleCreate


def _assert_model_fields(model, expected_fields):
    for field_name, expected_value in expected_fields.items():
        assert getattr(model, field_name) == expected_value


def test_valid_motorcycle_create_model():
    motorcycle_data = {
        "make": "Yamaha",
        "model": "Ténéré 700",
        "year": 2025,
        "category": "adventure",
        "engine_cc": 689,
        "power_hp": 72.0,
        "weight_kg": 205.0,
        "seat_height_mm": 875,
        "features": ["ABS", "Cruise control"],
        "description": "A capable adventure bike.",
    }

    motorcycle_create = MotorcycleCreate(**motorcycle_data)
    _assert_model_fields(motorcycle_create, motorcycle_data)

    motorcycle_unsupported_data = {**motorcycle_data, "color": "blue"}
    motorcycle_create_unsupported = MotorcycleCreate(**motorcycle_unsupported_data)

    _assert_model_fields(motorcycle_create_unsupported, motorcycle_data)
    assert not hasattr(motorcycle_create_unsupported, "color")


def test_motorcycle_inherits_create_fields_and_generates_id():
    motorcycle_data = {
        "make": "Honda",
        "model": "CBR600RR",
        "year": 2021,
        "category": "sport",
        "engine_cc": 599,
        "power_hp": 118.0,
        "weight_kg": 189.0,
        "seat_height_mm": 830,
        "features": ["Quickshifter"],
        "description": "A track-focused supersport machine.",
    }

    motorcycle = Motorcycle(**motorcycle_data)
    _assert_model_fields(motorcycle, motorcycle_data)
    assert isinstance(motorcycle.id, str)
    assert motorcycle.id
