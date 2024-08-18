from datetime import datetime

def read_products_file(file_name):
    products = {}
    try:
        with open(file_name, 'r') as file:
            for line in file:
                product_id, product_name, price = line.strip().split(',')
                products[product_id] = [product_name, float(price)]
    except FileNotFoundError:
        print("Error: missing file")
        print(f"[Errno 2] No such file or directory: '{file_name}'")
    except PermissionError:
        print("Error: permission issue with the file")
        print(f"[Errno 13] Permission denied: '{file_name}'")
    return products

def process_order(file_name, products):
    ordered_items = []
    try:
        with open(file_name, 'r') as file:
            for line in file:
                product_id, quantity = line.strip().split(',')
                if product_id in products:
                    product_name, price = products[product_id]
                    ordered_items.append((product_name, int(quantity), price))
                else:
                    raise KeyError(product_id)
    except FileNotFoundError:
        print("Error: missing file")
        print(f"[Errno 2] No such file or directory: '{file_name}'")
    except PermissionError:
        print("Error: permission issue with the file")
        print(f"[Errno 13] Permission denied: '{file_name}'")
    except KeyError as e:
        print("Error: unknown product ID in the request.csv file")
        print(f"'{str(e)}'")

    return ordered_items

def print_receipt(store_name, ordered_items):
    print(store_name + "\n")
    for item in ordered_items:
        product_name, quantity, price = item
        print(f"{product_name}: {quantity} @ {price:.2f}")
    print()
    num_items = sum(item[1] for item in ordered_items)
    print(f"Number of Items: {num_items}")

    subtotal = sum(item[1] * item[2] for item in ordered_items)
    print(f"Subtotal: {subtotal:.2f}")

    tax_rate = 0.06
    sales_tax = subtotal * tax_rate
    print(f"Sales Tax: {sales_tax:.2f}")

    total = subtotal + sales_tax
    print(f"Total: {total:.2f}\n")

    print("Thank you for shopping at the Inkom Emporium.")
    current_date_and_time = datetime.now()
    print(current_date_and_time.strftime("%a %b %d %H:%M:%S %Y"))