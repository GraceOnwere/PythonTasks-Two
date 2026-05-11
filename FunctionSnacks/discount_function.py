def checkDiscountCode(item_name,original_price,promotional_code)

    promotional_code_error_message = 'Invalid Promotional Code'

    if promotional_code == 'SAVE10':

        discount = 0.1

        discounted_bill = original_price - (original_price * discount)
        
        return discounted_bill

    elif promotional_code == 'HALFOFF'

        discount = 0.5
    
        discounted_bill = original_price - (original_price * discount)

        return discounted_bill

    return promotional_code_error_message


