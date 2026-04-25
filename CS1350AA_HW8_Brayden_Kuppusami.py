
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None


def safe_get_item(lst, index):
    try:
        return lst[index]
    except IndexError:
        return 'Not found'


def convert_to_number(value):
    try:
        
        return int(value)
    except (ValueError, TypeError):
        try:
            
            return float(value)
        except (ValueError, TypeError):
            return None
my_list = [1, 2, 3]
print(f"Item at index 1: {safe_get_item(my_list, 1)}")
print(f"Item at index 10: {safe_get_item(my_list, 10)}")

test_values = ["42", "3.14", "hello", None]
for val in test_values:
    result = convert_to_number(val)
    print(f"Converting '{val}': {result}")
print("=============================")

def access_data(data_structure, key):
    try:
        return data_structure[key]
    except LookupError:
        return None

def parse_value(value):
    try:
        return int(value)
    except (ValueError, TypeError):
        try:
            return float(value)
        except (ValueError, TypeError):
            return str(value)


print("\nEXERCISE 2: Exception Hierarchy")
test_list = [10, 20, 30]
test_dict = {'a': 1, 'b': 2}

print(f"list[1]: {access_data(test_list, 1)}")
print(f"list[10]: {access_data(test_list, 10)}")
print(f"dict['a']: {access_data(test_dict, 'a')}")
print(f"dict['z']: {access_data(test_dict, 'z')}")

parse_tests = ["42", "3.14", "hello", None]
for val in parse_tests:
    result = parse_value(val)
    print(f"Parsing '{val}': {result} (type: {type(result).__name__})")
print("=============================")

def process_file(filename):
    file = None
    try:
        file = open(filename, 'r')
    except FileNotFoundError:
        return "Error: File not found"
    except PermissionError:
        return "Error: Permission denied"
    except Exception as e:
        return f"Error: {e}"
    else:
        content = file.read()
        return f"Content: {content}"
    finally:
        if file:
            file.close()

class ResourceManager:
    def __init__(self, name):
        self.name = name
        self.resource = None

    def acquire(self):
        print(f"Acquiring {self.name}...")
        self.resource = "Active"

    def release(self):
        print(f"Releasing {self.name}...")
        self.resource = None

    def use(self):
        if not self.resource:
            raise RuntimeError("Resource not acquired!")
        print(f"Using {self.name}...")


print("\nEXERCISE 3: Complete Exception Pattern")
test_files = ["exists.txt", "missing.txt", "/root/file"]
for filename in test_files:
   
    result = process_file(filename)
    print(f"Processing '{filename}': {result}")

print("\nResource Manager Test:")
rm = ResourceManager("Database")
try:
    rm.acquire()
    rm.use()
except Exception as e:
    print(f"Caught: {e}")
finally:
    rm.release()

print("=============================")

class GameError(Exception):
    """Base class for game exceptions."""
    pass

class InvalidMoveError(GameError):
    """Invalid game move."""
    def __init__(self, position, reason):
        self.position = position
        self.reason = reason
        super().__init__(f"Invalid move at {position}: {reason}")

class GameOverError(GameError):
    """Game has ended."""
    def __init__(self, winner):
        self.winner = winner
        super().__init__(f"Game is already over. Winner: {winner}")


class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.game_over = False

    def make_move(self, row, col):
        
        if self.game_over:
            raise GameOverError("None (Draw or finished)")
            
        
        if not (0 <= row < 3 and 0 <= col < 3):
            raise InvalidMoveError((row, col), "Position out of bounds")
            
        
        if self.board[row][col] != ' ':
            raise InvalidMoveError((row, col), "Square already occupied")

        self.board[row][col] = self.current_player
        

print("EXERCISE 1: Custom Exceptions")
game = TicTacToe()
test_moves = [(0, 0), (0, 0), (5, 5)]

for row, col in test_moves:
    try:
        game.make_move(row, col)
        print(f"Move ({row}, {col}) successful")
    except InvalidMoveError as e:
        print(f"❌ Invalid move: {e}")
    except GameOverError as e:
        print(f"🏁 Game over: {e}")
print("=============================")

import os

class FileProcessor:
    def __init__(self):
        self.processed_files = []
        self.failed_files = []

    def process_file(self, filename):
        """Process a single file with complete error handling."""
        file = None
        try:
            
            file = open(filename, 'r')
            data = file.read()
        except FileNotFoundError:
            self.failed_files.append((filename, "File not found"))
        except PermissionError:
            self.failed_files.append((filename, "Permission denied"))
        except Exception as e:
            self.failed_files.append((filename, str(e)))
        else:
            
            self.processed_files.append(filename)
            return data
        finally:
            
            if file:
                file.close()

    def process_directory(self, file_list):
        """Process all files in a list, collecting errors."""
        for filename in file_list:
            self.process_file(filename)

    def get_report(self):
        """Return summary of processing."""
        return {
            "Successes": self.processed_files,
            "Failures": self.failed_files
        }

print("\nEXERCISE 2: Complete Error Handler")
processor = FileProcessor()
test_files = ["valid.txt", "missing.txt", "/root/restricted.txt"]


processor.process_directory(test_files)


report = processor.get_report()
print(f"Report: {report}")