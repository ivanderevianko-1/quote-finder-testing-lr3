import pytest

from src.citation_generator import CitationGenerator


# --- Тести validate_source ---


def test_validate_valid_doi():
    # EP Positive Test
    # Arrange
    generator = CitationGenerator()

    # Act
    result = generator.validate_source("10.1000/xyz123")

    # Assert
    assert result is True


def test_validate_valid_url():
    # EP Positive Test
    # Arrange
    generator = CitationGenerator()

    # Act
    result = generator.validate_source("https://example.com")

    # Assert
    assert result is True


def test_validate_valid_isbn():
    # EP Positive Test
    # Arrange
    generator = CitationGenerator()

    # Act
    result = generator.validate_source("1234567890")

    # Assert
    assert result is True


def test_validate_empty_source():
    # EP Negative Test
    # Arrange
    generator = CitationGenerator()

    # Act + Assert
    with pytest.raises(ValueError):
        generator.validate_source("")


def test_validate_invalid_source():
    # EP Negative Test
    # Arrange
    generator = CitationGenerator()

    # Act
    result = generator.validate_source("invalid_source")

    # Assert
    assert result is False


# --- Тести generate_citation ---


def test_generate_valid_citation():
    # EP Positive Test
    # Arrange
    generator = CitationGenerator()

    # Act
    result = generator.generate_citation(
        "10.1000/xyz123",
        "APA"
    )

    # Assert
    assert "APA" in result


def test_generate_invalid_style():
    # EP Negative Test
    # Arrange
    generator = CitationGenerator()

    # Act + Assert
    with pytest.raises(ValueError):
        generator.generate_citation(
            "10.1000/xyz123",
            "IEEE"
        )


# --- Тести export_citation ---


def test_export_txt():
    # EP Positive Test
    # Arrange
    generator = CitationGenerator()

    # Act
    result = generator.export_citation(
        "Test citation",
        "txt"
    )

    # Assert
    assert result == "citation_exported.txt"


def test_export_invalid_format():
    # EP Negative Test
    # Arrange
    generator = CitationGenerator()

    # Act + Assert
    with pytest.raises(ValueError):
        generator.export_citation(
            "Test citation",
            "pdf"
        )


# --- Тести save_history ---


def test_save_history():
    # EP Positive Test
    # Arrange
    generator = CitationGenerator()
    history = []

    # Act
    result = generator.save_history(
        history,
        "Citation 1"
    )

    # Assert
    assert len(result) == 1


def test_history_limit():
    # BVA Test
    # Arrange
    generator = CitationGenerator()

    history = [
        "1", "2", "3", "4", "5",
        "6", "7", "8", "9", "10"
    ]

    # Act
    result = generator.save_history(
        history,
        "11"
    )

    # Assert
    assert len(result) == 10
    assert "1" not in result