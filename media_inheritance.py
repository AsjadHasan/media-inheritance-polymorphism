
"""Demonstrate inheritance and polymorphism using media types."""


class Media:
    """Base class representing a media item."""

    def __init__(self, title, price):
        """Initialize common media attributes."""
        self.title = title
        self.price = price

    def describe(self):
        """Return a description of the media item."""
        raise NotImplementedError("Subclasses must implement describe()")


class Book(Media):
    """Represent a book with an author."""

    def __init__(self, title, price, author):
        """Initialize book attributes."""
        super().__init__(title, price)
        self.author = author

    def describe(self):
        """Return the book description."""
        return f"Book: {self.title} by {self.author} - Rs.{self.price}"


class Magazine(Media):
    """Represent a magazine with a publication frequency."""

    def __init__(self, title, price, frequency):
        """Initialize magazine attributes."""
        super().__init__(title, price)
        self.frequency = frequency

    def describe(self):
        """Return the magazine description."""
        return f"Magazine: {self.title} ({self.frequency}) - Rs.{self.price}"


class DVD(Media):
    """Represent a DVD with a duration in minutes."""

    def __init__(self, title, price, duration):
        """Initialize DVD attributes."""
        super().__init__(title, price)
        self.duration = duration

    def describe(self):
        """Return the DVD description."""
        return f"DVD: {self.title}, {self.duration} mins - Rs.{self.price}"


def main():
    """Create media objects and display their descriptions."""
    media_items = [
        Book("Clean Code", 499, "Robert C. Martin"),
        Magazine("Wired", 150, "Monthly"),
        DVD("Inception", 299, 148)
    ]

    for item in media_items:
        print(item.describe())


if __name__ == "__main__":
    main()
