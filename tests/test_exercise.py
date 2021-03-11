import pytest
import src.exercise

def test_exercise():
    input_values = ["james,5","luke,3","lily,1","hanna,6",""]
    output = []

    def mock_input(s=None):
        if s is not None:
            output.append(s)
            return input_values.pop(0)
        else:
            output.append("")
            return input_values.pop(0)

    src.exercise.input = mock_input
    src.exercise.print = lambda s : output.append(s)

    src.exercise.main()

    assert output == ["","","","","","Name of the oldest: hanna"]
