from BackToSender import calculate_wage

def test_less_than_50_percent():
    assert calculate_wage(25) == 9000   

def test_fifty_to_fifty_nine_percent():
    assert calculate_wage(50) == 15000  

def test_sixty_to_sixty_nine_percent():
    assert calculate_wage(60) == 20000  

def test_seventy_percent_and_above():
    assert calculate_wage(80) == 45000  
