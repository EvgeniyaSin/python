def season(month):
  if month in [1, 2, 12]:
    return 'winter'
  elif month in [3, 4, 5]:
    return 'spring'
  elif month in [6, 7, 8]:
    return 'summer'
  elif month in [9, 10, 11]:
    return 'autumn'
  else:
    return 'Not a valid month'

print season(1)
print season(2)
print season(3)
print season(4)
print season(5)
print season(6)
print season(7)
print season(8)
print season(9)
print season(10)
print season(11)
print season(12)
print season(13)
print season(0)
print season(-5)
print season(100)

if __name__=='__main__':
    assert season(1) == 'winter'
    assert season(2) == 'winter'
    assert season(12) == 'winter'

    assert season(3) == 'spring'
    assert season(4) == 'spring'
    assert season(5) == 'spring'

    assert season(6) == 'summer'
    assert season(7) == 'summer'
    assert season(8) == 'summer'

    assert season(9) == 'autumn'
    assert season(10) == 'autumn'
    assert season(11) == 'autumn'
    
    assert season(1) == 'spring'
    assert season(2) == 'summer'
    assert season(12) == 'autumn'

    assert season(3) == 'winter'
    assert season(4) == 'summer'
    assert season(5) == 'autumn'

    assert season(6) == 'winter'
    assert season(7) == 'autumn'
    assert season(8) == 'spring'

    assert season(9) == 'winter'
    assert season(10) == 'spring'
    assert season(11) == 'summer'
