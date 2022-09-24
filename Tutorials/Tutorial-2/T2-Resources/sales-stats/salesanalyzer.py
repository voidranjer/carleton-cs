# ================================= PROBLEM 1 =================================

def get_number_purchases(filename):
    infile = open(filename, "r")

    # count total number of lines (#order)
    counter = 0
    for _ in infile:
        counter += 1

    infile.close()
    
    # divide by 6 to convert (#order) to (#purchase)
    return int(counter/6)

def get_total_purchases(filename):
    infile = open(filename, "r")
    num_lines = get_number_purchases(filename) * 6

    sum = 0
    for i in range(1, num_lines + 1):
        line = infile.readline()
        if (i%6 == 0): # if line number is a multiple/divisble by 6 (every 6th line of the file)
            sum += int(line)

    infile.close()
    return sum

def get_average_purchases(filename):
    num_purchases = get_number_purchases(filename)
    total_purchases = get_total_purchases(filename)
    return (round(total_purchases/num_purchases, 2)) # round of to 2 decimal places

# ================================= PROBLEM 1 =================================



# ================================= PROBLEM 2 =================================

def get_number_customer_purchases(filename, customer):
    infile = open(filename, "r")
    counter = 0
    for line in infile:
        if line.strip() == customer:
            counter += 1
    infile.close()
    return counter

def get_total_customer_purchases(filename, customer):
    infile = open(filename, "r")
    sum = 0
    line_num = 0

    # toggles shouldCapture to True when customer name matches search (next total purchase will be captured)
    shouldCapture = False
    for line in infile:
        line_num += 1
        if line.strip() == customer:
            shouldCapture = True

    # 6th line of the file (total purchase data)
        if (line_num%6 == 0 and shouldCapture):
            sum += int(line)
            shouldCapture = False

    infile.close()
    return sum

def get_average_customer_purchases(filename, customer):
    # Customer doesn't exist in record
    if (get_number_customer_purchases(filename, customer) == 0):
        return 0
    average = get_total_customer_purchases(filename, customer)/get_number_customer_purchases(filename, customer)
    return round(average, 2)

# ================================= PROBLEM 2 =================================



# ================================= PROBLEM 3 =================================

def get_most_popular_product(filename):
    infile = open(filename, "r")

    products = {"Desktop": 0, "Laptop": 0, "Tablet": 0, "Toaster": 0}
    
    n_purchases = get_number_purchases(filename)

    # NOTE: _ denotes a variable that will not be used at any point in time during execution
    for _ in range(n_purchases):
        infile.readline() # Name of customer (unused)
        for product in products:
            products[product] += int(infile.readline())
        infile.readline() # Total purchase cost (unused)
    
    infile.close()

    return max(products, key=products.get)

# ================================= PROBLEM 3 =================================