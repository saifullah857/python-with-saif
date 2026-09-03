

## 1️⃣ Normal Programming → OOP

```text
Normal Programming
       │
       ▼
Procedural Programming
       │
       │  Functions
       ▼
      OOP
       │
       ├── Classes
       └── Objects
```

```python
# Normal -->   Procedural programing (fnx)  --> OOP (classes , objects)
```

### 🏗️ Class = Blueprint

Class ek **blueprint** hoti hai jo 2 cheezen store karti hai:

```text
                 CLASS
                   │
          ┌────────┴────────┐
          ▼                 ▼
     Properties           Methods
       (Data)          (Functions)
     Variables          Procedures
```

### 1. Properties

Data / Variables

### 2. Methods

Functions / Procedures

---

# 2️⃣ Simple Class & Objects

```python
class Student:
    course = "python"
    college = "Abbas College of Technology"
    duration = "3 monts"
    fee = 5000
    timing = "10:00 AM - 12:00 AM"

marrayam = Student()
marrayam_2 = Student()

print(marrayam.course, marrayam.college, marrayam.duration, marrayam.fee)

print(marrayam_2.course, marrayam_2.college, marrayam_2.duration, marrayam_2.fee)
```

### Graphical Representation

```text
                Student
               (CLASS)
                  │
        ┌─────────┴─────────┐
        │                   │
        ▼                   ▼
   marrayam              marrayam_2
   (OBJECT)               (OBJECT)
        │                   │
        ├─ course           ├─ course
        ├─ college          ├─ college
        ├─ duration         ├─ duration
        └─ fee              └─ fee
```

**Class** = Blueprint
**Object** = Blueprint se banne wali actual thing

Example:

```text
Class  → Student
Object → marrayam
Object → marrayam_2
```

---

# 3️⃣ Constructor in Python

## `__init__` Method

```text
__init__
   │
   ▼
object ko initialize krta hai
   │
   ▼
called everytime when we create object of class
```

Example:

```python
class Student:
    def __init__(self):
        print("Constructer was created")

marrayam = Student()
```

### Jab object create hota hai:

```text
Student()
   │
   ▼
__init__()
   │
   ▼
"Constructer was created"
```

---

# 4️⃣ Constructor with Parameters

```python
class Student:
    def __init__(self, name, course, duration, fee, timing):
        self.name = name
        self.course = course
        self.duration = duration
        self.fee = fee
        self.timing = timing

    def intro(self):
        print(
            f"Student name = {self.name} his / her course = {self.course} "
            f"with duration = {self.duration} paying fee = {self.fee} "
            f"and timing = {self.timing}"
        )


# yaha pr jo b pass hoga wo self mein save hoga
std1 = Student("Marrayam", "python", "3 monts", 5000, "10 - 12")
```

### Graphical Representation

```text
Student(
    "Marrayam",
    "python",
    "3 monts",
    5000,
    "10 - 12"
)
        │
        ▼
      std1
        │
        ├── name     → Marrayam
        ├── course   → python
        ├── duration → 3 monts
        ├── fee      → 5000
        └── timing   → 10 - 12
```

### `self` kya hai?

```text
self
 │
 ▼
current object ka reference
```

Yani:

```python
self.name = name
```

ka matlab:

```text
current object ka name = jo name pass hua
```

---

# 5️⃣ Types of Constructor

```text
             Constructor
                  │
          ┌───────┴────────┐
          ▼                ▼
       Default         Parameterized
          │                │
        self        self + parameters
```

### 1. Default

```text
self
```

### 2. Parameterized Constructor

```text
self + parameters
```

> **Note:** only one constructor hona cheiay hr aik class k liay.

---

# 6️⃣ Attributes in Class and Objects

Attributes ko 2 types mein divide kar sakte hain:

```text
             Attributes
                  │
          ┌───────┴────────┐
          ▼                ▼
    Class Attribute    Instance Attribute
          │                │
       Common           Unique
     for objects       for objects
```

---

## 🟦 1. Class Attribute

Attributes belong to **class** → common for all objects.

```python
class Student:
    course = "python"
    college = "Abbas College of Technology"
    duration = "3 monts"
    fee = 5000
```

### Representation

```text
              Student CLASS
                   │
       ┌───────────┼───────────┐
       ▼           ▼           ▼
    course      college       fee
    python      Abbas...      5000
       ▲           ▲           ▲
       │           │           │
       └────── common ─────────┘
              for objects
```

---

## 🟩 2. Instance Attribute

Attributes belong to **object** → unique for all objects.

```python
class Student:
    def __init__(self, name, course, duration, fee, timing):
        self.name = name
        self.course = course
        self.duration = duration
        self.fee = fee
        self.timing = timing

    def intro(self):
        print(
            f"Student name = {self.name} his / her course = {self.course} "
            f"with duration = {self.duration} paying fee = {self.fee} "
            f"and timing = {self.timing}"
        )

std1 = Student("Marrayam", "python", "3 monts", 5000, "10 - 12")
```

### Representation

```text
             Student CLASS
                   │
              creates object
                   │
                   ▼
                  std1
                   │
       ┌───────────┼────────────┐
       ▼           ▼            ▼
     name       course         fee
   Marrayam     python        5000
```

