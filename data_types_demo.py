def demonstrate_data_types():

    # Integer
    integer_example = 42
    print(f"Integer: {integer_example}, Type: {type(integer_example)}")

    # Float
    float_example = 3.14159
    print(f"Float: {float_example}, Type: {type(float_example)}")

    # String
    string_example = "Hello, World!"
    print(f"String: '{string_example}', Type: {type(string_example)}")

    # List
    list_example = [1, 2, 3, 4, 5]
    print(f"List: {list_example}, Type: {type(list_example)}")

    # Tuple
    tuple_example = (1, 2, 3, 4, 5)
    print(f"Tuple: {tuple_example}, Type: {type(tuple_example)}")

    # Dictionary
    dict_example = {"name": "Alice", "age": 30, "city": "New York"}
    print(f"Dictionary: {dict_example}, Type: {type(dict_example)}")

    # Set
    set_example = {1, 2, 3, 4, 5}
    print(f"Set: {set_example}, Type: {type(set_example)}")

    # Boolean
    boolean_example = True
    print(f"Boolean: {boolean_example}, Type: {type(boolean_example)}")

    # NoneType
    none_example = None
    print(f"NoneType: {none_example}, Type: {type(none_example)}")

    # Bytes
    bytes_example = b"byte string"
    print(f"Bytes: {bytes_example}, Type: {type(bytes_example)}")

    # Bytearray
    bytearray_example = bytearray(b"byte array")
    print(f"Bytearray: {bytearray_example}, Type: {type(bytearray_example)}")

    # Memoryview
    memoryview_example = memoryview(b"memory view")
    print(f"Memoryview: {memoryview_example}, Type: {type(memoryview_example)}")

    # Complex Number
    complex_example = 1 + 2j
    print(f"Complex: {complex_example}, Type: {type(complex_example)}")


if __name__ == "__main__":
    demonstrate_data_types()
