class Flight:

    def __init__(self, number, aircraft):
        if not number[:2].isalpha():
            raise ValueError("No Simbol in: {}".format(number))
        if not number[:2].isupper():
            raise ValueError("No Upper in: {}".format(number))
        if not number[2:].isdigit():
            raise ValueError("No digital in: {}".format(number))
        self._number = number
        self._aircraft = aircraft
        rows, seats = self._aircraft.seating_plan()
        self._seating = [None] + [{letter: None for letter in seats} for _ in rows]

    def number(self):
        return self._number

    def airline(self):
        return self._number[:2]

    def aircraft_model(self):
        return self._aircraft.model()

    def allocate_seat(self, seat, passenger):
        rows, seat_letters = self._aircraft.seating_plan()
        letter = seat[-1]

        row_text = seat[:-1]
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError("Invalid seat number {}".format(row_text))

        self._seating[row][letter] = passenger


class Aircraft:

    def __init__(self, reg, model, num_rows, num_seats):
        self._reg = reg
        self._model = model
        self._num_rows = num_rows
        self._num_seats = num_seats

    def registraion(self):
        return self._reg

    def model(self):
        return self._model

    def seating_plan(self):
        return (range(1, self._num_rows + 1),
                "ABCDEFGHJK"[:self._num_seats])