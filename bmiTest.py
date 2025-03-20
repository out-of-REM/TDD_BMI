import pytest
from BodyMassIndex import BMICalc, Categorization

#Tolerance for change is 0.1
tol = 0.1

#Tests different cases of the BMI Calc function
#Normal Weight, Underweight, OVerweight, Obese expected in this order
@pytest.mark.parametrize("feet, inches, weight, expBMI", [
  (5, 8, 125, round((125 * 0.45) / ((68 * 0.025) ** 2), 1)),
  (5, 4, 90, round((90 * 0.45) / ((64 * 0.025) ** 2), 1)),
  (5, 10, 200, round((200 * 0.45) / ((70 * 0.025) ** 2), 1)),
  (5, 6, 250, round((250 * 0.45) / ((66 * 0.025) ** 2), 1)),
  (5, 8, 0, None), #Zero weight
  (0, 0, 150, None) #Zero Height
  (-5, 8, 150, None) #Negative Height
  (5, 8, -150, None), #Negative Weight
])

def test_BMICalc(feet, inches, weight, expBMI): 
  if expBMI is None:
    with pytest.raises(ValueError):
      BMICalc(feet, inches, weight)
  else:
    assert abs(BMICalc(feet, inches, weight) - expBMI) < tol


#Tests the classification logic function using strong boundary testing for creating test cases
@pytest.mark.parametrize("bmi, expCat", [
  (18.4, "Underweight"), #Just below Underweight/Normal boundary
  (18.5, "Normal Weight"), #Lower boundary of Normal
  (18.6, "Normal Weight"), #Just inside normal
  (24.8, "Normal Weight"), #Just inside the upper boundary of Normal
  (24.9, "Normal Weight"), #On the upper boundary of normal
  (25.0, "Overweight"), #On the lower boundary of overweight
  (25.1, "Overweight"), #Just inside the lower boundary of overweight
  (29.8, "Overweight"), #Just inside the upper boundary of overweight
  (29.9, "Overweight"), #On the upper boundary of overweight
  (30.0, "Obese"), #On the lower boundary of obese
  (30.1, "Obese"), #Inside of the obese range
])

def test_Categorization(bmi, expCat):
  assert Categorization(bmi) == expCat
