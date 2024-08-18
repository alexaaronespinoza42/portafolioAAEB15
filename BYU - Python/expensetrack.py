import datetime
import csv
import math
import random
import requests
import pandas as pd
import tkinter as tk
import pytest


# Expense management functions
def add_expense(amount, date, description, category):
    expense = {
        'id': len(expenses) + 1,
        'amount': amount,
        'date': date,
        'description': description,
        'category': category
    }
    expenses.append(expense)


def edit_expense(expense_id, new_expense_data):
    for expense in expenses:
        if expense['id'] == expense_id:
            expense.update(new_expense_data)
            break


def delete_expense(expense_id):
    for expense in expenses:
        if expense['id'] == expense_id:
            expenses.remove(expense)
            break


def get_expense(expense_id):
    for expense in expenses:
        if expense['id'] == expense_id:
            return expense
    return None


def get_all_expenses():
    return expenses


def save_expenses_to_csv(filename):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['id', 'amount', 'date', 'description', 'category']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(expenses)


def load_expenses_from_csv(filename):
    expenses.clear()
    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            expenses.append(row)


# Test functions
def test_add_expense():
    add_expense(50, "2023-07-17", "Lunch", "Food")
    expense = get_expense(1)
    assert expense is not None
    assert expense['amount'] == 50


def test_edit_expense():
    edit_expense(1, {'amount': 60, 'category': 'Dining Out'})
    expense = get_expense(1)
    assert expense['amount'] == 60
    assert expense['category'] == 'Dining Out'


def test_delete_expense():
    delete_expense(1)
    expense = get_expense(1)
    assert expense is None


@pytest.mark.parametrize('tmp_path', ['.'])
def test_load_expenses_from_csv(tmp_path):
    csv_file = tmp_path / 'expenses.csv'
    add_expense(50, "2023-07-15", "Groceries", "Food")
    add_expense(100, "2023-07-15", "Dinner", "Food")
    save_expenses_to_csv(csv_file)
    load_expenses_from_csv(csv_file)
    assert len(expenses) == 2
    assert expenses[0]['amount'] == '50'
    assert expenses[1]['amount'] == '100'


def test_math_functions():
    assert math.sqrt(16) == 4
    assert math.factorial(5) == 120


def test_random_module():
    random_number = random.randint(1, 10)
    assert 1 <= random_number <= 10


def test_requests_module():
    response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
    assert response.status_code == 200


def test_pandas_module():
    data = {'Name': ['John', 'Jane', 'Mike'], 'Age': [25, 30, 35]}
    df = pd.DataFrame(data)
    assert df.shape == (3, 2)


def test_tkinter_module():
    root = tk.Tk()
    assert isinstance(root, tk.Tk)


# Main program
users = {}
expenses = []
categories = {}


def register_user(username, password):
    users[username] = password


def login(username, password):
    if username in users and users[username] == password:
        return True
    return False


def add_category(name):
    categories[name] = []


def edit_category(category_id, new_category_name):
    if category_id in categories:
        categories[new_category_name] = categories.pop(category_id)


def delete_category(category_id):
    if category_id in categories:
        del categories[category_id]


def get_all_categories():
    return categories.keys()


def set_budget(category, amount):
    categories[category] = amount


def get_budget(category):
    return categories.get(category, None)


def generate_expense_report(start_date, end_date):
    report = []
    for expense in expenses:
        expense_date = datetime.datetime.strptime(expense['date'], '%Y-%m-%d').date()
        if start_date <= expense_date <= end_date:
            report.append(expense)
    return report


def generate_category_report():
    report = {}
    for expense in expenses:
        category = expense['category']
        if category not in report:
            report[category] = 0
        report[category] += expense['amount']
    return report


def generate_budget_report():
    report = {}
    for category, budget in categories.items():
        total_expenses = sum(expense['amount'] for expense in expenses if expense['category'] == category)
        report[category] = {
            'budget': budget,
            'expenses': total_expenses,
            'remaining': budget - total_expenses
        }
    return report


# Execute test functions
def run_tests():
    test_add_expense()
    test_edit_expense()
    test_delete_expense()
    test_math_functions()
    test_random_module()
    test_requests_module()
    test_pandas_module()
    test_tkinter_module()

    print("All test functions passed successfully.")


if __name__ == '__main__':
    run_tests()


if __name__ == '__main__':
    run_tests()
