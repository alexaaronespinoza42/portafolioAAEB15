import water_flow
import pytest

def test_water_column_height():
    assert water_flow.water_column_height(10, 1.0) 
    assert water_flow.water_column_height(5, 0.5) 

def test_pressure_gain_from_water_height():
    assert water_flow.pressure_gain_from_water_height(10) 
    assert water_flow.pressure_gain_from_water_height(5) 

def test_pressure_loss_from_pipe():
    assert water_flow.pressure_loss_from_pipe(10, 0.1, 10) 
    assert water_flow.pressure_loss_from_pipe(5, 0.2, 5) 

def test_pressure_loss_from_fittings():
    assert water_flow.pressure_loss_from_fittings(10, 0.1, 2) 
    assert water_flow.pressure_loss_from_fittings(5, 0.2, 1) 

def test_reynolds_number():
    assert water_flow.reynolds_number(0.1, 10) 
    assert water_flow.reynolds_number(0.2, 5) 

def test_pressure_loss_from_pipe_reduction():
    assert water_flow.pressure_loss_from_pipe_reduction(10, 0.2, 0.1) 
    assert water_flow.pressure_loss_from_pipe_reduction(5, 0.4, 0.2) 
def run_tests():
    test_water_column_height()
    test_pressure_gain_from_water_height()
    test_pressure_loss_from_pipe()
    test_pressure_loss_from_fittings()
    test_reynolds_number()
    test_pressure_loss_from_pipe_reduction()

if __name__ == "__main__":
    run_tests()