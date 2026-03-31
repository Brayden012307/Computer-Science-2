from abc import ABC, abstractmethod

# ==========================================================
# Problem 1: Employee Payroll System (50 points)
# ==========================================================

class Employee(ABC):
    def __init__(self, name, employee_id):
        self.name = name 
        self.employee_id = employee_id 

    @abstractmethod
    def calculate_pay(self):
        """Each subclass computes pay differently"""
        pass 

    @abstractmethod
    def description(self):
        """Returns a one-line summary of the employee"""
        pass 

    def pay_stub(self):
        pay = self.calculate_pay() 
        return f"{self.name} (ID: {self.employee_id}): ${pay:.2f}" 

    @staticmethod
    def validate_positive(value, name):
        if value <= 0: 
            raise ValueError(f"{name} must be positive!") 
        return True 

class SalariedEmployee(Employee):
    def __init__(self, name, employee_id, annual_salary):
        super().__init__(name, employee_id) 
        self.validate_positive(annual_salary, "annual_salary") 
        self.annual_salary = annual_salary 

    def calculate_pay(self):
        return self.annual_salary / 24 

    def description(self):
        return f"Salaried: {self.name}" 

class HourlyEmployee(Employee):
    def __init__(self, name, employee_id, hourly_rate, hours_worked):
        super().__init__(name, employee_id) 
        self.validate_positive(hourly_rate, "hourly_rate") 
        self.validate_positive(hours_worked, "hours_worked") 
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked 

    def calculate_pay(self):
        if self.hours_worked <= 40: 
            return self.hourly_rate * self.hours_worked 
        else:
            overtime = self.hours_worked - 40 
            return (40 * self.hourly_rate) + (overtime * self.hourly_rate * 1.5) 

    def description(self):
        return f"Hourly: {self.name}" 

class CommissionEmployee(Employee):
    def __init__(self, name, employee_id, base_salary, sales, commission_rate):
        super().__init__(name, employee_id) 
        self.validate_positive(base_salary, "base_salary") 
        self.validate_positive(sales, "sales") 
        self.validate_positive(commission_rate, "commission_rate") 
        if commission_rate > 1.0: 
            raise ValueError("commission_rate must be <= 1.0!") 
        self.base_salary = base_salary
        self.sales = sales
        self.commission_rate = commission_rate 

    def calculate_pay(self):
        return self.base_salary + (self.sales * self.commission_rate) 

    def description(self):
        return f"Commission: {self.name}" 

class Payroll:
    def __init__(self):
        self.employees = [] 

    def add_employee(self, employee):
        self.employees.append(employee) 

    def total_payroll(self):
        return sum(emp.calculate_pay() for emp in self.employees) 

    def print_all_stubs(self):
        for emp in self.employees: 
            print(emp.pay_stub()) 

# ==========================================================
# Problem 2: Music Library - Bonus (50 points)
# ==========================================================

class Song:
    total_songs = 0 

    def __init__(self, title, artist, duration_seconds):
        self.title = title
        self.artist = artist
        self.duration_seconds = duration_seconds 
        Song.total_songs += 1 

    def display(self):
        duration = self.format_duration(self.duration_seconds) 
        return f"{self.title} | {self.artist} ({duration})" 

    @classmethod
    def from_string(cls, s):
        parts = s.split(" | ")
        title, artist = parts[0], parts[1]
        seconds = cls.parse_duration(parts[2]) 
        return cls(title, artist, seconds) 

    @classmethod
    def get_total_songs(cls):
        return cls.total_songs 

    @staticmethod
    def format_duration(seconds):
        mins = seconds // 60 
        secs = seconds % 60 
        return f"{mins}:{secs:02d}"

    @staticmethod
    def parse_duration(duration_str):
        mins, secs = map(int, duration_str.split(":")) 
        return (mins * 60) + secs 