### Important Note

```python
Student.course
```

✅ Works

Because `course` is a **class attribute**.

But:

```python
Student.name
```

❌ Error

Because `name` is an **object/instance attribute**.

---

# 7️⃣ Methods in Class

Methods ki **3 types**:

```text
                  Methods
                     │
        ┌────────────┼────────────┐
        ▼            ▼            ▼
    Instance       Class        Static
     Method        Method       Method
        │            │            │
       self          cls          none
```

---

# 8️⃣ Instance Method

### Instance Method

```text
compalsary parameter → self
```

It can also access:

```text
Instance Attributes
        +
Class Attributes
```

Example:

```python
class Laptop:
    storage_type = "ssd"  # class attr

    def __init__(self, name, RAM, storage):
        self.name = name
        self.RAM = RAM
        self.storage = storage

    def intro(self):  # instance method
        print(
            f"Lapton = {self.name} | RAM = {self.RAM} "
            f"| storage = {self.storage} "
            f"| storage_type = {self.storage_type}"
        )


l1 = Laptop("Lenovo", "8GB", "256")
l2 = Laptop("HP", "16GB", "256")

l2.intro()
```

### Representation

```text
              Laptop CLASS
                   │
             ┌─────┴─────┐
             ▼           ▼
            l1           l2
         (OBJECT)     (OBJECT)
             │           │
        ┌────┼───┐   ┌───┼────┐
        ▼    ▼   ▼   ▼   ▼    ▼
      name RAM storage name RAM storage
     Lenovo 8GB 256    HP  16GB 256

              │
              ▼
        l2.intro()
              │
              ▼
            self
              │
              ▼
             l2
```

### Key Point

```text
self → current object
```

---

# 9️⃣ Class Method

```text
1st parameter → cls
```

Class method:

```text
@classmethod
```

decorator use karta hai.

```text
Class Method
     │
     ▼
   cls
     │
     ▼
  Class
     │
     ▼
Class Attributes
```

Example:

```python
class Laptop:
    storage_type = "ssd"  # class attr

    def __init__(self, name, RAM, storage):
        self.name = name
        self.RAM = RAM
        self.storage = storage

    def intro(self):  # instance method
        print(
            f"Lapton = {self.name} | RAM = {self.RAM} "
            f"| storage = {self.storage} "
            f"| storage_type = {self.storage_type}"
        )

    @classmethod  # change the behaviour to make it class method
    def get_storage_type(cls):  # only can access class attr
        print(f"storage type = {cls.storage_type}")


l1 = Laptop("Lenovo", "8GB", "256")
l2 = Laptop("HP", "16GB", "256")

l1.get_storage_type()
```

### Representation

```text
              Laptop CLASS
                   │
                   │
                  cls
                   │
                   ▼
          Laptop.storage_type
                   │
                   ▼
                  "ssd"
```

### `self` vs `cls`

```text
┌──────────────────────────────┐
│          self                │
│              ↓               │
│       Current OBJECT         │
└──────────────────────────────┘

┌──────────────────────────────┐
│           cls                │
│              ↓               │
│          CLASS               │
└──────────────────────────────┘
```

---

# 🔟 Decorator

```text
decorator
    │
    ▼
take another fnx
    │
    ▼
change its behaviour
    │
    ▼
return it
```

Example:

```python
@classmethod
```

Ye normal method ke behaviour ko **class method** mein change karta hai.

---

# 1️⃣1️⃣ Static Method

```text
Static Method
      │
      ├── no self
      ├── no cls
      └── no direct access to class/instance attributes
```

Iske liye:

```python
@staticmethod
```

decorator use hota hai.

### Used to:

```text
combine related logic of class
```

Example:

```python
class Laptop:
    storage_type = "ssd"  # class attr

    def __init__(self, name, RAM, storage):
        self.name = name
        self.RAM = RAM
        self.storage = storage

    def intro(self):  # instance method
        print(
            f"Lapton = {self.name} | RAM = {self.RAM} "
            f"| storage = {self.storage} "
            f"| storage_type = {self.storage_type}"
        )

    @classmethod  # change the behaviour to make it class method
    def get_storage_type(cls):  # only can access class attr
        print(f"storage type = {cls.storage_type}")

    @staticmethod
    def discount(price, discount):
        final_price = price - (discount * price / 100)
        print(f"discounted price = {final_price}")


l1 = Laptop("Lenovo", "8GB", "256")
l2 = Laptop("HP", "16GB", "256")

l2.discount(50000, 20)
```

Output:

```text
discounted price = 40000.0
```

---

# 🧠 Final Revision — Students ko ye diagram zaroor dikhao

```text
                         OOP
                          │
                     ┌────┴────┐
                     ▼         ▼
                  Classes    Objects
                     │         │
                     │         │
              ┌──────┴──────┐  │
              ▼             ▼  │
         Properties       Methods
              │             │
              │       ┌─────┼────────┐
              │       ▼     ▼        ▼
              │   Instance Class   Static
              │     self    cls     none
              │
       ┌──────┴──────┐
       ▼             ▼
 Class Attribute  Instance Attribute
    common            unique
```

