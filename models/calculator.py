class Calculator:

    def all_count(self, number) -> float:
        new_number = number/3
        a = self.__second_count(new_number) 
        b = self.__third_count(new_number)
        c = self.__fourth_count(new_number)

        return print((a + b + c))

    def __second_count(self, number) -> float:
        new_number = (((number/4) + 7)**2)*0.257
        return new_number

    def __third_count(self, number) -> float:
        new_number = ((number**2.121)/5) + 1
        return new_number

    def __fourth_count(self, number) -> float:
        return number