class Playlist:
    total_playlists = 0 

    def __init__(self, name):
        Playlist.total_playlists += 1 
        self.playlist_id = f"PL_{Playlist.total_playlists:03d}" 
        self.name = name
        self.songs = [] 

    def add_song(self, song):
        self.songs.append(song) 

    def total_duration(self):
        return sum(s.duration_seconds for s in self.songs) 

    def display(self):
        duration = Song.format_duration(self.total_duration())
        return f"Playlist: {self.name} ({len(self.songs)} songs, {duration})" 

    @classmethod
    def get_total_playlists(cls):
        return cls.total_playlists 

class LibraryManager:
    @staticmethod
    def create_playlist_from_strings(name, song_strings):
        playlist = Playlist(name) 
        for s in song_strings:
            playlist.add_song(Song.from_string(s)) 
        return playlist 

    @staticmethod
    def format_library_report(playlists):
        report = "=== LIBRARY REPORT ===\n" 
        total_all_songs = 0
        for pl in playlists:
            report += f"Playlist: {pl.name}\n"
            for i, song in enumerate(pl.songs, 1):
                report += f"{i}. {song.display()}\n" 
                total_all_songs += 1
            report += f"Duration: {Song.format_duration(pl.total_duration())}\n" 
        report += f"Total Songs: {total_all_songs}\n" 
        report += "=======================" 
        return report

# ==========================================================
# Problem 3: Smart GradeBook - Bonus (50 points)
# ==========================================================

class GradeBook:
    def __init__(self, course_name):
        self.course_name = course_name 
        self.grades = {} 

    def __str__(self):
        return f"GradeBook: {self.course_name} ({len(self.grades)} students)" 

    def __repr__(self):
        return f"GradeBook('{self.course_name}')" 

    def __len__(self):
        return len(self.grades) 

    def __getitem__(self, student):
        if student not in self.grades: 
            raise KeyError(f"{student} not found") 
        return self.grades[student] 

    def __setitem__(self, student, grade):
        if not (0 <= grade <= 100): 
            raise ValueError("Grade must be between 0 and 100") 
        self.grades[student] = grade 

    def __contains__(self, student):
        return student in self.grades 

    def __iter__(self):
        return iter(self.grades) 

    def __bool__(self):
        return len(self.grades) > 0 

    @property
    def average(self):
        if not self.grades: 
            return 0.0 
        return sum(self.grades.values()) / len(self.grades) 

    def __add__(self, other):
        new_gb = GradeBook(f"{self.course_name} + {other.course_name}") 
        # Merge self
        for student, grade in self.grades.items():
            new_gb.grades[student] = grade
        # Merge other (keep higher)
        for student, grade in other.grades.items():
            if student in new_gb.grades:
                new_gb.grades[student] = max(new_gb.grades[student], grade) 
            else:
                new_gb.grades[student] = grade
        return new_gb 

    def __iadd__(self, other):
        for student, grade in other.grades.items(): 
            if student in self.grades:
                self.grades[student] = max(self.grades[student], grade) 
            else:
                self.grades[student] = grade
        return self 

    def __mul__(self, factor):
        new_gb = GradeBook(f"{self.course_name} (curved)") 
        for student, grade in self.grades.items():
            curved_grade = min(100, grade * factor) 
            new_gb.grades[student] = curved_grade
        return new_gb 

    def __eq__(self, other):
        return abs(self.average - other.average) < 0.01 

    def __lt__(self, other):
        return self.average < other.average 

    def __le__(self, other):
        return self.average <= other.average 

# ==========================================================
# Main Execution Blocks (Provided in HW document)
# ==========================================================
if __name__ == "__main__":
    # Problem 1 Test
    alice = SalariedEmployee("Alice Johnson", "E001", 84000) 
    bob = HourlyEmployee("Bob Smith", "E002", 25.00, 45) 
    carol = CommissionEmployee("Carol Davis", "E003", 2000, 50000, 0.05) 
    
    payroll = Payroll() 
    payroll.add_employee(alice) 
    payroll.add_employee(bob) 
    payroll.add_employee(carol) 
    
    print("Employee Descriptions:")
    for emp in [alice, bob, carol]:
        print(f"  {emp.description()}") 
    
    print("\nPay Stubs:")
    payroll.print_all_stubs() 
    print(f"\nTotal Payroll: ${payroll.total_payroll():.2f}") 