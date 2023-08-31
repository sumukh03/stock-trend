from datetime import datetime, timedelta

def generate_date_list(start_date, num_days, date_format='%Y-%m-%d'):
    """
    Generate a list of dates starting from the given start_date and continuing for the specified number of days.
    
    Parameters:
        start_date (str): The start date in 'YYYY-MM-DD' format.
        num_days (int): The number of days to generate.
        date_format (str, optional): The desired date string format. Default is '%Y-%m-%d'.
        
    Returns:
        list: A list of date strings in the specified format.
    """
    date_list = []
    current_date = datetime.strptime(start_date, '%Y-%m-%d')
    
    for _ in range(num_days):
        date_list.append(current_date.strftime(date_format))
        current_date += timedelta(days=1)
    
    return date_list

if __name__=="__main__":
    # Calling the function to generate a list of dates
    start_date = '2023-08-01'
    num_days = 10
    date_format = '%Y-%m-%d'

    dates = generate_date_list(start_date, num_days, date_format)
    print(dates)
