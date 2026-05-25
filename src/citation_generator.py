class CitationGenerator:
    SUPPORTED_STYLES = ["APA", "MLA", "Chicago"]
    SUPPORTED_EXPORTS = ["txt", "md"]
    VALID_ISBN_LENGTHS = [10, 13]

    def validate_source(self, source: str) -> bool:
        """
        Перевіряє коректність DOI, URL або ISBN.
        """

        if not source:
            raise ValueError("Source cannot be empty")

        if source.startswith("10."):
            return True

        if source.startswith(("http://", "https://")):
            return True

        if len(source.replace("-", "")) in self.VALID_ISBN_LENGTHS:
            return True

        return False

    def validate_style(self, style: str) -> bool:
        """
        Перевіряє чи підтримується стиль цитування.
        """

        return style in self.SUPPORTED_STYLES

    def generate_citation(self, source: str, style: str) -> str:
        """
        Генерує цитування у вибраному стилі.
        """

        if not self.validate_source(source):
            raise ValueError("Invalid source")

        if not self.validate_style(style):
            raise ValueError("Unsupported citation style")

        return f"[{style}] Citation generated for: {source}"

    def export_citation(self, citation: str, export_format: str) -> str:
        """
        Експортує цитування у файл.
        """

        if not citation:
            raise ValueError("Citation cannot be empty")

        if export_format not in self.SUPPORTED_EXPORTS:
            raise ValueError("Unsupported export format")

        return f"citation_exported.{export_format}"

    def save_history(self, history: list, citation: str) -> list:
        """
        Зберігає цитування в історію.
        """

        if len(history) >= 10:
            history.pop(0)

        history.append(citation)

        return history