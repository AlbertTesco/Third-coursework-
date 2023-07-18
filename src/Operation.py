import datetime


class Operation:

    def __init__(self,
                 operation_id: int,
                 state: str,
                 date: str,
                 amount: float,
                 currency_name: str,
                 currency_code: str,
                 description: str,
                 destination: str,
                 sender: str
                 ):
        self.operation_id = operation_id
        self.state = state
        self.date = date
        # self.date = datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%f')
        self.amount = amount
        self.currency_name = currency_name
        self.currency_code = currency_code
        self.description = description
        self.sender = sender
        self.destination = destination

    def get_masked_sender_info(self) -> str:
        """
        Mask sender info
        :return: string with masked sender info
        """

        new_line = self.sender.split(' ')

        line_number = self.sender.split(' ')[-1]
        line_number = line_number[:6] + "*" * 6 + line_number[12:]
        line_number = [line_number[i:i + 4] for i in range(0, len(line_number), 4)]
        line_number = " ".join(line_number)
        new_line[-1] = "".join(line_number)

        return ' '.join(new_line)

    def get_masked_destination_info(self) -> str:
        """
        Mask destination info
        :return: string with masked destination info
        """

        new_line = self.destination.split(' ')
        line_number = self.destination.split(' ')[-1]
        line_number = "**" + line_number[-4:]
        new_line[-1] = "".join(line_number)

        return ' '.join(new_line)

    def get_data(self) -> str:
        """
        Get data of the operation
        :return: string with data of the operation
        """
        date = datetime.datetime.strptime(self.date, '%Y-%m-%dT%H:%M:%S.%f').strftime('%d.%m.%Y')
        return date

    def get_operation_info(self) -> str:
        """
        Get info of the operation
        """
        result_string = f"{self.get_data()} {self.description}\n"

        if self.sender is not None:
            result_string += f"{self.get_masked_sender_info()} -> {self.get_masked_destination_info()}\n"
        else:
            result_string += f"{self.get_masked_destination_info()}\n"

        result_string += f"{self.amount} {self.currency_name}\n"

        return result_string
