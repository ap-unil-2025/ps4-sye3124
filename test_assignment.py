"""
Automated tests for Week 4 Assignment
This file contains pytest tests that will run automatically via GitHub Actions.
"""

import pytest
import os
import json

# Import student solutions
from problem1 import (
    create_number_list, filter_even_numbers, square_numbers,
    find_max_min, remove_duplicates, merge_lists,
    list_statistics, chunk_list
)

from problem2 import (
    create_student_record, get_value_safely, merge_dictionaries,
    count_word_frequency, invert_dictionary, filter_dictionary,
    group_by_first_letter, calculate_grades_average, nested_dict_access
)

from problem3 import (
    create_contact, add_contact, find_contact_by_name,
    search_contacts, delete_contact, count_contacts_with_email,
    get_all_phone_numbers, sort_contacts_by_name, contact_exists
)

from problem4 import (
    save_to_json, load_from_json, save_contacts_to_file,
    load_contacts_from_file, append_contact_to_file,
    backup_file, get_file_stats, merge_json_files, search_json_file
)


# Problem 1 Tests: List Operations
class TestProblem1:
    def test_create_number_list(self):
        assert create_number_list(1, 5) == [1, 2, 3, 4, 5]
        assert create_number_list(10, 13) == [10, 11, 12, 13]

    def test_filter_even_numbers(self):
        assert filter_even_numbers([1, 2, 3, 4, 5, 6]) == [2, 4, 6]
        assert filter_even_numbers([1, 3, 5]) == []

    def test_square_numbers(self):
        assert square_numbers([1, 2, 3, 4]) == [1, 4, 9, 16]
        assert square_numbers([0, 5, 10]) == [0, 25, 100]

    def test_find_max_min(self):
        assert find_max_min([3, 1, 4, 1, 5, 9, 2, 6]) == (9, 1)
        assert find_max_min([10]) == (10, 10)

    def test_remove_duplicates(self):
        assert remove_duplicates([1, 2, 2, 3, 4, 3, 5]) == [1, 2, 3, 4, 5]
        assert remove_duplicates([1, 1, 1]) == [1]

    def test_merge_lists(self):
        assert merge_lists([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
        assert merge_lists([1, 2], [10, 20, 30, 40]) == [1, 10, 2, 20, 30, 40]

    def test_list_statistics(self):
        result = list_statistics([1, 2, 3, 4, 5])
        assert result == {'sum': 15, 'average': 3.0, 'count': 5, 'max': 5, 'min': 1}

    def test_chunk_list(self):
        assert chunk_list([1, 2, 3, 4, 5, 6, 7], 3) == [[1, 2, 3], [4, 5, 6], [7]]
        assert chunk_list([1, 2], 5) == [[1, 2]]


# Problem 2 Tests: Dictionary Operations
class TestProblem2:
    def test_create_student_record(self):
        result = create_student_record("Alice", 20, "CS", 3.8)
        assert result == {'name': 'Alice', 'age': 20, 'major': 'CS', 'gpa': 3.8}

    def test_get_value_safely(self):
        d = {'a': 1, 'b': 2}
        assert get_value_safely(d, 'a') == 1
        assert get_value_safely(d, 'c', 'Not found') == 'Not found'

    def test_merge_dictionaries(self):
        result = merge_dictionaries({'a': 1, 'b': 2}, {'b': 3, 'c': 4})
        assert result == {'a': 1, 'b': 3, 'c': 4}

    def test_count_word_frequency(self):
        result = count_word_frequency("hello world hello")
        assert result == {'hello': 2, 'world': 1}

    def test_invert_dictionary(self):
        result = invert_dictionary({'a': 1, 'b': 2, 'c': 3})
        assert result == {1: 'a', 2: 'b', 3: 'c'}

    def test_filter_dictionary(self):
        result = filter_dictionary({'a': 1, 'b': 2, 'c': 3, 'd': 4}, ['a', 'c'])
        assert result == {'a': 1, 'c': 3}

    def test_group_by_first_letter(self):
        result = group_by_first_letter(['apple', 'banana', 'apricot', 'blueberry'])
        assert result == {'a': ['apple', 'apricot'], 'b': ['banana', 'blueberry']}

    def test_calculate_grades_average(self):
        result = calculate_grades_average({
            'Alice': [90, 85, 88],
            'Bob': [75, 80, 78]
        })
        assert result == {'Alice': 87.67, 'Bob': 77.67}

    def test_nested_dict_access(self):
        data = {'a': {'b': {'c': 123}}}
        assert nested_dict_access(data, ['a', 'b', 'c']) == 123
        assert nested_dict_access(data, ['a', 'x']) is None


# Problem 3 Tests: Contact Manager
class TestProblem3:
    def test_create_contact(self):
        contact = create_contact("Alice", "555-0001", "alice@email.com")
        assert contact == {'name': 'Alice', 'phone': '555-0001', 'email': 'alice@email.com'}

    def test_add_contact(self):
        contacts = []
        add_contact(contacts, "Alice", "555-0001", "alice@email.com")
        assert len(contacts) == 1
        assert contacts[0]['name'] == 'Alice'

    def test_find_contact_by_name(self):
        contacts = [{'name': 'Alice', 'phone': '555-0001', 'email': ''}]
        found = find_contact_by_name(contacts, 'alice')
        assert found is not None
        assert found['name'] == 'Alice'

    def test_search_contacts(self):
        contacts = [
            {'name': 'Alice Smith', 'phone': '555-0001', 'email': ''},
            {'name': 'Bob Jones', 'phone': '555-0002', 'email': ''}
        ]
        results = search_contacts(contacts, 'alice')
        assert len(results) == 1
        assert results[0]['name'] == 'Alice Smith'

    def test_delete_contact(self):
        contacts = [
            {'name': 'Alice', 'phone': '555-0001', 'email': ''},
            {'name': 'Bob', 'phone': '555-0002', 'email': ''}
        ]
        deleted = delete_contact(contacts, 'Alice')
        assert deleted == True
        assert len(contacts) == 1

    def test_count_contacts_with_email(self):
        contacts = [
            {'name': 'Alice', 'phone': '555-0001', 'email': 'alice@email.com'},
            {'name': 'Bob', 'phone': '555-0002', 'email': ''}
        ]
        assert count_contacts_with_email(contacts) == 1

    def test_get_all_phone_numbers(self):
        contacts = [
            {'name': 'Alice', 'phone': '555-0001', 'email': ''},
            {'name': 'Bob', 'phone': '555-0002', 'email': ''}
        ]
        phones = get_all_phone_numbers(contacts)
        assert phones == ['555-0001', '555-0002']

    def test_sort_contacts_by_name(self):
        contacts = [
            {'name': 'Charlie', 'phone': '555-0003', 'email': ''},
            {'name': 'Alice', 'phone': '555-0001', 'email': ''}
        ]
        sorted_contacts = sort_contacts_by_name(contacts)
        names = [c['name'] for c in sorted_contacts]
        assert names == ['Alice', 'Charlie']

    def test_contact_exists(self):
        contacts = [{'name': 'Alice', 'phone': '555-0001', 'email': ''}]
        assert contact_exists(contacts, "Alice") == True
        assert contact_exists(contacts, "David") == False


# Problem 4 Tests: JSON File Operations
class TestProblem4:
    def setup_method(self):
        """Clean up test files before each test"""
        self.cleanup()

    def teardown_method(self):
        """Clean up test files after each test"""
        self.cleanup()

    def cleanup(self):
        """Remove test files"""
        test_files = [
            'test_data.json', 'test_contacts.json', 'test_contacts_backup.json',
            'test_list1.json', 'test_list2.json', 'test_merged.json'
        ]
        for file in test_files:
            if os.path.exists(file):
                os.remove(file)

    def test_save_and_load_json(self):
        test_data = {'name': 'Alice', 'age': 25}
        save_to_json(test_data, 'test_data.json')
        loaded = load_from_json('test_data.json')
        assert loaded == test_data

    def test_save_and_load_contacts(self):
        contacts = [
            {'name': 'Alice', 'phone': '555-0001', 'email': 'alice@email.com'}
        ]
        save_contacts_to_file(contacts, 'test_contacts.json')
        loaded = load_contacts_from_file('test_contacts.json')
        assert len(loaded) == 1
        assert loaded[0]['name'] == 'Alice'

    def test_append_contact_to_file(self):
        contacts = [{'name': 'Alice', 'phone': '555-0001', 'email': ''}]
        save_contacts_to_file(contacts, 'test_contacts.json')
        new_contact = {'name': 'Bob', 'phone': '555-0002', 'email': ''}
        append_contact_to_file(new_contact, 'test_contacts.json')
        loaded = load_contacts_from_file('test_contacts.json')
        assert len(loaded) == 2

    def test_backup_file(self):
        data = {'test': 'data'}
        save_to_json(data, 'test_data.json')
        backup_file('test_data.json', 'test_data_backup.json')
        backup_data = load_from_json('test_data_backup.json')
        assert backup_data == data
        os.remove('test_data_backup.json')

    def test_get_file_stats(self):
        contacts = [{'name': 'Alice', 'phone': '555-0001', 'email': ''}]
        save_contacts_to_file(contacts, 'test_contacts.json')
        stats = get_file_stats('test_contacts.json')
        assert stats['exists'] == True
        assert stats['type'] == 'list'
        assert stats['count'] == 1

    def test_merge_json_files(self):
        list1 = [1, 2, 3]
        list2 = [4, 5, 6]
        save_to_json(list1, 'test_list1.json')
        save_to_json(list2, 'test_list2.json')
        merge_json_files('test_list1.json', 'test_list2.json', 'test_merged.json')
        merged = load_from_json('test_merged.json')
        assert merged == [1, 2, 3, 4, 5, 6]

    def test_search_json_file(self):
        contacts = [
            {'name': 'Alice', 'phone': '555-0001', 'email': ''},
            {'name': 'Bob', 'phone': '555-0002', 'email': ''}
        ]
        save_contacts_to_file(contacts, 'test_contacts.json')
        results = search_json_file('test_contacts.json', 'name', 'Alice')
        assert len(results) == 1
        assert results[0]['name'] == 'Alice'


# Bonus Tests: Recursion (Optional)
class TestBonusRecursion:
    def test_recursion_available(self):
        """Test if bonus recursion file exists"""
        try:
            import bonus_recursion
            assert True
        except ImportError:
            pytest.skip("Bonus recursion not implemented")

    def test_factorial(self):
        try:
            from bonus_recursion import factorial
            assert factorial(5) == 120
            assert factorial(0) == 1
        except ImportError:
            pytest.skip("Bonus recursion not implemented")

    def test_sum_list(self):
        try:
            from bonus_recursion import sum_list
            assert sum_list([1, 2, 3, 4, 5]) == 15
        except ImportError:
            pytest.skip("Bonus recursion not implemented")


if __name__ == "__main__":
    # Run tests with verbose output
    pytest.main([__file__, "-v", "--tb=short"])
